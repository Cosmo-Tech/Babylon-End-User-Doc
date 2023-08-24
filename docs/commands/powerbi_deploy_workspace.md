---
hide:
- toc
---
# Power BI Deploy Workspace

## Description

This macro command will deploy a PowerBI workspace and populate it with reports. If the given workspace name already exists, the reports will be published in the existing workspace.

This includes:

  - Creating a PowerBI workspace if it does not exists
  - Add user to PowerBI workspace
  - Uploading all reports from a folder
  - Updating dataset parameters
  - Updating dataset azure credentials

!!! abstract "Steps"

    1. Create a PowerBI workspace    
    ```bash
    babylon powerbi -c <context_id> -p <platform_id> workspace create <workspace_name>
    ```
    
    1. Add user to workspace  
    ```bash
    babylon powerbi -c <context_id> -p <platform_id> workspace user add <email> User Admin
    ```

    1. Upload a directory of `.pbix` reports to PowerBI Web  
    ```bash
    babylon powerbi -c <context_id> -p <platform_id> report upload 
    ```
    
    1. Take-over command
    ```bash
    babylon powerbi -c <context_id> -p <platform_id> dataset take-over <dataset_id> -e <email>
    ```

    1. Update uploaded PowerBI report parameters `ADX_cluster` and `ADX_database`  
    ```bash
    babylon powerbi -c <context_id> -p <platform_id> dataset parameters update <dataset_id> \
        -e <email> \
        -p ADX_cluster <cluster_name> \
        -p ADX_database %adx%database_name
    ```
    
    1. Refresh Azure credentials used to access data from `ADX`  
    ```bash
    babylon powerbi -c <context_id> -p <platform_id> dataset update-credentials <dataset_id> -e <email>
    ```


## Configuration 

!!! warning "Requirements"
    By default this macro command requires a folder called `powerbi` containing two sub-folders 
    both with your `.pbix` files in respectively directory.

        ├── powerbi
        │   ├── dashboard
        │   │   ├── dashboard_1.pbix
        │   │   ├── dashboard_2.pbix
        │   │   ├── dashboard_3.pbix
        │   │   ├── dashboard_4.pbix
        │   └── scenario
        │       └── scenario.pbix


!!! info "Note"
    You can setup your `email` and your `user principal id` ([Azure Directory](https://portal.azure.com/#view/Microsoft_AAD_UsersAndTenants/UserManagementMenuBlade/~/AllUsers)) in azure section to deploy powerbi workspace with your credentials

    ```bash
    babylon azure -c <context_id> -p <platform_id> config set azure email <changeme>
    babylon azure -c <context_id> -p <platform_id> config set azure user_principal_id <user_principal_id>
    babylon azure -c <context_id> -p <platform_id> adx permission set -t User -r Admin %azure%user_principal_id
    babylon azure -c <context_id> -p <platform_id> token store --scope powerbi
    ```

    !!! important 
        The last command will give you a secret to export it in your environment variables
        ```bash
        export BABYLON_ENCODING_KEY=<your_secret>
        ```


## Macro command

!!! Macro
    ```bash
    babylon powerbi -c <context_id> -p <platform_id> workspace deploy
    ```

!!! abstract "Usage"
    ```bash
    
    # Usage: babylon powerbi workspace deploy [OPTIONS] WORKSPACE_NAME
    # 
    #   Macro command allowing full deployment of a powerBI workspace   Requires a
    #   local folder named `POWERBI` and will initialize a full workspace with the
    #   given reports   Won't run powerbi workspace creation if it's already
    #   existing
    # 
    # Options:
    #   -f, --folder DIRECTORY          Override folder containing your .pbix files
    #                                   [required]
    #   -p, --parameter <QUERYSTRING QUERYSTRING>...
    #                                   Add a combination <Key Value> that will be
    #                                   sent as parameter to all your datasets
    #   --override                      override reports in case of name conflict ?
    #   -t, --type [scenario_view|dashboard_view]
    #                                   [required]
    #   --help                          Show this message and exit.
    # 
    ```



