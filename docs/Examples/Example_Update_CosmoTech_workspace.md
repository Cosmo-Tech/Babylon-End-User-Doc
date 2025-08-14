---
description: Example from scratch for Updating a Cosmo Tech workspace with best practice
---

# Update Cosmo Tech workspace 

!!! abstract "Remember"
    we assumed that the workspace already deployed we need just to update some configuration so this guide we show beast practic to do this with all use cases!

## :material-folder: Modifying Access Control Lists in API Objects

Assuming you need to add users to the access control lists for the **Organization**, **Solution**, and **Workspace**, here is how you can do it:

Go to the workspace repository, open the project, and then edit the `variables.yaml` file.  
In this example, we add users `Alice.Alice.@email.com` and `Bob.Bob@email.com`.

!!! example "variables.yaml"

    ```yaml
    organization_security:
      default: none
      accessControlList:
        - id: admin.user@example.com
          role: admin
        - id: editor.user@example.com
          role: editor
        - id: viewer.user@example.com
          role: viewer
        - id: alice.alice.@email.com   # add Alice user as editor
          role: editor
        - id: bob.bob@email.com    # add Bob user as viewer
          role: viewer

    solution_security:
      default: none
      accessControlList:
        - id: admin.user@example.com
          role: admin
        - id: editor.user@example.com
          role: editor
        - id: viewer.user@example.com
          role: viewer
        - id: alice.alice.@email.com   # add Alice user as editor
          role: editor
        - id: bob.bob@email.com    # add Bob user as viewer
          role: viewer

    workspace_security:
      default: none
      accessControlList:
        - id: admin.user@example.com
          role: admin
        - id: editor.user@example.com
          role: editor
        - id: viewer.user@example.com
          role: viewer
        - id: alice.alice.@email.com   # add Alice user as editor
          role: editor
        - id: bob.bob@email.com   # add Bob user as viewer
          role: viewer
    ```

## :material-console: Applying Babylon Commands

After making the necessary modifications, you can now apply the changes using Babylon commands.

!!! note "Remember"
    In the examples below, we use the `--payload-only` argument because there is no need to redeploy the Azure resources defined in `solution.yaml` and `workspace.yaml`.  
    We only want to update the deployment payload.

!!! warning "Important"
    Be cautious when modifying `workspace.yaml`: Babylon deploys Power BI reports and retrieves their IDs, which are then referenced in the payload under the dashboardview and scenarioview sections.  
    However, when using `--payload-only`, Babylon **skips Azure Power BI report deployment**.  
    Therefore, you must manually add or update the Power BI report references in your `workspace.yaml`.  

    See the example below for how to properly configure this.
    
??? example "workspace.yaml"

    ```yaml
    kind: Workspace
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
        solution_id: "{{services['api.solution_id']}}"
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
                - name: Report Name B
                  type: scenario
                  path: "powerbi/myreportB.pbix"
                  tag: "myReportBTag"
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
                - dynamicFilters:
                    title:
                    en: Report Name A
                    fr: Report Name A
                  # report_tag: "myReportATag"
                  reportId: "{{services['powerbi.dashboard_view.myReportATag']}}" # Babylon retrieves the report ID from the deployment state
              scenarioView:
                - dynamicFilters:
                    title:
                    en: Report Name B
                    fr: Report Name B
                  # report_tag: "myReportBTag"  
                  reportId: "{{services['powerbi.scenario_view.myReportBTag']}}" # Babylon retrieves the report ID from the deployment state
            instanceView:
              dataContent: null
              dataSource: null
            datasetManager:
            menu:
        security: {{workspace_security}}
    ```

With this configuration, Babylon intelligently uses the deployment state where all previously deployed reports are stored with tags.  
This allows Babylon to reference existing reports directly without redeploying them again.

!!! tip "Syntax"

    ```bash
    reportId: "{{services['powerbi.dashboard_view.myReportATag']}}"
    ```
    ```bash
    reportId: "{{services['powerbi.scenario_view.myReportBTag']}}"
    ```

The only case where you should avoid using `--payload-only` is when there are changes in the Azure resources section such as adding a new report or other Azure related modifications that require a full redeployment.

So now you can run the Babylon apply command to apply those modifications.

!!! example "Babylon Apply"

    ```bash
    export BABYLON_ORG_NAME="cosmotech"
    ```
    ```bash
    export BABYLON_SERVICE="https://example.api.cosmotech.com"
    ```
    ```bash
    export BABYLON_TOKEN="<ROOT TOKEN>"
    ```
    ```bash
    source ~/babylonenv/bin/activate
    ```
    ```bash
    babylon namespace use -c test -p dev -s 73a90433-5067-4a16-86d1-b816de22f215
    ```
    ```bash
    babylon apply --organization --var-file variables.yaml project/
    ```
    ```bash
    babylon apply --solution --var-file variables.yaml project/
    ```
    ```bash
    babylon apply --workspace --payload-only --var-file variables.yaml project/
    ```