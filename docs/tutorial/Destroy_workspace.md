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
    → Existing ID sol-6069lgex2xz found. Deleting...
    ✔ Solution sol-6069lgex2xz deleted
    ⚠ No Workspace ID found in state! skipping deletion
    → Existing ID o-nl8pgn5lpwd found. Deleting...
    ✔ Organization o-nl8pgn5lpwd deleted 

📋 Destruction Summary
    • Organization Id : DELETED
    • Solution Id     : DELETED
    • Workspace Id    : DELETED

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
        → Existing ID w-3pkx99z1k3v found. Deleting...
        ✔ Workspace w-3pkx99z1k3v deleted

    📋 Destruction Summary
        • Organization Id : o-9zmdn7w95k2
        • Solution Id     : sol-4vqjmov980v
        • Workspace Id    : DELETED
    ```

!!! example "🛡️ Protected Destruction"
    Destroy everything **except** a specific object (e.g., keep the organization):
    ```bash
    babylon destroy --exclude organization
    ```
    ```bash
    🔥 Starting Destruction Process in namespace: dev
        → Loading configuration from Kubernetes secret...
        → Existing ID sol-4vqjmov980v found. Deleting...
        ✔ Solution sol-4vqjmov980v deleted
        ⚠ No Workspace ID found in state! skipping deletion

    📋 Destruction Summary
        • Organization Id : o-9zmdn7w95k2
        • Solution Id     : DELETED
        • Workspace Id    : DELETED

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