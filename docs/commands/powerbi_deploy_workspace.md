---
hide:
- toc
---
# Power BI Deploy Workspace

`babylon powerbi deploy-workspace` will deploy a PowerBI workspace and populate it with reports.

This includes:

  - Creating a PowerBI workspace
  - Uploading all reports from a folder
  - Updating dataset parameters
  - Updating dataset azure credentials

???+ warning "Requirements"
    By default this macro command require a folder called `powerbi-reports` containing all your `.pbix` files in your current folder.

???+ abstract "Command"
    ```bash
    babylon powerbi deploy-workspace --help
    # Usage: babylon powerbi deploy-workspace [OPTIONS] WORKSPACE_NAME
    #
    #   Macro command allowing full deployment of a power bi workspace
    #
    #   Require a local folder named `powerbi-reports` and will initialize a full
    #   workspace with the given reports
    #
    # Options:
    #   -f, --report-folder DIRECTORY
    #   -p, --report-parameter <FILETYPE FILETYPE>...
    #   -h, --help                      Show this message and exit.
    ```

???+ success "Arguments"
    === "`WORKSPACE_NAME`"
        This parameter is a required parameter for the command.
        It is a unique string over your Power BI environment that name your future workspace.

???+ note "Options"
    === "`--report-folder` / `-f`"
        This option allows you to replace the default folder `powerbi-report` by any folder you may want to use.
        ???+ example
            ```bash
            ... --report-folder ./myfolder/mypowerbifolder
            ```
    === "`--report-parameter` / `-p`"
        This option can be used multiple times.
        This option allows you to define a pair of key/value that will be applied to all the dataset uploaded during the creation of the workspace
        Both the key and the value can be loaded using the `QueryType` (described in the advanced documentation)
        ???+ example
            ```bash
            # Would set the parameter named MyKey to the value MyValue
            ... --report-parameter MyKey MyValue
            # Would set the parameter named MySecondKey to the value read in the deployment file at `solution_id`
            ... --report-parameter MySecondKey %deploy%solution_id
            ```

???+ failure "Known Issues"
    After setting the parameter, this macro will try to update the credentials of the dataset.
    If you don't have the rights to the targeted databases this step can fail, but won't break the deployment.
    You will need an user with the correct permissions to `take-over` the dataset, and then to upgrade the credentials.

???+ abstract "Steps"
    - [babylon powerbi workspace create](https://cosmo-tech.github.io/Babylon/latest/cli/#create_15)
    - [babylon powerbi report upload](https://cosmo-tech.github.io/Babylon/latest/cli/#upload_2)
    - [babylon powerbi dataset parameters update](https://cosmo-tech.github.io/Babylon/latest/cli/#update_8)
    - [babylon powerbi dataset update-credentials](https://cosmo-tech.github.io/Babylon/latest/cli/#update-credentials)
