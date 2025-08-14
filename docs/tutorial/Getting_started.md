---
description: Tutorial for getting started with Babylon CLI
---

# Getting started with Babylon

This is a guide to getting started with Babylon. You'll learn how to install, run, and experiment with the Babylon.

--8<-- 'docs/guides/az_requirements.md'

--8<-- 'docs/partials/installation/from_source.md'

Now that you have a fully functional installation of Babylon, you can check the next steps to learn how to start running commands.

## Setup Babylon


Babylon use a [Vault](https://www.vaultproject.io/) service and provides a group of commands that can be used.

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
      uuidgen
      # Example output:
      0475231d-3c7c-4505-af38-558041240d3d
      ```

    - `platform_id` represents the **platform identifier** (e.g., `dev`, `staging`, ...).  
      ⚠️ It must be the **same `platform_id`** you used when initializing the Vault configuration.

    - Example Vault config command you can See 👉 [Usage](./Babylon_Vault_Init_Vars.md#usage) :
      ```bash
      python main.py config write --resource all --use-azure --engine v1 --platform-id dev
      ```

To initialize Babylon with these values, run:

```bash
babylon namespace use -c <context_id> -p <platform_id> -s <state_id>
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
The initial configuration is fetched from Vault and then persisted in two different backends to ensure consistency and recovery. This persisted configuration is referred to as the **Babylon state**.

!!! tip "Where *Babylon state* is stored"

    The state is saved in two places:

    1. **Remote backend (Azure Storage Blob)** → `babylon-states`  
    2. **Local backend (YAML file)** → `~/.config/cosmotech/babylon/state.<context_id>.<platform_id>.<state_id>.yaml`  
    
## State file specification

--8<-- 'docs/guides/resource_file.md'
