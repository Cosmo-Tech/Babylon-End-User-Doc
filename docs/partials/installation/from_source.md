### ** Get Babylon from source **

!!! warning "Requirements"
    --8<-- 'docs/partials/installation/prerequisites.md'

We will go through the process of getting a version of Babylon before the installation.

--8<-- 'docs/partials/installation/from_git.md'

## Install Babylon

You can install babylon globally in your system

```bash
pip install .
```

but, if you want you can set up a virtual environment in python using the library `pvenv` to keep your Babylon dependencies in a single location. See the guide below:


--8<-- 'docs/partials/installation/pyenv_setup.md'

* Install Babylon in your environment `<babylon_env_name>`
```bash
pyenv activate <babylon_env_name>
pip install .
```

??? tip "Enable autocompletion"
    On some systems autocompletion can be enabled for Babylon, more information on autocompletion can be found on the [click documentation](https://click.palletsprojects.com/en/8.1.x/shell-completion/) (since Babylon is based on `click`)
    === "Example of click autocompletion command for `bash`"
    ```bash
    echo 'eval "$(_BABYLON_COMPLETE=bash_source babylon)"' >> ~/.bashrc
    source ~/.bashrc
    ```