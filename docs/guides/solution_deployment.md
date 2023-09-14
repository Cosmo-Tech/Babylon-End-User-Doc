---
 hide:
  - toc
---

You can perform the following commands to deploy a new solution

!!! abstract "Remember"

    You have to choose the platform and project you want to work. Contact your babylon admin to know more about your options.

    In this example, we will use

    * context_id: `brewery`
    * platform_id: `perf`


<br>

### Container Registry

```bash
# retrieve configuration to work with dev platform
babylon config init -c brewery -p dev
```

```bash
# retrieve configuration to work with perf platform
babylon config init -c brewery -p perf
```

```bash
# listing images
babylon azure acr list -c brewery -p perf
```

```bash
# pull image from `dev` platform
babylon azure acr pull -i <image_docker:version> -c brewery -p dev
```

```bash
# push image to `perf` platform
babylon azure acr push -i <image_docker:version> -c brewery -p perf
```

### Setup basic configuration

```bash
babylon config set azure email <CHANGEME> -c brewery -p perf
```

```bash
babylon config set azure user_principal_id <user_principal_id> -c brewery -p perf
```
```bash
babylon config set api workspace_key <workspace_key> -c brewery -p perf
```

```bash
babylon config set powerbi dashboard_view -c brewery -p perf 
```

```bash
babylon config set powerbi scenario_view -c brewery -p perf 
```

```bash
babylon config set azure team_id <team_id> -c brewery -p perf
```

```bash
babylon config set acr simulator_repository <image_docker> -c brewery -p perf
```

```bash
babylon config set acr simulator_version <version> -c brewery -p perf
```

At this point, you can create or retrieve an organization

### Create organization


```bash
babylon api organizations payload create -c brewery -p perf
```

```bash
babylon api organizations create <organization_name> -c brewery -p perf
```

```bash
babylon api oeganizations security add -c brewery -p perf --email <CHANGEME> --role admin
```


```bash
babylon azure storage container create <organization_id> -c brewery -p perf 
```


```bash
babylon azure iam set -c brewery -p perf \
    --resource-type "Microsoft.Storage/storageAccounts" \
    --role-id %azure%storage_blob_reader \
    --principal-id %azure%team_id \
    --principal-type Group \
    --resource-name %azure%storage_account_name
```

```bash
babylon azure iam set -c brewery -p perf \
    --resource-type "Microsoft.Storage/storageAccounts" \
    --role-id %azure%storage_blob_reader \
    --principal-id %platform%principal_id \
    --resource-name %azure%storage_account_name
```

### Retrieve an organization

```bash
babylon api organizations get <organization_id> -c brewery -p perf 
```

```bash
# Optional
babylon api organizations get <organization_id> -c brewery -p perf \
    --output .payload/brewery.dev.organization.yaml
```

```bash
babylon azure iam set -c brewery -p perf \
    --resource-type "Microsoft.Storage/storageAccounts" \
    --role-id %azure%storage_blob_reader \
    --principal-id %azure%team_id \
    --principal-type Group \
    --resource-name %azure%storage_account_name
```

```bash
babylon azure iam set -c brewery -p perf \
    --resource-type "Microsoft.Storage/storageAccounts" \
    --role-id %azure%storage_blob_reader \
    --principal-id %platform%principal_id \
    --resource-name %azure%storage_account_name
```

At this point, you can create or retrieve an ADT Instance if you need it.

### Create ADT instance

```bash
babylon azure adt instance create -c brewery -p perf 
```

```bash
babylon azure iam set -c brewery -p perf \
    --resource-type Microsoft.DigitalTwins/digitalTwinsInstances \
    --role-id %adt%built_owner_id 
```

```bash
babylon azure iam set -c brewery -p perf \
    --resource-type Microsoft.DigitalTwins/digitalTwinsInstances \
    --role-id %adt%built_reader_id
```

```bash
babylon azure set -c brewery -p perf \
    --principal-id %azure%team_id \
    --principal-type Group \
    --resource-type Microsoft.DigitalTwins/digitalTwinsInstances \
    --role-id %adt%built_owner_id
```

```bash
babylon azure set -c brewery -p perf \
    --principal-id %azure%team_id \
    --principal-type Group \
    --resource-type Microsoft.DigitalTwins/digitalTwinsInstances \
    --role-id %adt%built_reader_id 
```

### Retrieve ADT instance

```bash
babylon config set adt digital_twins_url <digital_twins_url> -c brewery -p perf 
```

```bash
babylon azure iam set -c brewery -p perf \
    --resource-type Microsoft.DigitalTwins/digitalTwinsInstances \
    --role-id %adt%built_owner_id 
```

