from functools import wraps
import os
from os import path
import git
import jinja2
import shutil
import yaml

def generate_doc(inputs):
    """
    Generate input docs

    :param inputs: dict of all inputs
    """
    # inputs.yaml contains extra info on inputs which isn't contained in the manifest.
    # Add this extra info to each input key before generating the docs
    extras = {}
    with open(path.join(LOCAL_DIR, 'inputs.yml'), 'r') as extra_f:
        extras = yaml.safe_load(extra_f)
    for k in extras.get('inputs').keys():
        if k in inputs.keys():
            for item in ['long_desc', 'setup_text']:
                value = extras['inputs'][k].get(item)
                if value is not None:
                    inputs[k][item] = extras['inputs'][k][item]

    for k,v in inputs.items():
        write(path.join(GENERATE_DIR, f'{k}.md'), inputs_doc(v))

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
            if manifest.get('type') == 'input':
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
    policy_templates = input_info.get('policy_templates')
    sorted_params = sorted(policy_templates[0].get('vars'), key=lambda v: v['name'])
    return {"inp": input_info, "sorted_params": sorted_params}

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
