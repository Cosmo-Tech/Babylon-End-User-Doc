This is how the solution deployment file is structured

??? example "Solution.yaml"

    ```yaml
    kind: Solution
    namespace:
      remote: true   # false by default
      state_id: 8db6069e-e05f-42e6-b6d6-56dde124516a
      context: test
      platform:
        id: dev
        url: https://dev.api.cosmotech.com/phoenix/v3-0
    metadata:
      workspace_key: "Project1"
      selector:
        organization_id: "{{services['api.organization_id']}}"
    spec:
      payload:
        key: "demosolution"
        name: "My Solution Name"
        description: "My solution description"
        repository: brewery_for_continuous
        version: latest
        tags:
          - brewery
        runTemplates:
          - id: "run_id"
            name: "Standard simulation"
            csmSimulation: AzureWebApp/AzureWebApp_Simulation
            run: true
            preRun: true
        parameters:
        parameterGroups:
        security:
          default: none
          accessControlList:
            - id: user1@email.com
              role: admin
            - id: user2@email.com
              role: editor
            - id: user3@email.com
              role: viewer
    ```
The **`metadata`** section defines deployment specific attributes. It is required in the following resource files:  

  - `solution.yaml`  
  - `workspace.yaml`  
  - `webapp.yaml`  


The `workspace_key` parameter is a **mandatory field** within the `metadata` section  

- **Purpose**:  
  Identifies the target workspace  
  For example, when Babylon provisions resources such as a **Dataset (ADX)** or an **Event Hub**, the generated name follows the convention:  
  ```bash 
  <organization_id>-<workspace_key> # Ex : o-rv0h6dd492w8-testppdprojectwork
  ```
- **Constraints**:  
    - Must always be defined.  
    - Cannot be left empty.  

- ⚠️ **Failure Condition**:  
    If `workspace_key` is omitted or empty, the deployment will **fail**.


The `selector` block is used to specify the **target organization** under which the resource will be deployed.  

- **Parameter**: `organization_id`  
    - **Purpose**:  
      Defines the unique organization in which the solution (or other resource) will be created.  

- **Behavior**:  
    - Babylon will associate the deployment (e.g., a solution, workspace) with the specified **organization_id**.  
    - Typically, this value is injected dynamically from the Babylon state (`services['api.organization_id']`).  