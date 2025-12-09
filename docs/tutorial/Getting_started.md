---
description: Tutorial for getting started with Babylon CLI
---

# Getting started with Babylon

This is a guide to getting started with Babylon v5. You'll learn how to install, run, and experiment with Babylon.

--8<-- 'docs/partials/installation/from_source.md'

Now that you have a fully functional installation of Babylon, you can check the next steps to learn how to start running commands.

## Setup Babylon

!!! important "⚠️ Vault is replaced with Kubernetes secrets"

    Babylon now uses Kubernetes secrets as the source of configuration required for it to operate

    The first thing to do to verify that Babylon is working properly run:

    ```bash
    babylon --help
    ```
### Set Kubernetes Context
 
Some configuration variables must be set before interacting with the **Babylon CLI**.

Currently, there are two options:  
1. Babylon can load configuration directly from a Kubernetes secret.  
2. You can manually export the required values as environment variables.

!!! note "Error example"
    ```bash
    > babylon api about 
    INFO     2025-12-09 10:54:04,281:INFO:Babylon.utils.environment:Loading configuration from Kubernetes secret
    ERROR    2025-12-09 10:54:04,565:ERROR:Babylon.utils.environment:
            Failed to read Kubernetes secret 'keycloak-babylon' in namespace 'dev'
            Please ensure your kubeconfig is valid and your context is correctly set
            You can switch context using: 'kubectl config use-context <context-name>'
    ```

To fix this, check your current Kubernetes context and switch to the correct one:

!!! example
    ```bash
    > kubectl config current-context
    dev-aks

    > kubectl config use-context prod-aks
    Switched to context "prod-aks"

    > kubectl config current-context
    prod-aks
    ```

Now you can run the command again, and it should work:
!!! example
    ```bash
    > babylon api about
    INFO     2025-12-09 11:03:29,426:INFO:Babylon.utils.environment:Loading configuration from Kubernetes secret

    Get the version of the API service

    INFO     2025-12-09 11:03:30,115:INFO:Babylon.commands.api.meta.about:API version:{'full': '5.0.0-1639f21d', 'release': '5.0.0', 'major': 5, 'minor': 0, 'patch': 0, 'label': 'rc2', 'build': '1639f21d'}
    ```

Alternatively, if you need CI/CD workflows or want to run quick local tests without loading the Kubernetes secret, you can export the required variables directly in your terminal.

!!! example
    ```bash
    API_URL=https://dev.api.cosmotech.com/dev/v5   
    CLIENT_ID=cosmotech-babylon-client  
    CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxx 
    TOKEN_URL=https://dev.api.cosmotech.com/keycloak/realms/dev/protocol/openid-connect/token 
    ```

You can retrieve these values using `kubectl`, or you can contact your Babylon administrator to obtain them.


!!! note "Important"
    For **configuration**, you can retrieve the values from the cluster using one of the following methods:

    === "🖥️ Using k9s"
        Open `k9s`, navigate to the relevant **namespace**, and retrieve the secret named `keycloak-babylon` which contains the configuration.

    === "🧩 Using kubectl"
        ```bash
        # List all secrets in the target namespace
        kubectl -n dev get secrets

        # Look for the 'keycloak-babylon' secret and view its YAML content
        kubectl -n dev get secret keycloak-babylon -o json | jq -r '.data | to_entries[] | "\(.key)=\(.value | @base64d)"'
        ```

### Configuration

At this point, you need **three variables** to perform Babylon commands.

| Variable       | Description                                | Example   |
|----------------|--------------------------------------------|-----------|
| `context_id`   | Project name *(string of your choice, no special characters)* | `project1` |
| `tenant_id`    | Tenant ID *(e.g., dev, staging, prod)*                        | `dev`     |
| `state_id`     | State name *(string of your choice, no special characters)*   | `state1`  |

