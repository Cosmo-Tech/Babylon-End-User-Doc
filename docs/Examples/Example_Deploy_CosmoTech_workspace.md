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

    > kubectl config use-context prod-aks
    Switched to context "prod-aks"

    > kubectl config current-context
    prod-aks
    ```
##  Set up Babylon Context
```bash
babylon namespace use -c test -t dev -s 73a90433
```
## Initialization Babylon project

With Babylon v5, you can now generate a minimal manifest YAML file that can be used to test Babylon.

!!! example
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
        ├── customers.csv
        └── variables.yaml
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
    organization_name: to_fill                                              # Should be the name of the project like "project1 organization"

    # Workspace
    workspace_name: to_fill                                                 # Should be the name of the project like "project1 workspace"
    workspace_key: to_fill                                                  # Unique key to define according to your naming convention, for example: project1workspace1
    workspace_description: to_fill                                          # Quick sentence to explain the purpose of the workspace

    # Solution
    solution_name: to_fill                                                  # Should be the name of the project like "project1 solution"
    solution_key: to_fill                                                   # Unique key to define according to your naming convention, for example: project1solution1
    solution_description: to_fill                                           # Quick sentence to explain the purpose of the solution
    simulator_repository: to_fill                                           # To fill according to your simulator name
    simulator_version: to_fill                                              # To fill according to your simulator version
    # Dataset 
    dataset_name: to_fill
    dataset_description: to_fill
    # Runner 
    run_template_id: to_fill
    runner_name: to_fill
    runTemplate_name: to_fill
    owner_name: to_fill
    # Security
    # The list below will be used on all API objects.
    # If differents security list are needed for each API objects,
    # you can copy/paste this list, and edit {{security_<object>}}
    # in files organization.yaml, solution.yaml and workspace.yaml
    security:                                                                   
      default: none                                                            
        accessControlList:                                                        
        - id: admin.user@example.com                                             # Example of admin user
            role: admin                                                          
        - id: editor.user@example.com                                            # Example of editor user
            role: editor                                                         
        - id: viewer.user@example.com                                            # Example of viewer user
            role: viewer                                                         

    ```

As a best practice, it is recommended to create a `.env` file at the same level as the `variable.yaml` file containing the deployment commands. This allows you to easily update the workspace in the future by reusing or modifying the commands without retyping them.

!!! tip "Tree" 

    ```bash
    ├── variables.yaml
    ├── .env         # <--- 
    ├── .gitignore   # add .env  babylon.*
    ├── project
    │   ├── organization.yaml
    │   ├── solution.yaml
    │   └── workspace.yaml
    └── README.md
    ```

!!! example

    ```bash
    source .venv/bin/activate
    ```
    ```bash
    babylon namespace use -c test -t dev -s 73a90433
    ```
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
    babylon apply --dataset project/
    ```
    ```bash 
    babylon apply --runner project/
    ```
Here are some simple commands you can use if needed:

!!! example

    ```bash
    babylon api solutions create o-d2yrojeplmo test-api/Solution.yaml
    ```
    ```bash
    babylon api organizations delete o-d2yrojeplmo
    ```
    ```bash
    babylon api workspaces security get-all
    ```
    ```bash
    babylon api runners delete o-d2yrojeplmo w-5zompvvrg0j r-mdlq0mk0jo5
    ```

It is recommended to use `babylon --help` to get more details about the arguments of each command.

!!! example

    ```bash
    > babylon api organizations delete --help

    Usage: babylon api organizations delete [OPTIONS] ORGANIZATION_ID

    Delete a specific organization

    Args:

        ORGANIZATION_ID: The unique identifier of the organization

    Options:
    -c, --context TEXT   Context Name without any special character
    -t, --tenant TEXT    Tenant Id without any special character
    -s, --state-id TEXT  State Id
    -D                   Force Delete
    --help               Show this message and exit.
    ```