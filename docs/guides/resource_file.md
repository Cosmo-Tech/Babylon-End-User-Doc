If state file doesn't exist, the first babylon command you launch will create one and store it in Azure Storage
and in `/home/.config/cosmotech/babylon/<state_id>.yaml` file in local.

You will find three main sections:
```yaml
files: []
id: teststate
services:
```
The last one contains following keys with some information already prefilled with data from vault:

Azure Container Registry 

```yaml
  acr:
    login_server: 
    simulator_repository: 
    simulator_version: 
```

Azure Digital Twins 

```yaml
  adt:
    built_owner_id: 
    built_reader_id: 
    digital_twin_url:  
```

Azure Explorer Database

```yaml
  adx:
    built_contributor_id: 
    built_owner_id: 
    cluster_name: 
    cluster_principal_id: 
    cluster_uri: 
    database_name: 
```

Cosmotech API 

```yaml
  api:
    connector.adt_id: 
    connector.adt_version: 
    connector.storage_id: 
    connector.storage_version: 
    connector.twin_id: 
    connector.twin_version: 
    dataset.adt_id: 
    dataset.storage_id: 
    dataset.twin_id: 
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

Azure App Registration

```yaml
  app:
    app_id: 
    name: 
    object_id: 
    principal_id: 
```

Azure 

```yaml
    azure:
      cli_client_id:
      email: 
      eventhub_built_contributor_id:
      eventhub_built_data_receiver:
      eventhub_built_data_sender:
      function_artifact_url: 
      resource_group_name: 
      resource_location: 
      storage_account_name: 
      storage_blob_reader: 
      subscription_id:
      team_id:
      user_principal_id: 
```

Azure Babylon App Registration 

```yaml
    babylon:
      client_id: 
      principal_id: 
```

Github 

```yaml
    github:
      branch: 
      organization: 
      repository: 
      run_url: 
      workflow_path: 
```

Cosmotech Platform 

```yaml
    platform:
      app_id: 
      principal_id: 
      scope_id: 
```

PowerBI

```yaml
    powerbi:
      dashboard_view: 
      scenario_view: 
      scope: 
      workspace.id:
      workspace.name:
```

WebApp 

```yaml
    webapp:
      deployment_name: 
      enable_insights: 
      hostname: 
      insights_instrumentation_key: 
      location: 
      static_domain: 
```
