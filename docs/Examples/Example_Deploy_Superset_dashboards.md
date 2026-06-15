---
description: Example for setting up a Cosmo Tech workspace with Superset dashboards
---

# Deploy with Superset dashboards

!!! info "Init tree with Babylon v5"
    From Babylon v5 onwards, the `init` command will create a sub-folder `dashboard/<bi_provider>` under the project folder (by default, `project` if not otherwise indicated with the `--project-folder` option).

## :material-folder: Including the dahsboard files in the project tree

Assuming you have retreieved configured Superset dahsboards from a working cluster, you will have just to put the zipped files, one per dashboards, in the `dashboard/superset` folder of your project folder:

!!! example "Project tree example"

    ```bash
    .
    ├── babylon.log
    ├── project
    │   ├── dashboard
    │   │   └── superset
    │   │       ├── dashboard_satisfaction.zip
    │   │       ├── dashboard_scenarioView.zip
    │   │       └── dashboard_stock.zip
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


## :material-file-edit: Applying Babylon Commands

Having included the zipped dashboards, the Workspace needs to be configured manually to include the dashboards in the Solution after deployment:

!!! example "Workspace yaml 'charts' field"

    ```bash
      charts:
        supersetDomain: 'https://superset-{{cluster_name}}.{{domain_zone}}'
        dashboards:
          - id: '{{qadashboardsatisfaction}}'
            width: 100%
            filters:
              - id: YYAjEQr9vU5hY6JDURdd5
                operator: ==
                column: Simulation_run
                value: lastRunId
          - id: '{{qadashboardscenarioview}}'
            width: 100%
            filters:
              - id: RU4aRKyBZNo-VOvm-RlGr
                operator: ==
                column: Simulation_run
                value: lastRunId
          - id: '{{qadashboardstocks}}'
            width: 100%
            filters:
              - id: CguNPknZV8LkJoV-kSJ1t
                operator: ==
                column: Simulation_run
                value: lastRunId
            hideFilters: true
            expandFilters: false
        scenarioView:
          default: '{{qadashboardscenarioview}}'
        dashboardView:
          - id: '{{qadashboardsatisfaction}}'
            title:
              en: Customers Overview
              fr: Aperçu des clients
          - id: '{{qadashboardstocks}}'
            title:
              en: Stocks Overview
              fr: Aperçu des stocks
    ```

!!! important "Dashboards ids"
    You need to fill the ids of the dashboards in between curly brackets as here above by converting the dahsboard name as appearing in the Superset UI to a lowercase string with all its original special characters removed (for instance, "QA - Dashboard - Scenario View" becomes "qadashboardscenarioview").
    <br>Similarly, for now the filter ids have to be configured manually from the dashboard information found in the Superset IU.

!!! warning "Access rights"
    As currently, in order to be able to see the deployed dashboards in your Solution, you will need to have "Platform admin" assigned as a role in the Keycloak configuration.