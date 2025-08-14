---
description: Tutorial for setting up and initialization variables in Babylon Vault
---

# Populating the Vault

!!! abstract "Objective"
    The Vault service must be properly configured to work with the **Babylon CLI**.  

    In particular, you need to set up the **Terraform backend state** inside Vault.  

    We provide a tool for this, you can find it here 🔗[Vault](https://github.com/Cosmo-Tech/backend-tf-state-to-vault)
    This needs an initial Terraform deployment as it uses the Terraform state to parse and populate the Vault.
    
    Useful information can be found in the **README** of this repository !

!!! warning "Requirements"
    Before running this script, ensure that:  

    * **Cosmo Tech Platform is fully installed on your Azure tenant**  
    * **A Terraform state named `platform-tenant-infra-0001`** is present

## Installation

This tutorial starts from a clean installation

---

### **Get the Script from Source**

!!! warning "Additional Requirements"
    * 🐍 **Python 3.10+**  
    * 📦 **Pip 22.2+**  
    * 🌱 **Git (latest version)**  

---

!!! example "💻 Setup Environment"
    ```bash
    # 🔽 Clone the repository
    git clone git@github.com:Cosmo-Tech/backend-tf-state-to-vault.git
    cd backend-tf-state-to-vault

    # 🛠️ Create and activate a virtual environment
    python3 -m venv ~/backend-tf-state-to-vault
    source ~/backend-tf-state-to-vault/bin/activate

    # 📦 Install dependencies
    pip install -r requirements.txt
    ```

## Usage

---

### 1. Configure Environment Variables

For best practices, create a file (e.g. `.env.platform_name-tenant_name`) and define all required environment variables:

!!! example "⚙️ Configure Environment Variables"
    ```bash
    # Vault configuration
    export VAULT_ADDR="vault_url"
    export VAULT_TOKEN="vault_root_token"

    # Platform & Tenant identifiers
    export TENANT_ID="azure_tenant_id"
    export ORGANIZATION_NAME="vault_org_name"
    export CLUSTER_NAME="kunernetes_cluster_name"
    export PLATFORM_NAME="ns_platform_id"
    export PLATFORM_ID="ns_platform_id"

    # Terraform state storage
    export TFSTATE_BLOB_NAME="terraform_state_tenant_infra-id"
    export STORAGE_ACCOUNT_NAME="storage_account_name"
    export STORAGE_ACCOUNT_KEY="storage_account_key_to_get_from_Azure"
    export STORAGE_CONTAINER="container_hosting_terraform_states"
    ```

Fill in all values according to your environment

!!! note "important"
    For **VAULT_ADDR** and **VAULT_TOKEN**, you can retrieve them from the cluster using one of the following methods

    === "🖥️ Using k9s"
        Open `k9s`, navigate to the **vault** namespace, and retrieve the secret storing the root token.  
        For the Vault URL, check the **Ingress**.

    === "🧩 Using kubectl"
        ```bash
        # List all secrets in the 'vault' namespace
        kubectl -n vault get secrets

        # Get the detailed YAML of the vault token secret
        kubectl -n vault get secret vault-token-secret -o yaml

        # Describe the ingress resource to find the Vault URL
        kubectl -n vault describe ingress
        ```

### 2. Run the Script

Once your environment is configured, you can start using the script 

!!! tip "💡 Quick Run"
    ```bash
    source .env.platform_name-tenant_name

    # Enable secrets "cosmotech" (Vault engine v1)
    python main.py tenant enable --name cosmotech --engine v1

    # Write platform config into Vault (e.g. "main")
    python main.py config write --resource all --use-azure --engine v1 --platform-id main
    ```






