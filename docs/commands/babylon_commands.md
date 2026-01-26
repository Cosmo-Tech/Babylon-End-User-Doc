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
                                                                 v5.0.0-beta.1

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

## Namespace Use Command

!!! info "Namespace Use"

    ```bash
     > babylon namespace use -c test -t dev -s 4s5de
       ✔ Switched to context test, tenant dev successfully
    ```
## Apply Macro Command

!!! info "Macro Apply"

    ```bash
     > babylon apply project/
    ```
## Apply Single Command

!!! info "Create Organization"

    ```bash
     > babylon api organizations create project/Organization.yaml
    ```
    ```bash
     > babylon api organizations delete --oid o-xxxxxxxxxxxxx
    ```
## Destroy Macro Command

!!! info "Macro Destroy"

    ```bash
     > babylon destroy
    ```