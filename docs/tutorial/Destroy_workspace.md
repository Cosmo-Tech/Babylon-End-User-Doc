---
description: Tutorial how to destroy a Cosmo Tech workspace
---

# Destroy a Cosmo Tech Workspace

!!! warning "Remember"
    Keep in mind that the `destroy` command is a **macro command** that removes **everything** deployed.

If you no longer need a Cosmo Tech workspace, you can remove it and all associated resources using the `babylon destroy` macro command.  
This will automatically delete the following resources:

- Scenarios and scenario runs
- Datasets
- ADX databases
- Event Hubs
- Azure Functions
- Static Web apps
- Power BI workspaces
- Workspaces
- Run templates
- Solutions

By default, it destroys the resources referenced in the state saved in the namespace file.  

!!! note 
   
    The namespace file is stored at the following path on your host machine:

    ```bash
    ~/.config/cosmotech/babylon/namespace.yaml
    ```
    ```bash
    > cat namespace.yaml          
    context: test
    platform: dev
    state_id: 25075b92-sx82-4952-9e9b-53360dacg45f
    ```

You can also specify a different state file using the `--state-to-destroy` option:

!!! Example "Babylon Destroy"

    ```bash
    babylon destroy --state-to-destroy /path/to/<state_id>
    ```