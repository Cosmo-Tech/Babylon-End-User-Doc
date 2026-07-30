---
description: Tutorial how to destroy a Cosmo Tech workspace
---

# Destroy a Cosmo Tech Workspace

!!! warning "Remember"
    Keep in mind that the `destroy` command is a **macro command** that removes **everything** deployed.

If you no longer need a Cosmo Tech workspace, you can remove it and all associated resources using the `babylon destroy` macro command.  
This will automatically delete the following resources:

- Organizations
- Solutions
- Workspaces
- Superset assets
- PostgreSQL schemas
- kubernetes Secrets and ConfigMaps related to the workspace
- Web App

By default, it destroys the resources referenced in the current state saved in the namespace file.

To view the current context and state being used by Babylon, run the following command:

```bash
babylon namespace get-contexts
```

```bash
CURRENT  CONTEXT          TENANT  STATE ID  
*        test             dev     state 
```
When is the case you run simplement 

```bash
> babylon destroy
```
```bash
🔥 Starting Destruction Process in namespace: dev
    → Loading configuration from Kubernetes secret...
    → Existing ID sol-9epr7jxn2ndl found. Deleting...
    ✔ Solution sol-9epr7jxn2ndl deleted
    → Destroying postgreSQL schema for workspace w-0rnd73k2kyd5...
    → Applying kubernetes destroy job...
    → Waiting for job postgresql-destroy-w-0rnd73k2kyd5 to complete...
    → Checking job logs for errors...
    ✔ Schema destruction w_0rnd73k2kyd5 completed successfully
    → Deleting workspace Secret ...
    ✔ Secret o-841ez282ypmx-w-0rnd73k2kyd5 deleted
    → Deleting workspace ConfigMap ...
    ✔ ConfigMap o-841ez282ypmx-w-0rnd73k2kyd5-coal-config deleted
    → Deleting Superset assets ...
    → Found 3 dashboard(s) to delete for workspace 'w-0rnd73k2kyd5'
    ✔ Successfully deleted 3 dashboard(s)
    → Found 9 chart(s) to delete for workspace 'w-0rnd73k2kyd5'
    ✔ Successfully deleted 9 chart(s)
    → Found 2 dataset(s) to delete for workspace 'w-0rnd73k2kyd5'
    ✔ Successfully deleted 2 dataset(s)
    ✔ Superset asset cleanup complete for workspace 'w-0rnd73k2kyd5'
    → Existing ID w-0rnd73k2kyd5 found. Deleting...
    ✔ Workspace w-0rnd73k2kyd5 deleted
    → Existing ID o-841ez282ypmx found. Deleting...
    ✔ Organization o-841ez282ypmx deleted
    → Running Terraform destroy for WebApp resources...
    Acquiring state lock. This may take a few moments...
    module.chart-keycloak-client.data.kubernetes_secret.keycloak: Reading...
    module.chart-cosmotech-webapp.kubernetes_config_map.webapp: Destruction complete after 0s
   
    Destroy complete! Resources: 5 destroyed.
    ✔ WebApp webapp-business destroyed  

📋 Destruction Summary
  • Organization Id : DELETED
  • Solution Id     : DELETED
  • Workspace Id    : DELETED
  • Webapp Name     : DELETED

✨ Cleanup process complete
```
## Selective Destruction
The same **include/exclude philosophy** applies to resource destruction. This allows you to avoid removing specific objects or to target only a single resource for deletion.

To prevent removing a specific object while destroying others, or to focus on a single one, use the following flags:

!!! example "🗑️ Targeted Destruction"
    Destroy only a specific object (e.g., only the workspace):
    ```bash
    babylon destroy --include workspace
    ```
    ```bash
    🔥 Starting Destruction Process in namespace: dev
        → Loading configuration from Kubernetes secret...
        → Destroying postgreSQL schema for workspace w-6wj966w290n...
        → Applying kubernetes destroy job...
        → Waiting for job postgresql-destroy-w-6wj966w290n to complete...
        ✔ Schema w_6wj966w290n destroyed successfully
        → Deleting workspace Secret ...
        ✔ Secret o-6xq4g8veyj6-w-6wj966w290n deleted
        → Deleting workspace ConfigMap ...
        ✔ ConfigMap o-6xq4g8veyj6-w-6wj966w290n-coal-config deleted
        → Deleting Superset assets ...
        → Found 3 dashboard(s) to delete for workspace 'w-6wj966w290n'
        ✔ Successfully deleted 3 dashboard(s)
        → Found 9 chart(s) to delete for workspace 'w-6wj966w290n'
        ✔ Successfully deleted 9 chart(s)
        → Found 2 dataset(s) to delete for workspace 'w-6wj966w290n'
        ✔ Successfully deleted 2 dataset(s)
        ✔ Superset asset cleanup complete for workspace 'w-6wj966w290n'
        → Existing ID w-6wj966w290n found. Deleting...
        ✔ Workspace w-6wj966w290n deleted
        ☁ Syncing state cleanup to kubernetes...
        ✔ State secret babylon-state-project1-dev updated in namespace dev

    📋 Destruction Summary
        • Organization Id : o-6xq4g8veyj6
        • Solution Id     : sol-xm9k95oqv64
        • Workspace Id    : DELETED
        • Webapp Name     : DELETED

    ✨ Cleanup process complete
    ```

!!! example "🛡️ Protected Destruction"
    Destroy everything **except** a specific object (e.g., keep the organization):
    ```bash
    babylon destroy --exclude organization
    ```
    ```bash
    🔥 Starting Destruction Process in namespace: dev
        → Loading configuration from Kubernetes secret...
        → Existing ID sol-enowllxmdwx found. Deleting...
        ✔ Solution sol-enowllxmdwx deleted
        ⚠ No schema found ! skipping deletion
        → Deleting workspace Secret ...
        ⚠ Secret not found already deleted
        → Deleting workspace ConfigMap ...
        ⚠ ConfigMap not found already deleted
        → Deleting Superset assets ...
        → Found 0 dashboard(s) to delete for workspace ''
        ✔ Successfully deleted 0 dashboard(s)
        → Found 0 chart(s) to delete for workspace ''
        ✔ Successfully deleted 0 chart(s)
        → Found 0 dataset(s) to delete for workspace ''
        ✔ Successfully deleted 0 dataset(s)
        ✔ Superset asset cleanup complete for workspace''
        ⚠ No Workspace ID found in state! skipping deletion
        → Running Terraform destroy for WebApp resources...
        No changes. No objects need to be destroyed.
        Either you have not created any objects yet or the existing objects were
        already deleted outside of Terraform.

        Destroy complete! Resources: 0 destroyed.
        ✔ WebApp webapp-business destroyed
        ☁ Syncing state cleanup to kubernetes...
        ✔ State secret babylon-state-project1-dev updated in namespace dev

    📋 Destruction Summary
        • Organization Id : o-j0p01z13k58
        • Solution Id     : DELETED
        • Workspace Id    : DELETED
        • Webapp Name     : DELETED

    ✨ Cleanup process complete
    ```

!!! tip "Safety First"
    Always run `babylon namespace get-contexts` before a destruction command to verify which environment you are currently targeting.

<!-- 
You can also specify a different state file using the `--state-to-destroy` option:

!!! Example "Babylon Destroy"

    ```bash
    babylon destroy --state-to-destroy /path/to/<state_id>
    ``` -->