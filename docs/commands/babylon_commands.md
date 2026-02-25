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
                                                                 v5.0.0-beta.2

      CLI used for cloud interactions between CosmoTech and multiple cloud
      environment

    Options:
    -v, --verbosity LVL   Either CRITICAL, ERROR, WARNING, INFO or DEBUG
    -n, --dry-run         Will run commands in dry-run mode.
    --version             Print version number and return.
    --log-path DIRECTORY  Path to the directory where log files will be stored.
                            If not set, defaults to current working directory.
    --help                Show this message and exit.

    Commands:
    api        Cosmotech API
    apply      Macro Apply
    destroy    Macro Destroy
    init       Scaffolds a new Babylon project structure using YAML templates.
    namespace  Babylon namespace
    ```

## About Command

!!! info "About Command"

    ```bash
    babylon api about
    ```
    ```bash
    → Loading configuration from Kubernetes secret...
    → Sending request to API..
    ✔ API About Information: version=AboutInfoVersion(full='5.0.0-rc5-897806da', release='5.0.0-rc5', major=5, minor=0, patch=0, label='rc5', build='897806da')
    ```
## Namespace Use Command

!!! info "Namespace Use"

    ```bash
    babylon namespace use -c test -t dev -s 4s5de
    ```
    ```bash
     ✔ Switched to context test, tenant dev successfully
    ```
    ```bash
    babylon namespace get-contexts
    ```
    ```bash
    babylon namespace get-states local/remote
    ```
## Apply Macro Command

!!! info "Macro Apply"

    ```bash
    babylon apply project/
    ```
    ```bash
    babylon apply --var-file devops.yaml devops/
    ```
    ```bash
    babylon apply --exclude webapp --var-file devops.yaml devops/ 
    ```
    ```bash
    babylon apply --include organization --var-file devops.yaml devops/ 
    ```
## Apply Single Command

!!! info "Create Organization"

    ```bash
    babylon api organizations create project/Organization.yaml
    ```
    ```bash
    babylon api organizations delete --oid o-xxxxxxxxxxxxx
    ```
    ```bash
    babylon api solutions list --oid o-xxxxxxxxxxxxx
    ```
    ```bash
    babylon api workspaces get --oid o-xxxxxxxxxxxxx --wid w-xxxxxxxxxxxxx
    ```
## Destroy Macro Command

!!! info "Macro Destroy"

    ```bash
    babylon destroy
    ```
    ```bash
    babylon destroy --include workspace
    ```
    ```bash
    babylon destroy --exclude organization
    ```