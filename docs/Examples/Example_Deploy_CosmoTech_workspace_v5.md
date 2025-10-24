---
description: Deploy an example Cosmo Tech workspace from scratch with Babylon 5
---

# Deploy Cosmo Tech workspace 

!!! important
    Babylon needs a configured Vault instance in order to work properly. Contact the DevOps team if you need to access one!

After creating the Python virtual environment (`.venv`) to use Babylon, you can now get started.<br>
See 👉 [Install Babylon](../partials/installation/from_source.md#install-babylon)

!!! example "Deploy with Babylon v5"
    Export Vault variables
    ```bash
    export BABYLON_ORG_NAME="cosmotech" # cosmotech
    export BABYLON_TOKEN="vault_root_token"  # hvs.CLxxxxxxxxxxxxxxx
    export BABYLON_SERVICE="https://warp.api.cosmotech.com"
    ```
    Run babylon namespace use command 
    ```bash
    uuidgen | cut -c1-8 # to generate uuid 
    ```  
    ```bash
    babylon namespace use -c test-v5 -p sphinx -s 220d04f0 
    ```   
    Create a test folder, for example
    ```bash
    mkdir test-babylon && cd test-babylon
    ```
    Run the init command to generate the project structure
    ```bash
    babylon init
    ```
    All the manifest files for a minimal deployment are now ready.
    Edit them as you need, and then start the deployment process:
    ```bash
    babylon apply --organization project/  
    ```
    ```bash
    babylon apply --solution project/
    ```
    ```bash    
    babylon apply --workspace project/ 
    ```
    ```bash 
    babylon apply --runner project/
    ```
    You can also test individual Babylon commands: list resources, update security, etc.
    ```bash 
    babylon api organizations security get-all
    ```
    ```bash 
    babylon api solutions security get --email toto.tata@cosmotech.com 
    ```
    ```bash 
    babylon api workspaces security set-default --role admin
    ```
    ```bash 
    babylon api runners get-all
    ```
