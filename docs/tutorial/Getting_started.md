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
    babylon api about
    ```
    ```bash
    → Loading configuration from Kubernetes secret...

    ✘ Resource Not Found
    Secret keycloak-babylon could not be found in namespace dev

    💡 Troubleshooting:
    • Please ensure your kubeconfig is valid
    • Check that your context is correctly set kubectl config current-context
    • You can set context using kubectl config use-context <context-name>
    ```

To fix this, check your current Kubernetes context and switch to the correct one:

!!! example

    ```bash
    kubectl config current-context
    dev-aks
    ```
    ```bash
    kubectl config use-context prod-aks
    Switched to context "prod-aks"
    ```
    ```bash
    kubectl config current-context
    prod-aks
    ```

Now you can run the command again, and it should work:
!!! example

    ```bash
    babylon api about
    ```
    ```bash
    → Loading configuration from Kubernetes secret...
    → Sending request to API...
    ✔ API About Information: version=AboutInfoVersion(full='5.0.0-rc6-46f7c633', release='5.0.0-rc6', major=5, minor=0, patch=0, label='rc6', build='46f7c633')
    ```

Alternatively, if you need CI/CD workflows or want to run quick local tests without loading the Kubernetes secret, you can export the required variables directly in your terminal.

!!! example

    ```bash
    API_URL=https://dev.api.cosmotech.com/dev/v5   
    CLIENT_ID=cosmotech-babylon-client  
    CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxx 
    TOKEN_URL=https://dev.api.cosmotech.com/keycloak/realms/dev/protocol/openid-connect/token 
    ```

You can retrieve these values using `kubectl`, or you can contact your Babylon administrator to obtain them.<br>
Note: Make sure you have at least Contributor role assigned in Kubernetes.


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
If you no longer have access to the cluster, you can export these variables manually

| Variable         | Description                     | Example                                   |
|------------------|---------------------------------|-------------------------------------------|
| `API_URL   `     | API URL                         | `https://dev.api.cosmotech.com/tenant/v5` |
| `CLIENT_ID`      | Fixed Babylon client ID         | `cosmotech-babylon-client`                |
| `CLIENT_SECRET`  | Ask Babylon admin               | `xxxxxxxxxxx`                             |
| `TOKEN_URL`      | Auth endpoint                   | `https://dev.api.cosmotech.com/keycloak/realms/tenant/protocol/openid-connect/token`|

!!! example
    === "🖥️ Windows"
        ```bash
        $env:API_URL="https://dev.api.cosmotech.com/tenant/v5" 
        $env:CLIENT_ID="cosmotech-babylon-client" 
        $env:CLIENT_SECRET="your_secret_here" 
        $env:TOKEN_URL="https://dev.api.cosmotech.com/keycloak/realms/tenant/protocol/openid-connect/token"
        ```
    === "🐧 Linux" 
        ```bash
        export API_URL="https://dev.api.cosmotech.com/tenant/v5" 
        export CLIENT_ID="cosmotech-babylon-client" 
        export CLIENT_SECRET="your_secret_here" 
        export TOKEN_URL="https://dev.api.cosmotech.com/keycloak/realms/tenant/protocol/openid-connect/token
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
    === "🐧 Linux"
        ```bash
        sudo apt update
        sudo apt install uuid-runtime -y
        # Generate a UUID
        uuidgen | cut -c1-8
        # Example output:
        0475231d
        ```
    === "🖥️ Windows"
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
  babylon api organizations list
  ```
If you have already created an organization, you should see its details in the output.

!!! example "Example List Organizations"
    ```bash
    babylon api organizations list
    ```
    ```bash
    → Loading configuration from Kubernetes secret...
    → Sending request to API...
    ✔ 93 organization(s) retrieved successfully
    ```

In Babylon v5, the **state** is now independent of the configuration.  
The initial configuration is fetched from Kubernetes secrets, and the state is generated during deployment. It is then persisted in two different backends to ensure consistency and recovery.  

This persisted state is referred to as the **Babylon state**.

!!! tip "Where the *Babylon state* is stored"

    The state is saved in two locations:

    1. **Remote backend (cloud)** → storage account `cosmotechstates` → containers `babylon-states`
    2. **Local backend (YAML file)** → `~/.config/babylon/state.<context_id>.<tenant_id>.<state_id>.yaml`

## State file specification

--8<-- 'docs/guides/resource_file.md'


