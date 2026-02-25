If the **state file** does not exist, the first Babylon command you run will **initialize a new state** and persist it locally.

!!! note
    - To enable persistence in the **cloud**, you must set the parameter `remote: true`.  
      (This will be explained in detail in the *Deploy Workspace* tutorial, just keep it in mind for now.)
    - The structure and content of the state may change in future releases as needed.

### Cloud State Configuration

When you set `remote: true` and run `babylon apply`, you might encounter an error initially.

!!! error 
    ```bash
    🚀 Deploying Organization in namespace: sphinx
      ✘ Failed to initialize BlobServiceClient: Missing environment variables: 'STORAGE_NAME' and 'ACCOUNT_SECRET'
    ```
This is expected behavior as the cloud state requires specific environment variables to authenticate with your storage.

To use the cloud state, you **must** set the following environment variables:

| Variable | Description |
| :--- | :--- |
| `STORAGE_NAME` | The name of your Azure Storage Account. |
| `ACCOUNT_SECRET` | Your Storage Account access key. |


To find your **ACCOUNT_SECRET**, follow these steps in the Azure Portal:

1. Navigate to your **Storage Account**.
2. In the left-hand menu, go to the **Security + networking** section.
3. Click on **Access keys**.
4. You can use either `key1` or `key2` as your secret.

![Azure Access Keys](../assets/Access_keys.png)

!!! tip "Security Best Practice"
    Never commit your `ACCOUNT_SECRET` to a git repository. Always use environment variables or a secret manager to keep your credentials safe

**How to set them :**

!!! important
    === "🖥️ Windows"
        ```powershell
        $env:STORAGE_NAME="your_storage_account_name"
        $env:ACCOUNT_SECRET="your_access_key"
        ```
    === "🐧 Linux"
        ```bash
        export STORAGE_NAME="your_storage_account_name"
        export ACCOUNT_SECRET="your_access_key"
        ```

### Babylon State Structure

The **Babylon state** is a structured YAML file composed of multiple sections.  
At a high level, you will find three main entries:
```yaml
context:
files: []
id: 
tenant:
services:
  api:
    organization_id: 
    solution_id: 
    workspace_id: 
  postgres:
    schema_name: 
  webapp:
    webapp_name: 
    webapp_url:
```