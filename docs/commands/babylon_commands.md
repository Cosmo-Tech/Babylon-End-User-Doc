---
description: "Reference guide for essential Babylon CLI commands"
---
# Babylon Commands

## Help Command

!!! info "Help command"
    ```text
    > babylon --help
    Usage: babylon [OPTIONS] COMMAND [ARGS]...

       ____              __                 ___  
      /\  _`\           /\ \               /\_ \  
      \ \ \L\ \     __  \ \ \____   __  __ \//\ \      ___     ___  
       \ \  _ <'  /'__`\ \ \ '__`\ /\ \/\ \  \ \ \    / __`\ /' _ `\  
        \ \ \L\ \/\ \L\.\_\ \ \L\ \\ \ \_\ \  \_\ \_ /\ \L\ \/\ \/\ \  
         \ \____/\ \__/.\_\\ \_,__/ \/`____ \ /\____\\ \____/\ \_\ \_\  
          \/___/  \/__/\/_/ \/___/   `/___/> \\/____/ \/___/  \/_/\/_/  
                                        /\___/  
                                        \/__/  
                                                                 v4.2.3

      CLI used for cloud interactions between CosmoTech and multiple cloud

        environment

        The following environment variables are required:

        - BABYLON_SERVICE: Vault Service URI
        - BABYLON_TOKEN: Access Token Vault Service
        - BABYLON_ORG_NAME: Organization Name
            

        Options:
        -v, --verbosity LVL     Either CRITICAL, ERROR, WARNING, INFO or DEBUG
        --bare, --raw, --tests  Enable test mode, this mode changes output
                                formatting.
        -n, --dry-run           Will run commands in dry-run mode.
        --version               Print version number and return.
        --help                  Show this message and exit.

        Commands:
        abba       Cosmotech ABBA
        api        Cosmotech API
        apply      Macro Apply
        azure      Group allowing communication with Microsoft Azure Cloud
        destroy    Macro Destroy
        github     Group allowing communication with Github REST API
        hvac       Group handling Vault Hashicorp
        namespace  Babylon namespace
        powerbi    Group handling communication with PowerBI API
        webapp     Group handling Cosmo Sample WebApp configuration
    ```

## Namespace Use Command

!!! info "Namespace Use"

    ```bash
     > babylon namespace use -c test -t dev -s 25075b92
       INFO     2025-08-11 18:01:45,484 | [namespace] switched to namespace test, dev successfully
    ```
## Apply Macro Command

!!! info "Macro Apply"

    ```bash
     > babylon apply project/
    ```
## Apply Single Command

!!! info "Apply Organization"

    ```bash
     > babylon apply --organization --var-file variables.yaml project/
    ```
!!! info "Apply Solution"

    ```bash
     > babylon apply --solution --var-file variables.yaml project/
    ```
!!! info "Apply Workspace"

    ```bash
     > babylon apply --workspace --var-file variables.yaml project/
    ```
## Destroy Macro Command

!!! info "Macro Destroy"

    ```bash
     > babylon destroy --state-to-destro /path/to/<state_id>
    ```