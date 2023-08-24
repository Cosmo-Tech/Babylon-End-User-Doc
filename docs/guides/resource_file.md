The `babylon config -c <context_id> -p <platfom_id> select` command will create all config files for you.

You will find,

** Azure Container Registry **

* acr.yaml
```yaml
<context_id>:
  login_server: 
  simulator_repository: 
  simulator_version: 
```


** Azure Digital Twins **

* adt.yaml
```yaml
<context_id>:
  built_owner_id: 
  built_reader_id: 
  digital_twin_url: 
```

** Azure Explorer Database **

* adx.yaml
```yaml
<context_id>:
  built_contributor_id: 
  built_owner_id: 
  cluster_name: 
  cluster_principal_id: 
  cluster_uri: 
  database_name: 
```

** Cosmotech API **

* api.yaml
```yaml
<context_id>:
  connector:
    adt_id: 
    adt_version: 
    storage_id: 
    storage_version: 
    twin_id: 
    twin_version: 
  dataset:
    adt_id: 
    storage_id: 
    twin_id: 
  organization_id: 
  organization_url: 
  run_templates: 
  scope: 
  send_scenario_metadata_to_event_hub: 
  solution_id: 
  url: 
  use_dedicated_event_hub_namespace: 
  workspace_id: 
  workspace_key: 
```

** Azure App Registration **

* app.yaml
```yaml
<context_id>:
  app_id: 
  name: 
  object_id: 
  principal_id: 
```

** Azure Babylon App Registration **

* babylon.yaml
```yaml
<context_id>:
  client_id: 
  principal_id: 
```

** Github **

* github.yaml
```yaml
<context_id>:
  branch: 
  organization: 
  repository: 
  run_url: 
  workflow_path: 
```

** Cosmotech Platform **

* platform.yaml
```yaml
<context_id>:
  app_id: 
  principal_id: 
  scope_id: 
```

** PowerBI **

* powerbi.yaml
```yaml
<context_id>:
  dashboard_view: 
  group_id: 
  scenario_view: 
  scope: 
  workspace:
    id: 
    name: 
```

** WebApp **

* webapp.yaml
```yaml
<context_id>:
  deployment_name: 
  enable_insights: 
  hostname: 
  insights_instrumentation_key: 
  location: 
  static_domain: 
```


** Azure **

* azure.yaml
```yaml
<context_id>:
  function_artifact_url: 
  resource_group_name: 
  resource_location: 
  storage_account_name: 
  team_id: 
  subscription_id: 
  email: 
  eventhub_built_contributor_id: 
  eventhub_built_data_receiver: 
  eventhub_built_data_sender:  
  cli_client_id: 
  storage_blob_reader: 
  user_principal_id: 
```
