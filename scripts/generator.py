from functools import wraps
import jinja2
import os
from os import path
from pathlib import Path
import yaml

def generate_doc(inputs):
    """
    Generate input docs

    :param inputs: dict of all inputs
    """
    # inputs.yaml contains extra info on inputs which isn't contained in the manifest.
    # Add this extra info to each input key before generating the docs
    extras = {}
    with open('inputs.yml', 'r') as extra_f:
        extras = yaml.safe_load(extra_f)
    for k in extras.get('inputs').keys():
        if k in inputs.keys():
            inputs[k]['long_desc'] = extras['inputs'][k]['long_desc']

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


@templated('input_doc.j2')
def inputs_doc(input_info):
    """
    Generate text for input documentation

    :param input_info: Information on the input
    :returns: Text of the input documentation
    """
    policy_templates = input_info.get('policy_templates')
    sorted_params = sorted(policy_templates[0].get('vars'), key=lambda v: v['name'])
    return dict(inp=input_info,
            sorted_params=sorted_params)

local_dir = path.dirname(path.abspath(__file__))
INTEGRATIONS_DIR = path.expanduser('~/git/integrations/')
TEMPLATE_DIR = path.join(local_dir, './templates')
GENERATE_DIR = path.join(local_dir, '../generated')
template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_DIR)
template_env = jinja2.Environment(loader=template_loader,
                                  keep_trailing_newline=True,
                                  trim_blocks=True,
                                  lstrip_blocks=False)

if __name__ == '__main__':
    inputs_dict = find_inputs(INTEGRATIONS_DIR)
    generate_doc(inputs_dict)
