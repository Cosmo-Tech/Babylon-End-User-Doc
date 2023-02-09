## Get Babylon sources

???+ warning "Requirements"
    --8<-- 'docs/partials/Installation/InstallPrerequisites.md'

We will go through the process of getting a version of Babylon before the installation.

You can make your choice on how you may want to process:

=== "Get official releases"
    --8<-- 'docs/partials/Installation/GetOfficialRelease.md'

=== "Use latest version from git"
    --8<-- 'docs/partials/Installation/GetLatestFromGit.md'

## Install Babylon

Now that you have a "Babylon Installation Folder" ready we can move to the installation process

??? "Use a `venv`"
    --8<-- 'docs/partials/Installation/VenvSetup.md'

The setup is fairly direct, the following command will allow a full install of Babylon

!!! Example "Setup Babylon"
    ```bash
    pip install <Babylon Installation Folder>
    ```

??? tip "Enable autocompletion"
    On some systems autocompletion can be enabled for Babylon, more information on autocompletion can be found on the [click documentation](https://click.palletsprojects.com/en/8.1.x/shell-completion/) (since Babylon is based on `click`)
    === "Example of click autocompletion command for `bash`"
    ```bash
    echo 'eval "$(_BABYLON_COMPLETE=bash_source babylon)"' >> ~/.bashrc
    source ~/.bashrc
    ```