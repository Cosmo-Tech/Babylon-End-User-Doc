---
description: Example for setting up a Cosmo Tech workspace with Power BI dashboards
---

# Deploy with Power BI dashboards

!!! info "Init tree with Babylon v5"
    From Babylon v5 onwards, the `init` command will create a sub-folder `dashboard/<bi_provider>` under the project folder (by default, `project` if not otherwise indicated with the `--project-folder` option).

## :material-folder: Including the dahsboard files in the project tree

Assuming you have retreieved configured Power BI dahsboards from a working Power BI workspace, you will have just to put the .pbix files, one per dashboard, in the `dashboard/powerbi` folder of your project folder:

!!! example "Project tree example"

    ```bash
    .
    ├── babylon.log
    ├── project
    │   ├── dashboard
    │   │   └── powerbi
    │   │       └── brewery_dashboard.pbix
    │   ├── Organization.yaml
    │   ├── postgres
    │   │   └── jobs
    │   │       └── k8s_job.yaml
    │   ├── Solution.yaml
    │   ├── Webapp.yaml
    │   └── Workspace.yaml
    ├── devops.yaml
    └── terraform-webapp
    ```


## :material-file-edit: Babylon workspace configuration

Having included the .pbix dashboards, the Workspace needs to be configured manually to include the dashboards in the Solution after deployment:

!!! example "Workspace yaml 'charts' field"

    ```bash
      charts:
        workspaceId: "{{powerbi['workspace_id']}}"
        logInWithUserCredentials: false
        useWebappTheme: true
        dashboardsViewIframeDisplayRatio: 1.6
        scenarioViewIframeDisplayRatio: 2.14
        dashboardsView:
          - title:
              en: Customer Overview
              fr: Aperçu des clients
            reportId: "{{powerbi['reports']['brewery_dashboard']}}"
            settings:
              filterPaneEnabled: false
              navContentPaneEnabled: false
            pageName:
              en: d3c00faba401072eeff8
              fr: d3c00faba401072eeff8
            dynamicFilters:
              - table: "{{services['postgres.schema_name']}} cosmotech_satisfaction"
                column: Simulation_run
                values: lastRunId
              - table: "{{services['postgres.schema_name']}} cosmotech_stock"
                column: Simulation_run
                values: lastRunId
          - title:
              en: Stock Overview
              fr: Aperçu des stocks
            reportId: "{{powerbi['reports']['brewery_dashboard']}}"
            pageName:
              en: 2b30f1d8886fc53849b3
              fr: 2b30f1d8886fc53849b3
            settings:
              filterPaneEnabled: false
              navContentPaneEnabled: false
            dynamicFilters:
              - table: "{{services['postgres.schema_name']}} cosmotech_satisfaction"
                column: Simulation_run
                values: lastRunId
              - table: "{{services['postgres.schema_name']}} cosmotech_stock"
                column: Simulation_run
                values: lastRunId
        scenarioView:
          full_demo:
            reportId: "{{powerbi['reports']['brewery_dashboard']}}"
            pageName:
              en: f5e73ba46b8e2085c239
              fr: f5e73ba46b8e2085c239
            settings:
              filterPaneEnabled: false
              navContentPaneEnabled: false
            dynamicFilters:
              - table: "{{services['postgres.schema_name']}} cosmotech_satisfaction"
                column: Simulation_run
                values: lastRunId
              - table: "{{services['postgres.schema_name']}} cosmotech_stock"
                column: Simulation_run
                values: lastRunId
    ```

!!! info "Power Bi workspace ACL"
    Azure app registration for the WebApp is configured with the ACL (Access Control List) defined in the Power BI configurations in the `powerbi_permissions` field in [variables.yaml](/Examples/Example_Deploy_CosmoTech_workspace.md#start-deployment)

!!! warning "Azure permissions"
    The user running `babylon macro apply` must have the **Application Administrator** role in Azure AD. This is required to allow creation of App Registrations and Enterprise Applications needed for Power BI workspace setup.

!!! warning "Power BI license"
    A **valid Power BI license** is required for the workspace to allow Power BI workspace creation and report publishing.
