---
hide:
  - toc
---

!!! abstract "Remember"

    You have to choose the platform and project you want to work. Contact your babylon admin to know more about your options.
    
    In this example, we will use
    
    * context_id: `test`
    * platform_id: `dev`
    * state_id: `teststate`

To deploy a complete Cosmo Tech solution, you can declare its configuration in yaml files corresponding
to specific deployment type. Each file contains general information about the deployment:

```yaml
kind: Organization
namespace:
  state_id: "{{state_id}}"
  context: demo
  platform:
    id: dev
    url: https://dev.api.cosmotech.com/phoenix/v3-0
metadata: 
  workspace_key: "{{workspace_key}}" 
```

The `kind` key must be one of these: Organization, Solution, Workspace, WebApp, Dataset - it decides which
resource will be deployed with specification listed below. Note that the type of resource must always start with capital letter.
`namespace` key gives information that identifies the deployment: state, context and platform.

Also, the `metadata` section contain data specific to each deployment section. The `workspace_key` parameter must be included in each metadata.If `workspace_key` parameter is empty, the deployment will fail.


Then, each file declares resource configuration under `spec` key, specifically in the `payload` section,
e.g., in organization deployment file:

```yaml
kind: Organization
namespace:
 state_id: "{{state_id}}"
 context: demo
 platform:
  id: dev
  url: https://dev.api.cosmotech.com/phoenix/v3-0
metadata: 
  workspace_key: "{{workspace_key}}"
spec:
 payload:
  name: My new Organization
  security: {{security}}
```

All keys in this file can be templated with `{{}}` syntax for objects and `"{{}}"` for strings, as `security` section of this file. Corresponding
values must be stored in _variables.yaml_ file at the same level that your project:

```yaml
security:
  default: viewer
  accessControlList:
    - id: user@email.com
      role: admin
    - id: user2@email.com
      role: editor
workspace_key: digitalsupplychainassetmanagement
```

This is how the solution deployment file is structured:

```yaml
kind: Solution
namespace:
 state_id: "{{state_id}}"
 context: demo
 platform:
  id: dev
  url: https://dev.api.cosmotech.com/phoenix/v3-0
metadata: 
  workspace_key: "{{workspace_key}}"
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

Run templates are enumerated under `sidecars` key which lists every side resources needed for the
correct functioning of the solution. Run templates scripts must be placed in _run_templates_ folder
of your project with the following path: _run_templates/run_template_id/handler_id/script_file_

Workspace configuration contains keys needed to deploy a powerBI workspaces, an event hub
and an adx database. These keys are stored in `sidecars` section, under `azure` key.

```yaml
kind: Workspace
namespace:
 state_id: "{{state_id}}"
 context: demo
 platform:
  id: dev
  url: https://dev.api.cosmotech.com/phoenix/v3-0
metadata: 
  workspace_key: "{{workspace_key}}"
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

Path to existing powerBI reports could be declared in `powerBI` section of sidecars; adx script must be
in adx folder of your project.

!!! abstract "Remember"

    Some operations could fail if Babylon doesn't have enough rights to create Azure resources. 
    To create automatically an adx database, an azure function or an event hub, Babylon must be at least on Contributor 
    level. Owner rights allow it to assign roles to resources. If you security policy doesn't grant
    such access to Babylon, these operations must be done manually. 

To deploy a webapp you can create a new app registration or use an existing one; it can be
declared by `create` key of `sidecars.azure.app` section. If it is set to false, a `client_id` and a `name`
of your app registration must be declared.

!!! warning "Requirements"
Webapp deployment requires a GitHub repository with the destination branch. You can
follow these steps to create it:

1. [create a new repository](https://github.com/new) in Github


2. configure your branch `<BRANCH>` with code source (e.g https://github.com/Cosmo-Tech/azure-sample-webapp.git)


  ```bash
      git init
  ```
  ```bash
      echo "# empty_webapp" >> README.md
  ```
  ```bash
      git add README.md
  ```
  ```bash
      git commit -m "first commit"
  ```
  ```bash
      git branch -M <BRANCH>
  ```
  ```bash
      git remote add origin git@github.com:<YOUR_GITHUB_REPOSITORY>.git
  ```
  ```bash
      git remote add upstream https://github.com/Cosmo-Tech/azure-sample-webapp.git
  ```
  ```bash
      git remote set-url upstream --push "NO"
  ```
  ```bash
      git fetch --all --tags --prune
  ```
  ```bash
      git checkout -B <BRANCH> <SOURCE_TAG>
  ```
  ```bash
      rm -r .github/
  ```
  ```bash
      git add .; git commit -m 'first commit'
  ```
  ```bash
      git push origin <BRANCH> -f
  ```


Then, you can use this repository to deploy a new webapp:


```yaml
kind: WebApp
namespace:
 state_id: "{{state_id}}"
 context: demo
 platform:
  id: dev
  url: https://dev.api.cosmotech.com/phoenix/v3-0
metadata: 
  workspace_key: "{{workspace_key}}"
spec:
 sidecars:
  github:
   organization_name: Cosmo-Tech
   repository_name: azure-webapp-engineering-brewery-deployments
   branch: brewery
  powerbi:
   group_id: changement
   settings:
    properties:
     POWER_BI_SCOPE: "https://analysis.windows.net/powerbi/api/.default"
     POWER_BI_AUTHORITY_URI: https://login.microsoftonline.com/common/v2.0
     POWER_BI_WORKSPACE_ID: "{{services['powerbi.workspace.id']}}"
     POWER_BI_CLIENT_ID: "{{services['app.app_id']}}"
     POWER_BI_CLIENT_SECRET: "{{secret_powerbi}}"
     POWER_BI_TENANT_ID: "{{services['azure.tenant_id']}}"
  azure:
   app:
    create: false
    use:
     displayName: thisismyappforcontinuous
     client_id: "3d0531b1-d23b-4baf-98be-a764c0a42f00"
    principal_id: "{{services['app.principal_id']}}"
    add_to_powerbi: true
    payload:
     displayName: thisismyappforcontinuous
     signInAudience: AzureADMyOrg
     spa:
      redirectUris:
      - http://localhost:3000/sign-in
     requiredResourceAccess:
     - resourceAppId: "{{services['platform.app_id']}}"
       resourceAccess:
        - id: "{{services['platform.scope_id']}}"
          type: Scope
   function:
    url_zip: "https://github.com/Cosmo-Tech/supplychain-azure-function-dataset-download/releases/download/2.1.10/artifact.zip"
  config:
   REACT_APP_APPLICATION_INSIGHTS_INSTRUMENTATION_KEY: "{{services['webapp.insights_instrumentation_key']}}"
   REACT_APP_ENABLE_APPLICATION_INSIGHTS: "{{services['webapp.enable_insights']}}"
   REACT_APP_APP_REGISTRATION_CLIENT_ID: "{{services['app.app_id']}}"
   REACT_APP_AZURE_TENANT_ID: "{{services['azure.tenant_id']}}"
   REACT_APP_COSMOTECH_API_SCOPE: "{{services['api.scope']}}"
   REACT_APP_DEFAULT_BASE_PATH: "{{services['api.url']}}"
   REACT_APP_ORGANIZATION_ID: "{{services['api.organization_id']}}"
   REACT_APP_WORKSPACES_IDS_FILTER: ''
   REACT_APP_APP_VERSION: ''
   REACT_APP_ORGANIZATION_URL: "{{services['api.organization_url']}}"
   REACT_APP_DOCUMENTATION_URL: https://cosmotech.com
   REACT_APP_SUPPORT_URL: https://support.cosmotech.com
 payload:
  name: "my-webapp-for-continuous"
  location: westeurope
  properties:
   repositoryUrl: https://github.com/Cosmo-Tech/azure-webapp-engineering-brewery-deployments
   branch: brewery
   repositoryToken: "{{github_secret}}"
   buildProperties:
    appLocation: "/"
    apiLocation: api
    appArtifactLocation: build
  sku:
   name: Standard
   tier: Standard
```

To deploy one or multiple datasets, one yaml file is needed by dataset. Four _sourceType_ of datasets are
available:

- ADT - creates dataset from ADT
- AzureStorage - creates dataset with Azure Storage
- File - creates dataset from a local file
- None - creates an empty dataset

```yaml
kind: Dataset
namespace:
 state_id: "{{state_id}}"
 context: demo
 platform:
  id: dev
  url: https://dev.api.cosmotech.com/phoenix/v3-0
metadata: 
  workspace_key: "{{workspace_key}}"
spec:
 sidecars:
  azure:
   dataset:
    storage:
     local_path: # needed if you want to upload your local dataset to AzureStorage
    file:
     local_path: # needed for datasets with sourceType File
 payload:
  id: # mandatory if you want to launch an update, without id a new dataset will be created ; if you want a new dataset, leave this field empty
  name: Apply dataset
  description: Creating dataset with nothing but update
  sourceType: None | AzureStorage | ADT | File
  source:
    path: # path to the folder in AzureStorage, mandatory if sourceType is AzureStorage
          # and no local file is provided
    location: # mandatory field if sourceType is ADT: path to dataset stored in ADT;
              # if sourceType is AzureStorage, default value is set to organization
              # container, you can edit this field if you want to use a dataset from
              # another container
    name: # field used for sourceType AzureStorage, by default is set to storage account
          # name referenced in state; edit it if you want to use a dataset from another
          # account
  security:
   default: viewer
   accessControlList:
   - id: e-mail@cosmotech.com
     role: admin
```

Project folder must have this structure:

```bash
 ├── my-deployment
    ├── project
        ├── organization.yaml
        ├── solution.yaml
        ├── workspace.yaml
        ├── webapp.yaml
        ├── dataset1.yaml
        ├── dataset2.yaml
        ├── run_templates
            ├── run-template-id
                ├── run
            ├── adx
                ├── scripts
            ├── powerbi
    ├── variables.yaml
```

After filling all deployment files, you can launch the following command:

```bash
babylon apply project/
```

Babylon will create and deploy all resources and save it in the state except for datasets. Keeping this information in the
state simplifies modification of the resources as you can edit one of the project deployment files
and relaunch `babylon apply` command. It will update existing resources or create missing ones, for example,
in case when Babylon was granted more rights between two `apply` commands.