## What’s New in Babylon v5
### New namespace commands
Running the following command displays the updated namespace commands:
!!! example 

    ```bash
    babylon namespace --help
    ```
    ```bash
    Usage: babylon namespace [OPTIONS] COMMAND [ARGS]...

      Babylon namespace

    Options:
      --help  Show this message and exit.

    Commands:
      get-contexts  Display the currently active namespace
      get-states    Display states from local machine or remote storage.
      use           Switch to a specific namespace or create a new one

    ```
Using these commands, you can check the currently active namespace. <br>
Additionally, with `get-states`, you can list all states available on our local machine. Here are some examples:

!!! example 

    ```bash
    babylon namespace get-contexts
    ```
    ```bash
    CURRENT  CONTEXT                            TENANT        STATE ID                              
    *        project1                           dev           1184d4e3 
    ```

#### Viewing State Files

You can easily view and manage all available state files, whether they are stored locally or in the cloud. This is particularly useful when you need to select a specific state to update or redeploy your workspace.

The `babylon namespace get-states` command provides two options:

- `remote`: Lists all state files stored in the remote (cloud).
- `local`: Lists all state files available on your local machine.

!!! example 

    ```bash
    babylon namespace get-states remote
    ```
    ```bash
    ☁️  Remote States
    • state.project1.dev.d4ab0004.yaml
    • state.project2.prod.d4ab0005.yaml
    • state.project3.staging.d4ab0006.yaml
    ```
    ```bash
    babylon namespace get-states local
    ```
    ```bash
    📂  Local States
    • state.project1.dev.d4ab0004.yaml
    • state.project2.prod.d4ab0005.yaml
    • state.project3.staging.d4ab0006.yaml
    ```

### Keycloak Authentication
!!! note "Keycloak Auth"
    - Starting with version 5, Babylon uses Keycloak as the authentication system to authenticate with the Cosmotech API and execute commands to create objects.
    - A new client, `cosmotech-babylon-client`, is created in Keycloak for this purpose.

### New babylon init command
After setting the context with the `namespace use` command you can now easily initialize your project with a basic structure using the `babylon init` command.  
Here’s an example:

!!! example

    ```bash
    babylon init --help
    ```
    ```bash
    Usage: babylon init [OPTIONS]

    Create a Babylon project structure using YAML templates.

    Options:
    --project-folder TEXT  Name of the project folder to create (default:'project').
    --variables-file TEXT  Name of the variables file (default:'variables.yaml').
    --help  Show this message and exit.
    ```
    ```bash
    babylon init
    ```
    ```bash
    babylon init --project-folder devops --variables-file devops.yaml 
    ```
    ```bash
       → Cloning Terraform WebApp module...
       ✔ Terraform WebApp module cloned
       → Created directory: /home/user/CosmoTech/DevOps/babylon_v5_dir/devops
       ✔ Generated Organization.yaml
       ✔ Generated Solution.yaml
       ✔ Generated Workspace.yaml
       ✔ Generated Webapp.yaml
       ✔ Generated postgres/jobs/k8s_job.yaml
       ✔ Generated devops.yaml
    🚀 Project successfully initialized!
       Path: /home/user/CosmoTech/DevOps/babylon_v5_dir/devops

    Next steps:
       1. Edit your variables in devops.yaml
       2. Run your first deployment command
    ```
    for structure of the generated project, you should see something like this:

    ```bash
    .
    ├── babylon.log
    ├── devops
    │   ├── Organization.yaml
    │   ├── postgres
    │   │   └── jobs
    │   │       └── k8s_job.yaml
    │   ├── Solution.yaml
    │   ├── Webapp.yaml
    │   └── Workspace.yaml
    ├── terraform-webapp
    └── devops.yaml
    ```
Now, you can get started with running Babylon commands.
All the required YAML files for the resources you need to deploy in v5 are provided as templates.
You can customize and modify them based on your specific needs.

### New group for handling runner and run objects
!!! important
    There is no longer a **Connector** object, and **Scenario** / **ScenarioRun** have been replaced by **Runner** and **Run**.
    For more information refer to the Cosmo Tech platform release notes.

### Meta About Endpoint

You can now see which API version you are using with the following command:

!!! example "about"

    ```bash
    babylon api about
    ```
    ```bash
    → Loading configuration from Kubernetes secret...
    → Sending request to API..
    ✔ API About Information: version=AboutInfoVersion(full='5.0.0-rc5-897806da', release='5.0.0-rc5', major=5, minor=0, patch=0, label='rc5', build='897806da')
    ```

### Output Management

You can now handle the output of every single command. This is particularly useful for scripting, filtering data, or integration with other tools.

You can control the output using two main flags:

| Flag | Description | Supported Formats |
| :--- | :--- | :--- |
| `-o` | Displays the result in the terminal. | `json`, `yaml`, `wide` |
| `-f` | Saves the result directly to a file. | `json`, `yaml` |

