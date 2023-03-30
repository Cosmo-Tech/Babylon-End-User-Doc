---
hide:
  - toc
---
# Configuration

Now that you have installed Babylon we can learn about how it works.  

## Initialization

In order to begin working on your project you need a fully initialized configuration and working directory. Use the following command to create necessary files.
???+ info "Help of the command"
    ```bash
        # Usage: babylon config init [OPTIONS]
        # Initialize Babylon configuration, working directory and secret key
        # Options:
        #  --help  Show this message and exit.
    ```

???+ example "First commands"
    --8<-- 'docs/partials/Configuration/FirstCommands.md'

Now that you ran a few working commands, let's try one that requires some configuration.

???+ example "Run command without configuration"
    ```bash
    babylon azure storage container get-all
    ```
    ![Run command without configuration gif](../assets/Command_without_configuration.gif)

Without configuration this command will fail and you should see an error message telling you why.

???+ example "Error message description"
    --8<-- 'docs/partials/Configuration/ErrorMessageDescription.md'

Now we know that we need to set up some configuration to use our commands.

## Different type of configuration files

Two main configuration files exist on Babylon: platform and deployment

### `Platform` configuration file

This file contains the variables necessary to connect to a Cosmo Tech platform deployed on a given cloud.

### `Deployment` configuration file

A Deployment is a single application made available on a platform.

Using terms of the Cosmo Tech API, a deployment is equivalent to a `Workspace`

## Set configuration values

3 main ways exist to work on configuration values.  
In the following part we will only work on `platform`, but those 3 ways are identical for `platform` and `deployment` 

=== "Use `set-variable` command"
    --8<-- 'docs/partials/Configuration/1-SetVariable.md'
=== "Use `edit` command"
    --8<-- 'docs/partials/Configuration/1-Edit.md'
=== "Use a file editor"
    --8<-- 'docs/partials/Configuration/1-UseEditor.md'

Now you know how to set a specific configuration variable.
