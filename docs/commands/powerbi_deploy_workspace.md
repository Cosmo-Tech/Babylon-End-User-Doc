---
hide:
- toc
---
# Power BI Deploy Workspace


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
    You can setup your `email` and your `user principal id` in your config files to deploy powerbi workspace with your credentials (you will find them in this section: [Azure Directory](https://portal.azure.com/#view/Microsoft_AAD_UsersAndTenants/UserManagementMenuBlade/~/AllUsers))

    ```bash
    babylon azure -c <context_id> -p <platform_id> config set azure email <changeme>
    babylon azure -c <context_id> -p <platform_id> config set azure user_principal_id <user_principal_id>
    ```

    Then, make sure you have the rights required
    ```bash
    babylon azure -c <context_id> -p <platform_id> adx permission set -t User -r Admin %azure%user_principal_id
    ```

    Finally, you have to retrieve your access token powerbi
    ```bash
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
    babylon powerbi -c <context_id> -p <platform_id> workspace deploy <WORKSPACE_NAME> \
        --folder <FOLDER_NAME>/scenario \
        --type <scenario_view | dashboard_view>
    ```

!!! Usage
    ```bash
    # Usage: babylon powerbi -c <context_id> -p <platform_id> workspace deploy [OPTIONS] WORKSPACE_NAME
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


## Description

This macro command will deploy a PowerBI workspace and populate it with reports. If the given workspace name already exists, the reports will be published in the existing workspace.

This includes:

  - Creating a PowerBI workspace if it does not exists
  - Add user to PowerBI workspace
  - Uploading all reports from a folder
  - Updating dataset parameters
  - Updating dataset azure credentials

