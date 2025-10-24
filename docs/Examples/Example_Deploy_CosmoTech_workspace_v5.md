---
description: Example from scratch for deploying a Cosmo Tech workspace with babylon v5
---

# Deploy Cosmo Tech workspace 

!!! important
    For testing, use the `sphinx` platform is already configured in Vault.

After creating the Python virtual environment (`.venv`) to use Babylon, you can now get started<br>
See 👉 [Install Babylon](../partials/installation/from_source.md#install-babylon)

!!! example "Deploy with Babylon v5"
    Export Vault Variables
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
    Create a folder of your choice, for example
    ```bash
    mkdir test-babylon && cd test-babylon
    ```
    Run the Babylon init command to generate the project structure
    ```bash
    babylon init
    ```
    Now, you will see all the manifest files already generated for a minimal deployment.
    You can modify them as you wish, and then start the deployment process.
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
    You can also test individual Babylon commands, such as updating security, runtemplates, etc.
    ```bash 
    babylon api organizations security  get-all
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