!!! important "⚠️ Variable Constraints"
    - `context_id` and `state_id` can be **any string** of your choice, but **they must not contain special characters**.  
    - For state_id, you can generate a new UUID with [`uuidgen`](https://man7.org/linux/man-pages/man1/uuidgen.1.html):  
    === "Linux"
    ```bash
    sudo apt update
    sudo apt install uuid-runtime -y
    # Generate a UUID
    uuidgen | cut -c1-8
    # Example output:
    0475231d
    ```
    === "Windows"
    ```powershell
    # Open PowerShell and run:
    [guid]::NewGuid().ToString().Substring(0,8)
    # Example output:
    0475231d
    ```

    - `tenant_id` represents the **namespace kubernetes** (e.g., `dev`, `staging`, ...).  


To initialize Babylon namespace with these values, run:

```bash
babylon namespace use -c <context_id> -t <tenant_id> -s <state_id>
```

!!! note "Generated Configuration"
    - This command creates a file called **namespace.yaml**
    - Location: **~/.config/cosmotech/babylon/namespace.yaml**
    - It contains the current context for your deployment

You can now test Babylon by running a simple command:
  ```bash
  babylon api organizations get-all
  ```
If you have already created an organization, you should see its details in the output.

!!! example "Example List Organizations"
    ```bash
    > babylon api organizations get-all
    ```
    ```json
    [
      {
        "id": "o-55dsz6e51n8y8j",
        "name": "Organization name",
        "ownerId": "e0035649-0f12-4221-9631-3519704816c1",
        "services": null,
        "security": {
          "default": "none",
          "accessControlList": [
            {
              "id": "example.test@cosmotech.com",
              "role": "admin"
            }
          ]
        }
      }
    ]
    ```

In Babylon v5, the **state** is now independent of the configuration.  
The initial configuration is fetched from Kubernetes secrets, and the state is generated during deployment. It is then persisted in two different backends to ensure consistency and recovery.  

This persisted state is referred to as the **Babylon state**.

!!! tip "Where the *Babylon state* is stored"

    The state is saved in two locations:

    1. **Remote backend (cloud)** → `babylon-states`  (❗not available in this release, will be implemented in a future release)
    2. **Local backend (YAML file)** → `~/.config/babylon/state.<context_id>.<tenant_id>.<state_id>.yaml`

!!! note
    In this release, the state is stored **only locally**.  
    Remote state persistence will be implemented in a future release.
    
## State file specification

--8<-- 'docs/guides/resource_file.md'


## What’s New in Babylon v5
### New namespace commands
Running the following command displays the updated namespace commands:
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
Using these commands, you can check the currently active namespace. <br>
Additionally, with `get-states`, you can list all states available on our local machine. Here are some examples:

!!! example 

    ```bash
    > babylon namespace get-contexts  
    CURRENT  CONTEXT                            TENANT        STATE ID                              
    *        project1                           dev           1184d4e3 

    # or use get-states

    > babylon namespace get-states 
    INFO   2025-10-23 22:27:31,230 |  state.project1.dev.c9b011db.yaml
    INFO   2025-10-23 22:27:31,232 |  state.project2.prod.d4ab0004.yaml
    INFO   2025-10-23 22:27:31,233 |  state.project3.staging.9646a17d.yaml
    ```
### Keycloak Authentication
!!! note "Keycloak Auth"
    - Starting with vesion 5, Babylon uses Keycloak as the authentication system to authenticate with the Cosmotech API and execute commands to create objects.
    - A new client, `cosmotech-babylon-client`, is created in Keycloak for this purpose.

### New babylon init commnad
After setting the context with the `namespace use` command you can now easily initialize your project with a basic structure using the `babylon init` command.  
Here’s an example:

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
    For more information refer to the Cosmo Tech platform release notes.

### Meta About Endpoint

You can now see which API version you are using with the following command:

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
### Commands for Testing

For more details on how to test, see 👉 [Examples](../Examples/Example_Deploy_CosmoTech_workspace.md#deploy-cosmo-tech-workspace).

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

There is no support for a `babylon apply --dataset` command but datasets can be
created with the `babylon api datasets create` command.