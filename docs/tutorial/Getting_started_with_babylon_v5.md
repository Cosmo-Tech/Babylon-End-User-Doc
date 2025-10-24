---
description: Tutorial for getting started with Babylon CLI v5
---

# Getting started with Babylon v5

This is a guide to getting started with Babylon v5. You'll learn how to install, run, and experiment Babylon commands.

--8<-- 'docs/partials/installation/from_source.md'

Now that you have a fully functional installation of Babylon, you can check the next steps to learn how to start running commands.

## Setup Babylon

Babylon use a [Vault](https://www.vaultproject.io/) service as its source of configuration and provides a group of commands that can be used.

The first thing to do in order to check if Babylon is working properly:
```bash
babylon --help
```

### Setup Environment Variables

The Vault service is required some environment variables before interacting with **Babylon CLI** To do so, 
Contact your Babylon admin to get **service URI** and **token**.  

!!! important
    You can retrieve those values directly from the cluster  
    See 👉 [Retrieve Vault URL and Token](./Babylon_Vault_Init_Vars.md#1-configure-environment-variables).

When you retrieve these values, you need to set the following environment variables

!!! example 
    ```bash
    export BABYLON_ORG_NAME="vault_org_name" # cosmotech
    export BABYLON_TOKEN="vault_root_token"  # hvs.CLxxxxxxxxxxxxxxx
    export BABYLON_SERVICE="vault_url"       # https://example.api.cosmotech.com
    ```
### Configuration

At this point, you need **three variables** to perform Babylon commands.

| Variable       | Description                                | Example   |
|----------------|--------------------------------------------|-----------|
| `context_id`   | Project name *(string of your choice, no special characters)* | `project1` |
| `platform_id`  | Platform ID *(e.g., dev, staging, prod)*   | `dev`     |
| `state_id`     | State name *(string of your choice, no special characters)* | `state1`  |

!!! important "⚠️ Variable Constraints"
    - `context_id` and `state_id` can be **any string** of your choice, but **they must not contain special characters**.  

    - If you are on **Linux**, you can generate a new UUID with [`uuidgen`](https://man7.org/linux/man-pages/man1/uuidgen.1.html):  
      ```bash
      sudo apt update
      sudo apt install uuid-runtime -y
      # run uuidgen command 
      uuidgen | cut -c1-8
      # Example output:
      0475231d-3c7c-4505-af38-558041240d3d
      ```

    - `platform_id` represents the **platform identifier** (e.g., `dev`, `staging`, ...).  
      ⚠️ It must be the **same `platform_id`** you used when initializing the Vault configuration.

To initialize Babylon with these values, run

```bash
babylon namespace use -c <context_id> -p <platform_id> -s <state_id>
```

!!! note "Generated Configuration"
    - This command creates a file called **namespace.yaml**
    - Location: **~/.config/cosmotech/babylon/namespace.yaml**
    - It contains the current context for your deployment

## What’s New in Babylon v5
### New namespace commands
Running the following command displays the updated namespace commands
!!! example 

    ```bash
    > babylon namespace --help
    Usage: babylon namespace [OPTIONS] COMMAND [ARGS]...

      Babylon namespace

    Options:
      --help  Show this message and exit.

    Commands:
      get-contexts  Display the currently active namespace
      get-states    Display all states in your local machine
      use           Switch to a specific namespace or create a new one

    ```
Using these commands, we can view the currently active namespace. <br>
Additionally, with `get-states`, we can list all states available on our local machine. Here are some examples

!!! example 

    ```bash
    > babylon namespace get-contexts  
    CURRENT  CONTEXT                            TENANT        STATE ID                              
    *        sphinx-dev  sphinx  1184d4e3-b9de-4c10-a8f0-db8101e4c1e0 

    # or use get-states

    > babylon namespace get-states 
    INFO   2025-10-23 22:27:31,230 |  state.dev.sphinx.c9b011db-93d9-42f2-a603-8766ffee5aee.yaml
    INFO   2025-10-23 22:27:31,232 |  state.prod.sphinx.d4ab0004-a10c-4b98-8fb0-f4176725e0db.yaml
    INFO   2025-10-23 22:27:31,233 |  state.staging.sphinx.9646a17d-4b87-445f-adee-980ac8fd912h.yaml
    ```
### Keycloak Authentication
!!! note "Keycloak Auth"
    - In v5, Babylon now uses Keycloak as the authentication system to authenticate with the API and execute commands to create a Cosmotech API object.
    - A new client, `cosmotech-babylon-client`, is created in Keycloak for this purpose.

### New babylon init commnad
After setting the context with the `use` command you can now easily initialize your project folder with the basic structure using the `babylon init` command.  
Here’s an example

!!! examples 

    ```bash
    > babylon init --help
    Usage: babylon init [OPTIONS]

    Create a Babylon project structure using YAML templates.

    Options:
    --project-folder TEXT  Name of the project folder to create (default:'project').
    --variables-file TEXT  Name of the variables file (default:'variables.yaml').
    --help  Show this message and exit.
    ```
    ```bash
     > babylon init
     INFO     2025-10-24 09:54:53,853 | 
            [babylon] Project successfully initialized at: ~/CosmoTech/DevOps/babylon_v5_dir/test-babylon/project
    ```
    ```bash
      .
      ├── babylon.error
      ├── babylon.log
      ├── project
      │   ├── Dataset.yaml
      │   ├── Organization.yaml
      │   ├── Runner.yaml
      │   ├── Solution.yaml
      │   └── Workspace.yaml
      └── variables.yaml
    ```
Now, you can get started with running Babylon commands.  
All the required YAML files for the resources you need to deploy in v5 are provided as templates.  
You can customize and modify them based on your specific needs.

### New group for handling runner and run objects
!!! important
    In v5, there is no longer a **Connector** object, and **Scenario** / **ScenarioRun** have been replaced by **Runner** and **Run**.

### Meta About Endpoint

Now, with Babylon, you can see which API version you are using with the following command

!!! example "about"

    ```bash
    babylon api about
    ```
    ```bash
    {
      "version": {
        "full": "5.0.0-beta5-7ebc87cb",
        "release": "5.0.0-beta5",
        "major": 5,
        "minor": 0,
        "patch": 0,
        "label": "beta5",
        "build": "7ebc87cb"
      }
    }
    ```
### Command for Testing

For more details on how to test, see 👉 [Examples](../Examples/Example_Deploy_CosmoTech_workspace_v5.md#deploy-cosmo-tech-workspace).

!!! example "Commands"

    ```bash
    babylon apply --organization project/  
    ```
    ```bash
    babylon apply --solution project/
    ```
    ```bash    
    babylon apply --workspace project/ 
    ```
    ```bash 
    babylon apply --runner project/
    ```
    !!! Note 
        You can use the `--var-file` option to specify a particular `variables.yaml` file.