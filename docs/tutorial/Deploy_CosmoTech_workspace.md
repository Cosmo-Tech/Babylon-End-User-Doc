---
description: Tutorial for creating or update Cosmo Tech workspace
---

# Deploy Cosmo Tech workspace

!!! abstract "Remember"
    This guide focuses on explaining each object individually.  
    A complete deployment workflow is provided in the [Examples](../Examples/Example_Deploy_CosmoTech_workspace.md) section, where all components are combined in a practical scenario !

    Before proceeding, ensure that you have selected the correct `tenant`.

    In this example, we will use the following identifiers:

    - `context_id`: `test`  
    - `tenant_id`: `dev`  
    - `state_id`: `8db6069e`

To deploy a complete Cosmo Tech workspace, you can declare its configuration in yaml files corresponding
to specific deployment type. <br>

Each file contains general information about the deployment:

!!! abstract "Important"
    In this tutorial each **Cosmo Tech object**, values defined directly within the corresponding YAML file.  
    However, in the [Examples](../Examples/Example_Deploy_CosmoTech_workspace.md) section, you will see that we use a centralized `variables.yaml` file, which defines all required variables and is then referenced across the YAML configurations !

## :material-folder: API Organization

--8<-- 'docs/tutorial/API/Organization.md'

## :material-folder: API Solution

--8<-- 'docs/tutorial/API/Solution.md'

## :material-folder: API Workspace

--8<-- 'docs/tutorial/API/Workspace.md'

## :material-folder: API Dataset

--8<-- 'docs/tutorial/API/Dataset.md'

## :material-folder: API Runner

--8<-- 'docs/tutorial/API/Runner.md'

## :material-folder:  Cosmo Tech Web App

--8<-- 'docs/tutorial/API/Webapp.md'

## :material-file-tree: Babylon project structure 

Project folder must have the following structure:

!!! tip "Tree" 

    ```bash
    ├── variables.yaml
    ├── project
    │   ├── Organization.yaml
    │   ├── Solution.yaml
    │   ├── Workspace.yaml   
    │   ├── Runner.yaml
    │   ├── Dataset.yaml
    │   └── Workspace.yaml
    └── README.md
    ```


## :material-console: Launching the deployment Macro command

After filling all deployment files, you can launch the following command:

!!! example "Babylon Macro apply"

    ```bash
    babylon apply project/
    ```

Babylon will create and deploy all resources and save it in the state except for datasets and runner. <br>
Keeping this information in the
state simplifies modification of the resources as you can edit one of the project deployment files
and relaunch `babylon apply` command. It will update existing resources or create missing ones, for example,
in case when Babylon was granted more rights between two `apply` commands.


You can also specify different variable files when launching the `babylon apply` command. 

To do this, use the `--var-file` option.

!!! example 

    ```bash
    babylon apply project/ --var-file variable_file_1.yaml --var-file variable_file_2.yaml
    ```

!!! abstract "Remember"
    If you don't specify a variable file, Babylon will use the default variable file `variables.yaml`

## :material-console: Executing babylon apply on a Single Object API

Babylon now supports deploying or updating a **single object API** using the `apply` macro command.  
This enhancement makes it easier to **maintain** and **update only the specific object** that has changed, instead of running the macro for **all objects** following best practices for efficient deployments.

To support this, Babylon introduces two new options: `--include` `--execlude`

| Option | Description |
| :--- | :--- |
| `--include` | Specifies only the objects to be included in the action. |
| `--exclude` | Specifies the objects to be skipped during the action. |


!!! example "**include**"
    ```bash
    > babylon apply --include organization project
    ```
    ```bash
    🚀 Deploying Organization in namespace: sphinx
        → Loading configuration from Kubernetes secret...
        → No existing organization ID found. Creating...
        ✔ Organization o-nl8pgn5lpwd created

    📋 Deployment Summary
        • Organization Id : o-nl8pgn5lpwd

    ✨ Deployment process complete
    ```

!!! example "**exclude**"
    ```bash
    > babylon apply --exclude workspace project/
    ```
    ```bash
    🚀 Deploying Organization in namespace: sphinx
        → Loading configuration from Kubernetes secret...
        → No existing organization ID found. Creating...
        ✔ Organization o-nl8pgn5lpwd created

    🚀 Deploying Solution in namespace: sphinx
        → Loading configuration from Kubernetes secret...
        → No existing solution ID found. Creating...
        ✔ Solution sol-6069lgex2xz created

    📋 Deployment Summary
        • Organization Id : o-nl8pgn5lpwd
        • Solution Id     : sol-6069lgex2xz

    ✨ Deployment process complete
    ```
<!-- This will be visible after adding the Superset feature -->
<!-- ## :material-console: Executing babylon with `--payload-only` option 

The `--payload-only` option allows Babylon to deploy or update an object API without triggering the deployment of associated Azure services defined in the deployment file.<br>
This is particularly useful for incremental updates where you only need to modify lightweight parts, such as adding permissions in the Object ACL or updating the payload. Fully redeploying these parts can be time consuming.

However, this option should not be used when there are new superset reports, or other changes related to azure section, as those require a full deployment.

!!! tip "💡 Best practice for using `--payload-only` "
    Use this option only when you have changes limited to the payload itself, avoiding unnecessary redeployment of Azure section.
    
    ```bash
    > babylon apply --OBJECT --payload-only --var-file variable_file_1.yaml project/
    ```
    As objects now, Babylon accepts the following:

    ```bash
    --workspace          Deploy or update a workspace payload only.
    ``` -->