```bash
babylon azure iam set -c brewery -p perf \
    --resource-type Microsoft.DigitalTwins/digitalTwinsInstances \
    --role-id %adt%built_reader_id
```

```bash
babylon azure set -c brewery -p perf \
    --principal-id %azure%team_id \
    --principal-type Group \
    --resource-type Microsoft.DigitalTwins/digitalTwinsInstances \
    --role-id %adt%built_owner_id
```

```bash
babylon azure set -c brewery -p perf \
    --principal-id %azure%team_id \
    --principal-type Group \
    --resource-type Microsoft.DigitalTwins/digitalTwinsInstances \
    --role-id %adt%built_reader_id 
```

```bash
babylon azure adt model upload dtdl/ -c brewery -p perf 
```

### Azure Data Explorer database

Configuration 

!!! warning "Requirements"
    By default this command requires a folder called `adx` containing scripts *.kql 

        ├── adx
        │   ├── script.kql
    
    ```bash
    # by default the name is <organization_id>-<workspace_key>
    babylon azure adx database create -c brewery -p perf 
    ```

    ```bash
    babylon azure adx permission set -c brewery -p perf --type User --role Admin %azure%user_principal_id  
    ```

    ```bash
    babylon azure adx permission set -c brewery -p perf --type Group --role Admin %azure%team_id
    ```

    ```bash
    babylon azure adx permission set -c brewery -p perf --type App --role Admin %platform%principal_id 
    ```

    ```bash
    babylon azure adx script run-folder adx/ -c brewery -p perf
    ```

### Create Eventhub namespace 

```bash
babylon azure arm run -c brewery -p perf --file %templates%/arm/eventhub_deploy.json <NAME>
```

Make sure you have all rights.

```bash
babylon azure iam set -c brewery -p perf \
    --resource-type Microsoft.EventHub/Namespaces \
    --role-id %azure%eventhub_built_data_receiver \
    --principal-id %adx%cluster_principal_id
```

```bash
babylon azure iam set -c brewery -p perf \
    --resource-type Microsoft.EventHub/Namespaces \
    --role-id %azure%eventhub_built_data_sender \
    --principal-id %platform%principal_id 
```

```bash
babylon azure iam set -c brewery -p perf \
    --resource-type Microsoft.EventHub/Namespaces \
    --role-id %azure%eventhub_built_data_sender \
    --principal-id %babylon%principal_id
```

```bash
babylon azure iam set -c brewery -p perf \
    --principal-id %azure%team_id \
    --principal-type Group \
    --resource-type Microsoft.EventHub/Namespaces \
    --role-id %azure%eventhub_built_contributor_id 
```

### Eventhub consumer group and connectors ADX

```bash
babylon azure adx consumer add "adx" "ProbesMeasures" -c brewery -p perf 
```

```bash
babylon azure adx consumer add "adx" "ScenarioMetaData" -c brewery -p perf 
```

```bash
babylon azure adx consumer add "adx" "ScenarioRun" -c brewery -p perf 
```

```bash
babylon azure adx consumer add "adx" "ScenarioRunMetaData" -c brewery -p perf 
```

### Create connections

```bash
babylon azure adx connections create -c brewery -p perf ProbesMeasures %adx%database_name \
    --data-format JSON \
    --table-name ProbesMeasures \
    --compression GZip \
    --consumer-group adx \
    --mapping ProbesMeasuresMapping
```

```bash
babylon azure adx connections create -c brewery -p perf ScenarioMetaData %adx%database_name \
    --data-format CSV \
    --table-name ScenarioMetadata \
    --consumer-group adx \
    --mapping ScenarioMetadataMapping
```
    
```bash
babylon azure adx connections create -c brewery -p perf ScenarioRun %adx%database_name \
    --data-format JSON \
    --table-name SimulationTotalFacts \
    --consumer-group adx \
    --mapping SimulationTotalFactsMapping
```

```bash
babylon azure adx connections create -c brewery -p perf ScenarioRunMetaData %adx%database_name \
    --data-format CSV \
    --table-name ScenarioRunMetadata \
    --consumer-group adx \
    --mapping ScenarioRunMetadataMapping
```

### Retrieve eventhub key

!!! warning "Requirements"
    Azure CLI
    
    ```bash
    eventkey=$(az eventhubs namespace authorization-rule keys list \
        -g <RESOURCE_GROUP> \
        --namespace-name <ORGANIZATION_ID>-<WORKSPACE_ID> \
        --name RootManageSharedAccessKey \
        --query primaryKey)
    ```

    ```bash
    # save this secret
    babylon hvac set project eventhub $eventkey -c brewery -p perf
    ```

