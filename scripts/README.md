### How it works

`generator.py` takes content from a few places; `inputs.yml` and the integration repo's manifest files.


#### inputs.yml

`inputs.yml` contains extra documentation for the inputs, which can't be extracted automatically from the manifest documentation. This text is added and maintained manually.

To use this, add text into the `input` key name, in a section that will be inserted into the template.

Currently, these sections are supported:

`title` -- Human-readable title for the input
`long_desc` -- A longer description of the input, which will be displayed at the top.
`setup_text` -- Text describing how to set up the integration.

#### Integrations repo

The first time the generator is run, it will clone the integrations repo. This seems to be very slow. After that, the generator script will use the manifest files from the `main` commit in this directory. It'll need to be manually pulled if you need to get the latest changes.

### Generated inputs

Since inputs come from various places, and there are some we don't want to generate docs for, the list of inputs to generate is hardcoded in `generator.py`. That list needs to be updated to change the input docs to generate.

# TODO

* All file generation is done with the templates in `scripts/templates` and `inputs.yml`. There will need to be a way to generate and include content in the root of the repo (or change the structure to only have one source of content).
* The generator only takes params from the integration manifests, so inputs from beats have almost no content generated.
* The integrations repo is not updated after cloning, there will need to be a process to get the latest changes.
