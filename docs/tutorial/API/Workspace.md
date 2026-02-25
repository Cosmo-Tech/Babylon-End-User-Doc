The **Workspace configuration** may include additional parameters required to provision external services.

These parameters are normally defined under the `sidecars` section.

One of the major changes is the replacement of the `ADX` database with `PostgreSQL` by default. Babylon now automatically creates a dedicated PostgreSQL schema for each workspace, which can be used to store runner results. As a result, the `sidecars` section now references `postgres` instead of `ADX`.

#### PostgreSQL Schema Creation with Kubernetes Job

With the new workspace configuration, Babylon leverages a Kubernetes job to automate the creation of a PostgreSQL schema for each workspace. This is defined under the `sidecars.postgres.schema.jobs` section:

When `create` is set to `true`, Babylon will execute the specified Kubernetes job (`k8s_job.yaml`) located in the `postgres/jobs` directory. This job is responsible for initializing the PostgreSQL schema required by the workspace. This approach ensures that each workspace has its own isolated schema, improving data management and security.

!!! example "Workspace.yaml"

    ```yaml
    kind: Workspace
    namespace:
      remote: true   # false by default
    spec:
      sidecars:
        postgres:
          schema:
            create: true # false by default
            jobs:
              - name: k8s_job.yaml
                path: postgres/jobs
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
          webapp:
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
            datasetManager: 'removeToDisableDatasetManager'
            datasourceFilter: []
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