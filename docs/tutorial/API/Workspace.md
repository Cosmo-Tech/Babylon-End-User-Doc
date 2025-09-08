The **Workspace configuration** may include additional parameters required to provision external services such as:

- **Power BI workspaces**
- **Azure Event Hubs**
- **Azure Data Explorer (ADX) databases**

These parameters are defined under the `sidecars` section, specifically within the `azure` key.

??? example "Workspace.yaml"

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

The path to existing **Power BI reports** can be specified under the `sidecars → powerbi → workspace → reports` section.  

!!! example 

    ```yaml
        reports:
          - name: Report Name A
            type: dashboard
            path: "powerbi/myreportA.pbix" # <--- 
            tag: "myReportATag"
            parameters:
    ```
### How Babylon Handles Power BI Report IDs

!!! note "Automatic Power BI Report ID Retrieval"
    Babylon can now automatically **retrieve and manage Power BI report IDs** during deployment.  
    This eliminates the need for manual copy-paste of report IDs, as was required before.  

    **How it works**

    - Each imported Power BI report must be assigned a **unique identifier**, called a `tag`.  
    - Babylon uses this `tag` to **map the report ID**.  
    - Once mapped, the report ID can be referenced in the following sections:
        - `dashboardsView`
        - `scenarioView`
    - This referencing will be accomplished using a second variable called `reportTag` in dashboardsView and scenarioView sections, as illustrated in the example below. This variable should correspond to the Power BI report tag you intend to use. Therefore, Babylon will handle everything automatically.

    ??? example
    
        ```yaml
            sidecars:
              powerbi: 
                workspace:
                  reports:
                    - name: Report Name A
                      type: dashboard
                      path: "powerbi/myreportA.pbix"
                      tag: "myReportATag" # Here, you should add the tag corresponding to this Power BI report
                    - name: Report Name B
                      type: dashboard
                      path: "powerbi/myreportB.pbix"
                      tag: "myReportBTag"

            dashboardsView:
              - dynamicFilters:
                title:
                  en: Report Name A
                  fr: Report Name A
                report_tag: "myReportATag"

            scenarioView:
              - dynamicFilters:
                title:
                  en: Report Name B
                  fr: Report Name B
                report_tag: "myReportBTag"
          
        ```
    With this configuration:

    - The `tag` (e.g., `myReportATag`, `myReportBTag`) acts as a **stable reference**.  
    - Babylon automatically resolves and injects the corresponding **Power BI Report ID** into the deployment files.  
    - These IDs are also persisted in the **Babylon state**, ensuring consistency across environments.

    !!! example "Auto-injected Report IDs in `workspace.yaml`"

        ```yaml
            dashboardsView:
              - dynamicFilters: []
                reportTag: "myReportATag"
                title:
                  en: "Report Name A"
                  fr: "Report Name A"
                reportId: "03729d49-c423-4bf5-bb85-681449b56710"

            scenarioView:
              - dynamicFilters: []
                reportTag: "myReportBTag"
                title:
                  en: "Report Name B"
                  fr: "Report Name B"
                reportId: "9c275c7a-d390-40a0-bc75-b9c5c8093986"
        ```
    ---
    !!! example "Stored in Babylon State"

        ```yaml
            powerbi:
              dashboard_view:
                myReportATag: 03729d49-c423-4bf5-bb85-681449b56710
              scenario_view:
                myReportBTag: 9c275c7a-d390-40a0-bc75-b9c5c8093986
        ```

---

All ADX scripts **must be placed** inside the `adx/` folder of your project structure See 👉 [Examples](../../Examples/Example_Deploy_CosmoTech_workspace.md)


!!! abstract "Permissions Reminder"

    Certain operations may fail if Babylon doesn't have the necessary Azure permissions.

    To automatically create **Azure Data Explorer (ADX) databases**, **Azure Functions**, or **Event Hubs**, Babylon must have **at least** the `Contributor` role on the target resource group.

    > 🛡️ **Owner** role is required if Babylon also needs to assign roles to Azure resources during the deployment.

    If you security policy doesn't grant such access to Babylon, these operations must be done manually.