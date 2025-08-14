---
description: Example from scratch for deploying a Cosmo Tech workspace with best practice
---

# Deploy Cosmo Tech workspace 

!!! abstract "Remember"
    For deploying the workspace with Babylon, the project team should provide you with a delivery package containing all necessary files, including:  

    - Manifest YAML files for deployment  
    - ADX scripts  
    - Power BI reports (for the solution)  
    - Another delivery package for the web app, if needed  

!!! example
    - **Workspace:** [https://github.com/Cosmo-Tech/delivery-project/tree/0.1.0](https://github.com/Cosmo-Tech/babylon-project-templates.git) (project/ folder)  
    - **Webapp:** [https://github.com/Cosmo-Tech/webapp-project/tree/0.1.0](https://github.com/Cosmo-Tech/azure-sample-webapp.git)


## :material-github: Preparation github repositors

we need to [Create two GitHub repositories](https://github.com/new): one for the web app and another for the workspace. for best practice we can follow those naming format

   - workspace repository : cluster_name-namespace_name-workspaces
   - web app repository : cluster_name-namespace_name-webapps

## :material-source-repository: Configuring GitHub Repositories

We start with the **Web App** repository by following these commands

!!! example "Commands to configure your web app branch"

    ```bash
    git clone git@github.com:Cosmo-Tech/cluster_name-namespace_name-webapps.git
    ```
    ```bash
    cd cluster_name-namespace_name-webapps
    ```
    ```bash
    git init
    ```
    ```bash
    echo "# empty_webapp" >> README.md
    ```
    ```bash
    git add README.md
    ```
    ```bash
    git commit -m "first commit"
    ```
    ```bash
    git remote add upstream git@github.com:Cosmo-Tech/azure-sample-webapp.git
    ```
    ```bash
    git remote set-url upstream --push "NO"
    ```
    ```bash
    git fetch --all --tags --prune
    ```
    ```bash
    git checkout -B <BRANCH> <SOURCE_TAG> # e.g main 0.1.0
    ```
    ```bash
    rm -rf .github/ .git-hooks .git/
    ```
    ```bash
    rm -r config.json   # ⚠️ Remove if exists
    ```
    ```bash
    git init
    ```
    ```bash
    git config --global init.defaultBranch main
    ```
    ```bash
    git branch -m <BRANCH>   # e.g main 
    ```
    ```bash
    git remote add origin git@github.com:<YOUR_GITHUB_REPOSITORY>.git
    ```
    ```bash
    git add .
    ```
    ```bash
    git commit -m "Deploy web app"
    ```
    ```bash
    git push origin <BRANCH> -f # e.g main 
    ```
Your web app GitHub repository is now initialized and contains the source code.

Next, switch context to the Workspace repository and replicate the process by executing the following commands:

!!! example "Commands to configure your workspace branch"
 
    ```bash
    git clone --branch 0.1.0 --single-branch git@github.com:Cosmo-Tech/delivery-project.git
    ```
    ```bash
    mv delivery-project cluster_name-namespace_name-workspaces
    ```
    ```bash
    cd cluster_name-namespace_name-workspaces
    ```
    ```bash
    echo rm -rf .git/ .github/ 
    ```
    ```bash
    git init
    ```
    ```bash
    git commit -m "first commit"
    ```
    ```bash
    git remote add origin git@github.com:Cosmo-Tech/cluster_name-namespace_name-workspaces.git
    ```
    ```bash
    git add .
    ```
    ```bash
    git commit -m "deploy workspace"
    ```
    ```bash
    git push origin <BRANCH> -f  # e.g main 
    ```
!!! abstract "Note"
 
    Before starting the deployment, check that all values in the manifest files (all `.yaml` files in your workspace repository) are correct. 

    If anything is wrong, update them using the details from the customer’s DevOps ticket.  

Project folder must have the following structure:

!!! tip "Tree" 

    ```bash
    ├── variables.yaml
    ├── project
    │   ├── adx
    │   │   └── scripts
    │   │       └── Create.kql
    │   ├── connector_azure_storage.yaml
    │   ├── organization.yaml
    │   ├── powerbi
    │   │   ├── report1.pbix
    │   │   ├── report2.pbix
    │   │   └── report3.pbix
    │   ├── solution.yaml
    │   ├── webapp.yaml
    │   └── workspace.yaml
    └── README.md
    ```
## :material-alert: Push Simulator Image to ACR Target

In this step, you will push the simulator container image (as specified in the DevOps ticket) to the designated container registry.

!!! example "Pull and Push Simulator Image"

    ```bash
    az acr login -n <source_acr_service_name>.azurecr.io*
    ```
    ```bash
    docker pull <source_acr_service_name>.azurecr.io/<image_name>:<image_version>
    ```
    ```bash
    docker tag <source_acr_service_name>.azurecr.io/<image_name>:<image_version> <destination_acr_service_name>.azurecr.io/<image_name>:<image_version>
    ```
    ```bash
    az acr login -n <destination_acr_service_name>.azurecr.io
    ```
    ```bash
    docker push <destination_acr_service_name>.azurecr.io/<image_name>:<image_version>
    ```

## :material-cloud-upload: Start Deployment

Now, we can start running the Babylon command to deploy the workspace.

!!! abstract "Remember"
    Don't forget to generate a new **UUID** before running this command and update `variables.yaml` → `state_id`.  
    Also, fill up all variables with values depending on your project!

Here is an example of `variables.yaml` with detailed explanations:

!!! example "variable.yam"

    ```yaml
    state_id: to_fill                                                      # UUID to generate with command: uuidgen
    context_id: to_fill                                                    # Should be the name of your project
    platform_id: to_fill                                                   # Kubernetes namespace (will be used for Vault)
    platform:
        id: to_fill                                                         # Kubernetes namespace (same value as ns_platform_id)
        url: https://<api_domain>/<namespace_name>/<api_version>            # Example: https://cluster.api.example.com/namespace1/v3
    location: francecentral                                                 # Edit according to your location

    # Organization
    organization_name: to_fill                                              # Should be the name of the project like "project1 organization"

    # Workspace
    workspace_name: to_fill                                                 # Should be the name of the project like "project1 workspace"
    workspace_key: to_fill                                                  # Unique key to define according to your naming convention, for example: project1workspace1
    workspace_description: to_fill                                          # Quick sentence to explain the purpose of the workspace

    # PowerBI
    powerbi_workspace_name: to_fill                                         # Should be the same value as workspace_name
    powerbi_group_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx                  # Manually create a PowerBi group on Azure EntraID and copy/paste its Object ID here
    powerbi_permissions:
    - identifier: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx                      # UUID of the Static WebApp App registration allowed to display PowerBi dashboards from the PowerBi workspace
        description: to_fill                                                # Name of the Static WebApp App registration allowed to display PowerBi dashboards from the PowerBi workspace
        rights: Admin                                                       # Level of permission for the group
        type: App                                                           # Type of static app registration is "App"
    - identifier: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx                      # UUID of group allowed to display PowerBi dashboards from the PowerBi workspace
        description: to_fill                                                # Name of group allowed to display PowerBi dashboards from the PowerBi workspace
        rights: Admin                                                       # Level of permission for the group
        type: Group                                                         # Type of group is "Group"

    # Solution
    solution_name: to_fill                                                  # Should be the name of the project like "project1 solution"
    solution_key: to_fill                                                   # Unique key to define according to your naming convention, for example: project1solution1
    solution_description: to_fill                                           # Quick sentence to explain the purpose of the solution
    simulator_repository: to_fill                                           # To fill according to your simulator name
    simulator_version: to_fill                                              # To fill according to your simulator version
    azure_connector_id: to_create_manually_using_API                        # This connector has to be created only one time and will be reused for all solutions
    resource_opening_time_function_key: ''
    transport_duration_function_key: ''
    scenario_download_function_key: ''

    # Webapp
    webapp_name: WebApp-project1                                            # Name of the Static Webapp on Azure, to define according your naming convention
    webapp_app_registration_display_name: App-project1                      # Name of the Webapp App registration on Azure, to define according your naming convention
    webapp_repository_url: https://github.com/organization/project1_webapp1 # /!\ Needs to be a Github repository /!\ will store the webapp source code that will be used to deploy the webapp on the static web app
    webapp_repository_name: project1_webapp1                                # Name of the Github repository
    webapp_repository_branch: main                                          # Name of the Github repository branch
    webapp_organization_name: to_fill                                       # Name of the Github organization
    webapp_location: westeurope                                             # Edit according to your location
    webapp_custom_domain: https://project1-webapp1.<azure_dns_zone>/sign-in # Custom domain to create on Azure, example: https://webapp1.app.example.com/sign-in
    documentation_link: provided_cosmotech_documentation_link               # Documentation link according to your Cosmo Tech product

    # ADX
    adx_permissions:
    - type: App                                                              # Platform App registration type is "App"
        description: to_fill                                                 # Platform App registration name
        principal_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx                   # Platform App registration principal ID
        role: Admin                                                          # Platform App registration role, must be "Admin"
    - type: Group                                                            # Example of admin group on ADX 
        description: to_fill                                                 
        principal_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx                   
        role: Admin                                                        
    - type: User                                                             # Example of admin user on ADX 
        description: username@example.com                                    
        principal_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx                   
        role: Admin                                                          

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
    │   ├── adx
    │   │   └── scripts
    │   │       └── Create.kql
    │   ├── connector_azure_storage.yaml
    │   ├── organization.yaml
    │   ├── powerbi
    │   │   ├── report1.pbix
    │   │   ├── report2.pbix
    │   │   └── report3.pbix
    │   ├── solution.yaml
    │   ├── webapp.yaml
    │   └── workspace.yaml
    └── README.md
    ```

!!! example ".env"

    ```bash
    export BABYLON_ORG_NAME="cosmotech"
    ```
    ```bash
    export BABYLON_SERVICE="https://example.api.cosmotech.com"
    ```
    ```bash
    export BABYLON_TOKEN="<ROOT TOKEN>"
    ```
    ```bash
    source ~/babylonenv/bin/activate
    ```
    ```bash
    babylon namespace use -c test -p dev -s 73a90433-5067-4a16-86d1-b816de22f215
    ```
    ```bash
    babylon apply --organization --var-file variables.yaml project/
    ```
    ```bash
    babylon apply --solution --var-file variables.yaml project/
    ```
    ```bash
    babylon apply --webapp --var-file variables.yaml project/
    ```
    ```bash
    babylon apply --workspace --var-file variables.yaml project/
    ```