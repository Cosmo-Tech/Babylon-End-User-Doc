---
description: Tutorial for creating or update Cosmo Tech workspace with and existing organization and solution
---

# Deploy Cosmo Tech workspace with an existing organization and solution

!!! abstract "Remember"
    This guide focuses on explaining who we can deploy a wokspace with an existing organization and solution.  
    A complete deployment workflow is provided in the [Examples](../Examples/Example_Deploy_CosmoTech_workspace.md) section, where all components are combined in a practical scenario !

    Before proceeding, ensure that you have selected the correct `platform` and `project`.  
    If unsure, contact your `Babylon administrator` for the available options.
    In this example, we will use
    
    * context_id: `test`
    * tenant_id: `dev`
    * state_id: `8db6069e`

Before going further, you should know that we have two concepts: deploying a solution object within an existing organization, and deploying a workspace object within an existing organization and solution. This is just to give you some quick context for the tutorial.

## :material-folder: Deploy a new solution Within an existing organization

In this section, we will walk through deploying a **Solution** within an **existing Organization**.  
This setup assumes that:

- You already have at least **one Organization** deployed.
- A **Solution** can be deployed and linked to this existing organization.

To deploy a new **Solution** within an **existing Organization**, you must declare its configuration in the YAML file.  
The main changes occur in the `solution.yaml` file, where you add the `metadata` section.

### Metadata Overview

The `metadata` section contains deployment specific data and can appear in:

- `solution.yaml`
- `workspace.yaml`

### Selector Overview

Within `metadata`, there is a nested section called `selector` where you can set the `organization_id` field.  
This allows deployment of a solution **within an existing organization**.

!!! note "Important"
    Add `organization_id` to the `variables.yaml` file.
    
    !!! example "variables.yaml" 
       
        ```yaml
        # API 
        organization_id: o-rv0x8vd464kl
        ```
Below is an example of the solution manifest structure.

!!! example "solution.yaml"

    ```yaml
    kind: Solution
    namespace:
      remote: true   # false by default
    metadata:
      selector:
        organization_id: "{{organization_id}}" # <---
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

## :material-folder: Deploy a new workspace withing an existing solution and organization

Similarly, you can deploy a new **Workspace** within an existing **Organization** and **Solution**.  

To do this, add both `organization_id` and `solution_id` under `metadata.selector` in the workspace configuration file.

!!! example "Workspace.yaml"

    ```yaml
    kind: Workspace
    namespace:
      remote: true   # false by default
    metadata:
      selector:
        organization_id: "{{organization_id}}" # <--- 
        solution_id: "{{solution_id}}"         # <---
    spec:
      sidecars:
        cloud:
      payload:
        key: "Project1"
        name: "My Workspace Name"
        description: "Workspace for solution"
        solution:
          solutionId: "{{services['api.solution_id']}}"
        useDedicatedEventHubNamespace: true
        sendScenarioMetadataToEventHub: true
        sendInputToDataWarehouse: true
        sendScenarioRunToEventHub: true
        additionalData:
          webApp:
            solution:
              runTemplateFilter:
              defaultRunTemplateDataset: null
            charts:
              workspaceId:
              logInWithUserCredentials: false
              scenarioViewIframeDisplayRatio: 4.514285714
              dashboardsViewIframeDisplayRatio: 1.610062893
              useWebappTheme: true
              dashboardsView:
              scenarioView:
            menu:
              supportUrl: 'https://support.cosmotech.com'
              organizationUrl: 'https://cosmotech.com'
              documentationUrl: 'https://portal.cosmotech.com/resources/platform-resources/web-app-user-guide'
            datasetManager:
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

Make sure to reference the corresponding `organization_id` and `solution_id` values declared in your `variables.yaml` file.

!!! example "variables.yaml" 
    
    ```yaml
    # API 
    organization_id: o-rv0x8vd464kl
    solution_id: sol-wryolow98dsg
    ```

Now, with this Babylon feature, you can deploy multiple **Workspaces** that:

1. Share the **same Organization and Solution**.
2. Share the **same Organization** but use **different Solutions**.

!!! note "Important"
    For each workspace deployment, you need a **specific state file**.

    e.g :  `state.<context_id>.<tenant_id>.<state_id>.yaml`