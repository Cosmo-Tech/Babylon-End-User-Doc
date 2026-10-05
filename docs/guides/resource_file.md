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
At a high level, you will find four main entries (`context`, `remote`, `services`, `tenant`).

Example for a Babylon state file:
```yaml
context:
remote: true
services:
  api:
    organization_id: 
    solution_id: 
    workspace_id: 
  dashboards:
    superset:
      reports:
      workspace_id: 
  postgres:
    schema_name: 
  webapp:
    webapp_name: 
    webapp_url:
tenant:
```
\* Note: This is an example structure of a Babylon state file with Superset dashboards.
The state of a project with Power BI dashboards would have the same structure with a `powerbi` key under the `dashboards` section.

### State Synchronization

Local and remote states are automatically synchronized (since version 5.5.0).

### State Destruction

Local and remote state files are automatically removed after successful resource cleanup with the `destroy` macro command (since version 5.5.0).

### Dashboard IDs & Babylon State
During the first deployment, Babylon creates the required dashboards and stores their IDs in the Babylon state.
For subsequent deployments, Babylon retrieves the existing dashboard IDs from the state.
This allows to have one single source of truth across multiple deployments, with each workspace (instance) referencing the same common configuration and with dashboard IDs being automatically managed through the Babylon state.
