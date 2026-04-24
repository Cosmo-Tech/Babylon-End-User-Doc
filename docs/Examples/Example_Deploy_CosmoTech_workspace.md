---
description: Example from scratch for deploying a Cosmo Tech workspace with best practice
---

# Deploy Cosmo Tech workspace 

Make sure your Python virtual environment is set up correctly see 👉 [Install](../tutorial/Getting_started.md#Getting started with Babylon).

After that, you need to create a test folder, for example:

```bash
mkdir test-babylon && cd test-babylon
```

##  Set Kubernetes Context

Check your current Kubernetes context and switch to the correct one:

!!! example
    ```bash
    > kubectl config current-context
    dev-aks
    ```
    ```bash
    > kubectl config use-context prod-aks
    Switched to context "prod-aks"
    ```
    ```bash
    > kubectl config current-context
    prod-aks
    ```
##  Set up Babylon Context
```bash
babylon namespace use -c test -t dev
```
## Initialization Babylon project

With Babylon v5, you can now generate a minimal manifest YAML file that can be used to test Babylon.

!!! example

    ```bash
    babylon init --project-folder devops --variables-file devops.yaml azure
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
    the `init` command creates a project folder with the following structure:
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
## Start Deployment

Now, we can start running the Babylon command to deploy the workspace.

Here is an example of `variables.yaml` with detailed explanations:

!!! example "variable.yam"

    ```yaml
    # =========================================================
    # IMPORTANT: You can add variables here as needed!
    # Make sure they are used in the manifest YAML.
    # =========================================================
    # Organization
    organization_name: to_fill    # Should be the name of the project like "project1 organization"

    # Workspace
    workspace_name: to_fill       # Should be the name of the project like "project1 workspace"
    workspace_key: to_fill        # Unique key to define according to your naming convention, for example: project1workspace1
    workspace_description: to_fill              # Quick sentence to explain the purpose of the workspace

    # Solution
    solution_name: to_fill                      # Should be the name of the project like "project1 solution"
    solution_key: to_fill                       # Unique key to define according to your naming convention, for example: project1solution1
    solution_description: to_fill                # Quick sentence to explain the purpose of the solution
    simulator_repository: to_fill               # To fill according to your simulator name
    simulator_version: to_fill                  # To fill according to your simulator version
    # Webapp
    cloud_provider: azure                       # Cloud provider to use (e.g., azure, aws, gcp)
    cluster_name: aks-dev-test                  # Name of the Kubernetes cluster
    cluster_domain: aks-dev-test.azure.platform.cosmotech.com  # Domain of the Kubernetes cluster
    tenant: dev                                 # namespace kubernetes (e.g., dev, prod)
    webapp_name: business                       # Name of the web application
    organization_id: o-xxxxxxxxxxx                         # Organization ID
    azure_subscription_id: xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxx # Azure subscription ID
    azure_entra_tenant_id: xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxx # Azure Entra (AAD) tenant ID
    powerbi_app_deploy: false                              # Set to true if deploying Power BI app, false otherwise

    # Enabled by default: stores deployment state in a Kubernetes secret.
    # Set to false for local testing.
    remote: true

    # Security
    # The list below will be used on all API objects.
    # If differents security list are needed for each API objects,
    # you can copy/paste this list, and edit {{security_<object>}}
    # in files organization.yaml, solution.yaml and workspace.yaml
    security:                                                                   
      default: none                                                            
        accessControlList:                                                        
        - id: admin.user@example.com    # Example of admin user
            role: admin                                                          
        - id: editor.user@example.com   # Example of editor user
            role: editor                                                         
        - id: viewer.user@example.com   # Example of viewer user
            role: viewer                                                         

    ```
Now you can launch the `apply` command to deploy the workspace:

!!! example

    ```bash
    source .venv/bin/activate
    ```
    ```bash
    babylon namespace use -c test -t dev
    ```
    ```bash
    babylon apply project/
    ```
Here are some simple commands you can use if needed:

!!! example

    ```bash
    babylon api solutions create --oid o-d2yrojeplmo project/Solution.yaml
    ```
    ```bash
    babylon api organizations delete --oid o-d2yrojeplmo
    ```
    ```bash
    babylon api runners delete --oid o-d2yrojeplmo --wid w-5zompvvrg0j --rid r-mdlq0mk0jo5
    ```

It is recommended to use `babylon --help` to get more details about the arguments of each command.

!!! example

    ```bash
    babylon api organizations delete --help
    ```
    ```bash
    Usage: babylon api organizations delete [OPTIONS] ORGANIZATION_ID

    Delete an organization by ID

    Options:
    -c, --context TEXT   Context Name without any special character
    -t, --tenant TEXT    Tenant Id without any special character
    -s, --state-id TEXT  State Id
    --oid TEXT           Organization ID  [required]
    --help               Show this message and exit.
    ```