### PowerBI deploy

!!! warning "Requirements"
    By default this macro command requires a folder called `powerbi` containing two sub-folders (`dashboard` and `scenario`) with your `.pbix` files. 

        ├── powerbi
        │   ├── dashboard
        │   │   ├── dashboard_1.pbix
        │   │   ├── ...
        │   └── scenario
        │       └── scenario.pbix


!!! info "Note"
    You can setup your `email` and your `user principal id` ([Azure Directory](https://portal.azure.com/#view/Microsoft_AAD_UsersAndTenants/UserManagementMenuBlade/~/AllUsers)) in azure section to deploy powerbi workspace with your credentials

    ```bash
    babylon config set azure email <CHANGEME> -c brewery -p perf 
    ```

    ```bash
    babylon config set azure user_principal_id <user_principal_id> -c brewery -p perf  
    ```

    ```bash
    babylon azure  token store -c brewery -p perf --scope powerbi  
    ```

    !!! warning 
        The last command `babylon azure  token store -c brewery -p perf --scope powerbi` will give you a secret
        ```bash
        export BABYLON_ENCODING_KEY=<your_secret>
        ```

    !!! Macro
        ```bash
        babylon powerbi workspace deploy <WORKSPACE_NAME> -c brewery -p perf --type dashboard_view --folder powerbi/dashboard/ --override 
        ```

        ```bash
        babylon powerbi workspace deploy <WORKSPACE_NAME> -c brewery -p perf --type scenario_view --folder powerbi/scenario/ --override 
        ```

    [Get additional information about command](/commands/powerbi_deploy_workspace/)  

<br>

### Webapp deploy

!!! warning "Requirements"
    This macro requires a github access token set in vault service.
        
    Please generate github access token using classic tokens [Github access Tokens](https://github.com/settings/tokens) and perform the following command:
    
    ```bash
    babylon hvac set global github token [github_token]
    ```

    This macro requires a github repository with the destination branch already created.
    
    1. [create a new repository](https://github.com/new) in Github  
    1. configure your branch `<BRANCH>` with the source code. (example: https://github.com/Cosmo-Tech/azure-sample-webapp.git)
        
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
    git commit -m "add readme"
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

    Setup the webapp configuration.

    ```bash
    babylon config set azure function_artifact_url <uri_artifact_zip> -c brewery -p perf  
    ```
    ```bash
    babylon config set webapp deployment_name <CHANGEME> -c brewery -p perf 
    ```
    ```bash
    babylon config set webapp location <CHANGEME> -c brewery -p perf 
    ```
    ```bash
    babylon config set github branch <CHANGEME> -c brewery -p perf 
    ```
    ```bash
    babylon config set github organization <CHANGEME> -c brewery -p perf 
    ```
    ```bash
    babylon config set github repository <CHANGEME> -c brewery -p perf 
    ```
    ```bash
    babylon webapp deploy -c brewery -p perf 
    ```
    ```bash
    babylon powerbi workspace user add -c brewery -p perf %app%principal_id App Admin
    ```

    ```bash
    babylon azure iam set -c brewery -p perf \
        --resource-type Microsoft.EventHub/Namespaces \
        --role-id %azure%eventhub_built_data_sender \
        --principal-id %app%principal_id 
    ```

    [Get additional information about command](/commands/webapp_deploy/)  

<br>

### Retrieve azure function key

!!! warning "Requirements"
    Azure CLI

    ```bash
    azf_key=$(az functionapp keys list \ 
        -g <RESOURCE_GROUP> \
        -n <ORGANIZATION_ID>-<WORKSPACE_KEY> --query masterKey)
    ```
    
    ```bash
    # save this secret
    babylon hvac set project func $azf_key -c brewery -p perf 
    ```

At this point, you can create or retrieve a solution.

### Create Solution

```bash
babylon api solutions payload create -c brewery -p perf 
```

!!! info 
    You will find a new file in `.payload` directory.

    * Make changes in solution description file `.payload/brewery.dev.solution.yaml`

```bash
babylon api solutions create <solution_name> -c brewery -p perf 
```


### Create Workspace

```bash
# setup run_templates
babylon config set api run_templates -c brewery -p perf \
    --item "1" \
    --item "2" \
    --item "3" 
```

```bash
babylon api workspaces payload create -c brewery -p perf 
```

!!! info 
    You will find a new file in `.payload` directory.
    
    * Make changes in workspace description file `.payload/brewery.dev.workspace.yaml`

```bash
babylon api workspaces create <CHANGEME> -c brewery -p perf 
```

### Register the eventhub key in workspace

```bash
babylon api workspaces send-key -c brewery -p perf 
```