Usage Examples:

!!! example "Commands"

    ```bash
    babylon api organizations list -o wide
    ```
    ```bash
    → Loading configuration from Kubernetes secret...
    → Sending request to API...
    ✔ 94 organization(s) retrieved successfully
    ID                NAME                                         CREATED         
    o-zjrw54r8kxp     Debugging organization                       2025-12-10 11:21
    o-x5oo38rjywq     Debugging organization                       2025-12-03 16:21
    o-e2o50oxk7oe     Debugging organization                       2025-12-23 09:40
    o-vd0wk30pdxx     Debugging organization                       2025-12-10 10:52
    ```
    ```bash
    babylon api organizations list -o json
    ```
    ```bash
    babylon api organizations list -o yaml
    ```
    ```bash
    babylon api organizations list -f organizations.json
    ```
    ```bash
    babylon api organizations list -f organizations.yaml
    ```
### Webapp Deployment

!!! Webapp_deployment
    We have introduced a new macro command to handle the deployment of webapps, based on terraform modules [`terraform-webapp`](https://github.com/Cosmo-Tech/terraform-webapp). This command simplifies the deployment process by automating the creation of necessary resources and configurations for web applications in specific Kubernetes clusters.

### PostgreSQL Schema Creation
!!! Workspace_improvements
    The workspaces macro command has been significantly enhanced, especially for creating PostgreSQL schemas. These improvements streamline the setup and management of database schemas within your workspaces, making it faster and easier to define, deploy, and maintain the necessary database structures.

### Commands for Testing

For more details on how to test, see 👉 [Examples](../Examples/Example_Deploy_CosmoTech_workspace.md#deploy-cosmo-tech-workspace).

!!! example "Commands"

    ```bash
    babylon apply project/  
    ```
    ```bash
    🚀 Deploying Organization in namespace: dev
      → Loading configuration from Kubernetes secret...
      → No existing organization ID found. Creating...
      ✔ Organization o-xxxxxxxxx created

    🚀 Deploying Solution in namespace: dev
      → Loading configuration from Kubernetes secret...
      → No existing solution ID found. Creating...
      ✔ Solution sol-xxxxxxxxx created

    🚀 Deploying Workspace in namespace: dev
      → Loading configuration from Kubernetes secret...
      → No existing workspace ID found. Creating...
      ✔ Workspace w-xxxxxxxxx created
      → Found PostgreSQL service postgresql
      → Initializing PostgreSQL schema for workspace w-xxxxxxxxx...
      → Waiting for job postgresql-init-w-xxxxxxxxx to complete...
      → Checking job logs for errors...
      ✔ Schema creation w_xxxxxxxxx completed successfully

    🚀 Deploying webapp in namespace: dev
      → Running Terraform deployment...
      backend.tf
      Initializing the backend...

      Successfully configured the backend "azurerm"! Terraform will automatically
      use this backend unless the backend configuration changes.

      Apply complete! Resources: 5 added, 0 changed, 0 destroyed.
      ✔ WebApp business deployed

    📋 Deployment Summary
      • Organization Id : o-xxxxxxxxx
      • Solution Id     : sol-xxxxxxxxx
      • Workspace Id    : w-xxxxxxxxx
      • Webapp Name     : webapp-business
      • Webapp Url      : https://dev.azure.platform.cosmotech.com/dev/webapp-business

    ✨ Deployment process complete
    ```

    !!! note "Using --var-file" 
        You can use the `--var-file` option to specify a particular `variables.yaml` file.
        ```bash
        e.g. → babylon apply --var-file devops-test.yaml devops-test/
        ```

The **macro command** currently only covers **Organization**, **Solution**, and **Workspace** levels. For other resources like **Runners**, **Datasets**, etc., you must use the **single commands** directly to interact with the API.

!!! example "Commands"

    ```bash 
    babylon api runners create --oid o-xxxxxxxxxx --sid sol-d-xxxxxxxxx --wid w-xxxxxxxxxxx project/runner.yaml
    ```
    ```bash 
    babylon api datasets create --oid o-xxxxxxxxxx --wid w-xxxxxxxxxxx project/dataset.yaml
    ```
    ```bash 
    babylon api runs list --oid o-xxxxxxxxxx --wid w-xxxxxxxxxxx --rid r-xxxxxxxxxxx
    ```
    ```bash 
    babylon api datasets create-part --oid o-xxxxxxxxxx --wid w-xxxxxxxxxxx --did d-r-xxxxxxxxxx project/dataset_part.yaml
    ```