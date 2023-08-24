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
    You can setup your `email` and your `user principal id` ([Azure Directory](https://portal.azure.com/#view/Microsoft_AAD_UsersAndTenants/UserManagementMenuBlade/~/AllUsers)) in your config files to deploy powerbi workspace with your credentials.

    ```bash
    babylon config set azure email <CHANGEME> -c <context_id> -p <platform_id> 
    ```

    ```bash
    babylon config set azure user_principal_id <USER_PRINCIPAL_ID> -c <context_id> -p <platform_id> 
    ```

    Then, make sure you have the required rights.
    ```bash
    babylon azure adx permission set -c <context_id> -p <platform_id> --type User --role Admin %azure%user_principal_id 
    ```

    Finally, you have to retrieve your access token powerbi
    ```bash
    babylon azure token store -c <context_id> -p <platform_id> --scope powerbi 
    ```

    !!! important 
        The last command will give you a secret.
        ```bash
        export BABYLON_ENCODING_KEY=<your_secret>
        ```


## Macro command

!!! Macro
    ```bash
    babylon powerbi workspace deploy <WORKSPACE_NAME> -c <context_id> -p <platform_id> \
        --folder <FOLDER_NAME>/<scenario | dashboard> \
        --type <scenario_view | dashboard_view> 
    ```

!!! Usage
    ```bash
    # Usage: babylon powerbi workspace deploy [OPTIONS] WORKSPACE_NAME 
    # 
    #   Macro command allowing full deployment of a powerBI workspace
    #   Requires a local folder named `powerbi` and will initialize a full workspace with the
    #   given reports. Won't run powerbi workspace creation if it's already existing
    # 
    # Options:
    #   --folder DIRECTORY          Override folder containing your .pbix files
    #                                   [required]
    #   --parameter <QUERYSTRING QUERYSTRING>...
    #                                   Add a combination <Key Value> that will be
    #                                   sent as parameter to all your datasets
    #   --override                      override reports in case of name conflict ?
    #   --type [scenario_view|dashboard_view]
    #                                   [required]
    #   --help                          Show this message and exit.
    ```




