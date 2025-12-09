If the **state file** does not exist, the first Babylon command you run will **initialize a new state** and persist it locally.

!!! note
    - To enable persistence in the **cloud**, you must set the parameter `remote: true`.  
      (This will be explained in detail in the *Deploy Workspace* tutorial, just keep it in mind for now.)
    - The structure and content of the state may change in future releases as needed.

### Babylon State Structure

The **Babylon state** is a structured YAML file composed of multiple sections.  
At a high level, you will find three main entries:
```yaml
context:
files: []
id: 
tenant:
```
```yaml
services:
  api:
    organization_id: 
    solution_id: 
    workspace_id: 
```

