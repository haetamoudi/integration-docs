from functools import wraps
from collections import abc
import os
from os import path
import git
import jinja2
import shutil
import yaml

# Docs will be generated for these packages
INCLUDE_LIST = ["aws-cloudwatch",
                "aws-s3",
                "aws/metrics",
                "awsfargate/metrics",
                "azure-blob-storage",
                "azure-eventhub",
                "azure/metrics",
                "cel",
                "entity-analytics",
                "filestream",
                "gcp-pubsub",
                "gcp_metrics",
                "gcs",
                "http/metrics"
                "http_endpoint",
                "httpjson",
                "jolokia/metrics",
                "journald",
                "logfile",
                "netflow",
                "packet",
                "prometheus/metrics",
                "redis",
                "sql/metrics",
                "statsd/metrics",
                "system/metrics",
                "tcp",
                "udp",
                "winlog"]

def generate_doc(inputs):
    """
    Generate input docs

    :param inputs: dict of all inputs
    """
    # inputs.yaml contains extra info on inputs which isn't contained in the manifest.
    # Add this extra info to each input key before generating the docs
    with open(path.join(LOCAL_DIR, 'inputs.yml'), 'r') as extra_f:
        extra_info = yaml.safe_load(extra_f)
    inputs = merge_recursive(inputs, extra_info)

    print(f'{extra_info.keys()}\n\n\n')
    print(inputs.keys())

    for k,v in inputs.items():
        write(path.join(GENERATE_DIR, f'{k.replace("/","_")}.md'), inputs_doc(v))

def merge_recursive(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if (key in merged and
                isinstance(merged[key], abc.Mapping) and
                isinstance(value, abc.Mapping)):
            merged[key] = merge_recursive(merged[key], value)
        else:
            merged[key] = value
    return merged

def templated(template_name):
    """Decorator function to simplify rendering a template.

    :param template_name: the name of the template to be rendered
    """
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            ctx = func(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator

def render_template(template_name, **context):
    """Renders a template from the template folder with the given
    context.

    :param template_name: the name of the template to be rendered
    :param context: the variables that should be available in the
                    context of the template.
    """
    template = template_env.get_template(template_name)
    return template.render(**context)

def write(f, text):
    """
    Write text to file
    """
    os.makedirs(path.dirname(f), exist_ok=True)
    with open(f, "w") as outfile:
        outfile.write(text)
    print(f'Wrote file: {f}')

def find_inputs(integrations_dir):
    """
    Search the integrations dir for all input packages

    :return: dict of all input packages
    """
    found_files = []
    input_dict = {}
    for root, _, files in os.walk(integrations_dir):
        for file in files:
            if file == 'manifest.yml':
                full_path = path.join(root, file)
                found_files.append(full_path)
    for file in found_files:
        with open(file, 'r') as f:
            manifest = yaml.safe_load(f)
            if manifest.get('type') == 'input' or manifest.get('name') in INCLUDE_LIST:
                input_dict[manifest['name']] = manifest
    return input_dict

def get_tree_by_url(
    url: str,
    git_ref: str,
) -> git.objects.tree.Tree:
    repo: git.repo.base.Repo
    clone_from_remote = False
    if os.path.exists(LOCAL_TARGET_GIT_DIR):
        repo = git.Repo(LOCAL_TARGET_GIT_DIR)

        if not git_ref in repo.tags and not git_ref in repo.branches:
            shutil.rmtree(LOCAL_TARGET_GIT_DIR)
            clone_from_remote = True
    else:
        clone_from_remote = True

    if clone_from_remote:
        print(f'Loading elastic/integrations version "{git_ref}"')
        repo = git.Repo.clone_from(url, LOCAL_TARGET_GIT_DIR, branch=git_ref)

    repo.git.checkout(git_ref)
    return repo.head.commit.tree


@templated('input_doc.j2')
def inputs_doc(input_info):
    """
    Generate text for input documentation

    :param input_info: Information on the input
    :returns: Text of the input documentation
    """
    sorted_params = {}
    if input_info is not None:
        policy_templates = input_info.get('policy_templates')
        if policy_templates is not None:
            var_list =[]
            for template in policy_templates:
                var = template.get('vars')
                if var is not None:
                    var_list = var_list + template.get('vars')
                if len(var_list) > 0:
                    sorted_params = sorted(var_list, key=lambda v: v['name'])
    has_user_params = any([True if v.get('show_user') else False for v in sorted_params])
    has_hidden_user_params = any([True if v.get('show_user') == False else False for v in sorted_params])
    return {"inp": input_info,
            "sorted_params": sorted_params,
            "has_user_params": has_user_params,
            "has_hidden_user_params": has_hidden_user_params}

LOCAL_DIR = path.dirname(path.abspath(__file__))
TEMPLATE_DIR = path.join(LOCAL_DIR, './templates')
GENERATE_DIR = path.join(LOCAL_DIR, '../generated')
LOCAL_TARGET_GIT_DIR = path.join(LOCAL_DIR, "./build/integrations/")
INTEGRATIONS_GIT = "https://github.com/elastic/integrations.git"
INTEGRATIONS_VERSION = "main"

template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_DIR)
template_env = jinja2.Environment(loader=template_loader,
                                  keep_trailing_newline=True,
                                  trim_blocks=True,
                                  lstrip_blocks=False)

if __name__ == '__main__':
    get_tree_by_url(INTEGRATIONS_GIT, INTEGRATIONS_VERSION)
    inputs_dict = find_inputs(LOCAL_TARGET_GIT_DIR)
    generate_doc(inputs_dict)
