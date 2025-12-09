The **Workspace configuration** may include additional parameters required to provision external services such as:

- **Power BI workspaces**
- **Azure Event Hubs**
- **Azure Data Explorer (ADX) databases**

These parameters are normally defined under the `sidecars` section, specifically within the `cloud` key.

However, this is **not the case in the current release**, because Cosmotech API v5 does **not depend on any external cloud resources** for the moment.


!!! example "Workspace.yaml"

    ```yaml
    kind: Workspace
    namespace:
      remote: true   # false by default
    metadata:
      selector:
        organization_id: "{{services['api.organization_id']}}"
        solution_id: "{{services['api.solution_id']}}"
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