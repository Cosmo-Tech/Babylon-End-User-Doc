This is how the solution deployment file is structured

!!! example "Solution.yaml"

    ```yaml
    kind: Solution
    namespace:
      remote: true   # false by default
    metadata:
      selector:
        organization_id: "{{services['api.organization_id']}}"
    spec:
      payload:
        key: "demosolution"
        name: "My Solution Name"
        description: "My solution description"
        repository: brewery_for_continuous
        version: latest
        sdkVersion: '10.4.0'
        alwaysPull: true
        url: 'https://webapp.com'
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

The `selector` block is used to specify the **target organization** under which the resource will be deployed.  

- **Parameter**: `organization_id`  
    - **Purpose**:  
      Defines the unique organization in which the solution (or other resource) will be created.  

- **Behavior**:  
    - Babylon will associate the deployment (e.g., a solution, workspace) with the specified **organization_id**.  
    - Typically, this value is injected dynamically from the Babylon state (`services['api.organization_id']`).  