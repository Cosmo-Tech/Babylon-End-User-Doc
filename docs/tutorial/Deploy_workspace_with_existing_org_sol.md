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
    * platform_id: `dev`
    * state_id: `8db6069e-e05f-42e6-b6d6-56dde124516a`

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
- `webapp.yaml`

!!! warning "Required Parameter"
    The `workspace_key` parameter **must** be included in each `metadata` section.  
    If `workspace_key` is empty, the deployment will **fail**.

### Selector Overview

Within `metadata`, there is a nested section called `selector` where you can set the `organization_id` field.  
This allows deployment of a solution **within an existing organization**.

!!! note "Important"
    Add `organization_id` to the `variables.yaml` file.
    
    !!! example "variables.yaml" 
       
        ```yaml
        state_id: 8db6069e-e05f-42e6-b6d6-56dde124516a
        context_id: test
        platform_id: dev
        platform:
           id: dev
           url: https://dev.api.cosmotech.com/phoenix/v3-0
        
        workspace_key: Project1
        # API 
        organization_id: o-rv0x8vd464kl
        ```
Below is an example of the solution manifest structure.

??? example "solution.yaml"

    ```yaml
    kind: Solution
    namespace:
      remote: true   # false by default
      state_id: "{{state_id}}"
      context: "{{context_id}}"
      platform: {{platform}}
    metadata:
      workspace_key: "{{workspace_key}}"
      selector:
        organization_id: "{{organization_id}}" # <---
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

## :material-folder: Deploy a new workspace withing an existing solution and organization

Similarly, you can deploy a new **Workspace** within an existing **Organization** and **Solution**.  

To do this, add both `organization_id` and `solution_id` under `metadata.selector` in the workspace configuration file.

??? example "Workspace.yaml"

    ```yaml
    kind: Workspace
    namespace:
      remote: true   # false by default
      state_id: "{{state_id}}"
      context: "{{context_id}}"
      platform: {{platform}}
    metadata:
      workspace_key: "{{workspace_key}}"
      selector:
        organization_id: "{{organization_id}}" # <--- 
        solution_id: "{{solution_id}}"         # <---
    spec:
      sidecars:
        azure:
          powerbi: # <--- powerbi section
            workspace:
              name: "My workspace Powerbi Name"
              reports:
                - name: Report Name A
                  type: dashboard
                  path: "powerbi/myreportA.pbix"
                  tag: "myReportATag"
                  parameters:
                    - id: "ADX_Cluster"
                      value: "https://{{services['adx.cluster_name']}}.westeurope.kusto.windows.net"
                    - id: "ADX_Database"
                      value: "{{services['api.organization_id']}}-{{workspace_key}}"
              permissions:
                - identifier: "user1@email.com"
                  rights: Admin
                  type: User
                - identifier: "user2@email.com"
                  rights: Contributor
                  type: User
                - identifier: "user3@email.com"
                  rights: Viewer
                  type: User
                - identifier: "<guid>"
                  description: "Object Id of Service Principal WebApp"
                  rights: Admin
                  type: App
          adx:                   # <--- adx section
            database:
              uri: "https://{{services['adx.cluster_name']}}.{{location}}.kusto.windows.net"  # URI Azure Data Explorer Cluster
              create: true
              retention: 365
              permissions:
                - type: User
                  email: "user1@email.com"
                  principal_id: "412f3fad-3ce3-588s-994c-2a36bccaa0b2"
                  role: Admin
                - type: User
                  email: "user2@email.com"
                  principal_id: "987d3fad-3ce3-588s-994c-2f5s4de8ddd5"
                  role: User
                - type: App
                  description: "Cosmo Tech Platform <platform_name> For <tenant_name>"
                  principal_id: "{{services['platform.principal_id']}}" # Object ID of Platform Enterprise Application
                  role: Admin
              scripts:
                - id: "demoscript"
                  name: Create.kql
                  path: "adx/scripts"
          eventhub:                    # <--- Eventhub section
            consumers:
              - displayName: adx
                entity: ProbesMeasures
              - displayName: adx
                entity: ScenarioMetadata
              - displayName: adx
                entity: ScenarioRun
              - displayName: adx
                entity: ScenarioRunMetadata
            connectors:
              - table_name: ProbesMeasures
                consumer_group: adx
                connection_name: ProbesMeasures
                database_target: "{{services['api.organization_id']}}-{{workspace_key}}"
                format: JSON
                compression: Gzip
                mapping: ProbesMeasuresMapping
              - table_name: ScenarioMetadata
                consumer_group: adx
                connection_name: ScenarioMetadata
                database_target: "{{services['api.organization_id']}}-{{workspace_key}}"
                format: CSV
                compression: None
                mapping: ScenarioMetadataMapping
              - table_name: SimulationTotalFacts
                consumer_group: adx
                connection_name: ScenarioRun
                database_target: "{{services['api.organization_id']}}-{{workspace_key}}"
                format: JSON
                compression: None
                mapping: SimulationTotalFactsMapping
              - table_name: ScenarioRunMetadata
                consumer_group: adx
                connection_name: ScenarioRunMetadata
                database_target: "{{services['api.organization_id']}}-{{workspace_key}}"
                format: CSV
                compression: None
                mapping: ScenarioRunMetadataMapping
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
        webApp:
          url: "https://{{services['webapp.static_domain']}}"
          options:
            disableOutOfSyncWarningBanner: true
            charts:
              workspaceId: "{{services['powerbi.workspace.id']}}"
              dashboardsViewIframeDisplayRatio: 1.8686131386861313
              scenarioViewIframeDisplayRatio: 3.2
              logInWithUserCredentials: false
              dashboardsView:
              scenarioView:
            instanceView:
              dataContent: null
              dataSource: null
            datasetManager:
            menu:
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
    state_id: 8db6069e-e05f-42e6-b6d6-56dde124516a
    context_id: test
    platform_id: dev
    platform:
        id: dev
        url: https://dev.api.cosmotech.com/phoenix/v3-0
    
    workspace_key: Project1
    # API 
    organization_id: o-rv0x8vd464kl
    solution_id: sol-wryolow98dsg
    ```

Now, with this Babylon feature, you can deploy multiple **Workspaces** that:

1. Share the **same Organization and Solution**.
2. Share the **same Organization** but use **different Solutions**.

!!! note "Important"
    For each workspace deployment, you need a **specific state file**.

    e.g :  `state.<context_id>.<platform_id>.<state_id>.yaml`