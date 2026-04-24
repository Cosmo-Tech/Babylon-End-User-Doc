If the **state file** does not exist, the first Babylon command you run will **initialize a new state** and persist it locally.

!!! note
    - To enable persistence in the **cloud**, you must set the parameter `remote: true`.  
      (This will be explained in detail in the *Deploy Workspace* tutorial, just keep it in mind for now.)
    - The structure and content of the state may change in future releases as needed.

### State Configuration

Babylon now stores the state as a Kubernetes Secret within the cluster. This allows us to support all major managed Kubernetes distributions, including AKS, EKS, and GKE.

When you set `remote: true` and execute `babylon apply`, Babylon automatically creates a Secret named `babylon-state-<context_id>-<tenant_id>` in your current namespace to persist the state information.

### Babylon State Structure

The **Babylon state** is a structured YAML file composed of multiple sections.  
At a high level, you will find three main entries:
```yaml
context:
tenant:
remote: true
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