!!! abstract "Remember"

    You have to choose the platform and project you want to work. Contact your babylon admin to know more about your options.
    
    In this example, we will use
    
    * context_id: `demo`
    * platform_id: `dev`
    * state_id: `teststate`

## Deploying a solution with an existing organization

To deploy a new solution within an existing organization, you can declare its configuration in the YAML files corresponding to the solution. In this case, you need to add a new field, `metadata`, to the `solution.yaml` file.<br>

The `metadata` section contains data specific to each deployment. It can be found in the `solution.yaml`, `workspace.yaml`, and `webapp.yaml` files.<br>

The `workspace_key` parameter must be included in each metadata. If `workspace_key` parameter is empty, the deployment will fail.<br> 

`Note`: In the `metadata`, there is another section called `selector`. Here, we can add the important field `organization_id`, which allows us to deploy a solution within an existing organization. The user should specify and add `organization_id` to the `variables.yaml` file,
<font color="red"><strong>and ensure that organization deployment is deactivated.</strong></font>

```yaml
kind: Solution
namespace:
  remote: true   # false by default
  state_id: "{{state_id}}"
  context: demo
  platform:
    id: dev
    url: https://dev.api.cosmotech.com/phoenix/v3-0
metadata:
  workspace_key: "{{workspace_key}}"
  selector:
    organization_id: "{{organization_id}}"
spec:
  sidecars:
    azure:
      run_templates:
        - id: run_template_id
          handlers:
            preRun: true
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
    parameterGroups:
    security:
      default: none
      accessControlList:
        - id: e-mail@cosmotech.com
          role: admin

```
## Deploying a workspace with an existing solution and organization

Similarly, if you want to deploy a new workspace within an existing organization and solution, it is now possible. You should add the `organization_id` and `solution_id` in `metadata.selector` and reference the `organization_id` and `solution_id` declared in `variables.yaml`, <font color="red"><strong>and ensure that organization and solution deployment is deactivated.</strong></font>

```yaml
kind: Workspace
remote: true   # false by default
namespace:
  state_id: "{{state_id}}"
  context: demo
  platform:
    id: dev
    url: https://dev.api.cosmotech.com/phoenix/v3-0
metadata:
  workspace_key: "{{workspace_key}}"
  selector:
    organization_id: "{{organization_id}}"
    solution_id: "{{solution_id}}"
spec:
  sidecars:
    azure:
      powerbi:
        workspace:
          name: "My workspace Powerbi Name"
          reports:
            - name: Report Name A
              type: dashboard
              path: "powerbi/myreportA.pbix"
              parameters:
                - id: "ADX_Cluster"
                  value: "https://{{services['adx.cluster_name']}}.westeurope.kusto.windows.net"
                - id: "ADX_Database"
                  value: "{{services['api.organization_id']}}-{{key}}"
          permissions:
            - identifier: "e-mail@cosmotech.com"
              rights: Admin
              type: User
            - identifier: "<guid>"
              description: "Object Id of Service Principal WebApp"
              rights: Admin
              type: App
      adx:
        database:
          uri: https://<name>.<location>.kusto.windows.net  # URI Azure Data Explorer Cluster
          create: true
          retention: 365
          permissions:
            - type: User
              email: e-mail@cosmotech.com
              principal_id: "412f3fad-3ce3-410a-994c-2a36bccaa0b2"
              role: Admin
            - type: App
              description: "Cosmo Tech Platform <some-platform> For <some-tenant>"
              principal_id: "<guid>"
              role: Admin
          scripts:
            - id: "demoscript"
              name: Create.kql
              path: "adx/scripts"
      eventhub:
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
            database_target: "{{services['api.organization_id']}}-{{key}}"
            format: JSON
            compression: Gzip
            mapping: ProbesMeasuresMapping
          - table_name: ScenarioMetadata
            consumer_group: adx
            connection_name: ScenarioMetadata
            database_target: "{{services['api.organization_id']}}-{{key}}"
            format: CSV
            compression: None
            mapping: ScenarioMetadataMapping
          - table_name: SimulationTotalFacts
            consumer_group: adx
            connection_name: ScenarioRun
            database_target: "{{services['api.organization_id']}}-{{key}}"
            format: JSON
            compression: None
            mapping: SimulationTotalFactsMapping
          - table_name: ScenarioRunMetadata
            consumer_group: adx
            connection_name: ScenarioRunMetadata
            database_target: "{{services['api.organization_id']}}-{{key}}"
            format: CSV
            compression: None
            mapping: ScenarioRunMetadataMapping
  payload:
    key: "{{key}}"
    name: "My Workspace Name"
    description: "Workspace for solution"
    solution:
      solutionId: "{{services['api.solution_id']}}"
    useDedicatedEventHubNamespace: true
    sendScenarioMetadataToEventHub: true
    sendInputToDataWarehouse: true
    sendScenarioRunToEventHub: true
    security:
      default: none
      accessControlList:
        - id: e-mail@cosmotech.com
          role: admin

```
<font color="red"><strong>Note</strong></font> : Make sure you have already add those variable in `variables.yaml` file : 

```yaml
# example
state_id: ‘’
workspace_key: ‘’
solution_key: ‘’
simulator: ‘’
simulator_version: ‘’
organization_id: o-djwr88wl60go
solution_id: sol-g1d93qee34yx
```

## Standard deployment including organization and solution creation

If you want to perform a standard deployment from scratch, including creating an organization and solution, ensure that in the `solution.yaml` and `workspace.yaml` files, within the `metadata.selector` section, point directly to the `state` instead of referencing `variables.yaml`, as follows:

```yaml
kind: Solution
remote: true   # false by default
namespace:
  state_id: "{{state_id}}"
  context: demo
  platform:
    id: dev
    url: https://dev.api.cosmotech.com/phoenix/v3-0
metadata:
  workspace_key: "{{workspace_key}}"
  selector:
    organization_id: "{{services['api.organization_id']}}"
spec:
  sidecars:
    azure:
      run_templates:
        - id: run_template_id
          handlers:
            preRun: true
            .............................
```

The same action for `workspace.yaml` :

```yaml
kind: Workspace
remote: true   # false by default
namespace:
  state_id: "{{state_id}}"
  context: demo
  platform:
    id: dev
    url: https://dev.api.cosmotech.com/phoenix/v3-0
metadata:
  workspace_key: "{{workspace_key}}"
  selector:
    organization_id: "{{services['api.organization_id']}}"
    solution_id: "{{services['api.solution_id']}}"
spec:
  sidecars:
    azure:
      powerbi:
        workspace:
          name: "My workspace Powerbi Name"
          reports:
            - name: Report Name A
              type: dashboard
              path: "powerbi/myreportA.pbix"
              parameters:
                - id: "ADX_Cluster"
                  value: "https://{{services['adx.cluster_name']}}.westeurope.kusto.windows.net"
                - id: "ADX_Database"
                  value: "{{services['api.organization_id']}}-{{key}}"
          permissions:
            - identifier: "e-mail@cosmotech.com"
              rights: Admin
              type: User
            - identifier: "<guid>"
              description: "Object Id of Service Principal WebApp"
              rights: Admin
              type: App
              ....................................
```