---
 hide:
  - toc
---

You can perform the following commands to deploy a new solution

!!! abstract "Remember"

    You have to choose the platform and project you want to work. Contact your babylon admin to know more about your options.

    In this example, we will use

    * context_id: `brewery`
    * platform_id: `staging`


<br>

* ** Container Registry ** 
```bash
# retrieve configuration to work with dev platform
babylon config -c brewery -p dev select
# retrieve configuration to work with staging platform
babylon config -c brewery -p staging select

# tranfer image from `dev` to `staging` platform
babylon azure -c brewery -p dev     acr pull -i <image_docker:tag>
babylon azure -c brewery -p staging acr push -i <image_docker:tag>
```

* ** Setting variables ** 
```bash
# set some required variables
babylon config -c brewery -p staging set azure email <changeme>
babylon config -c brewery -p staging set azure user_principal_id <user_principal_id> 
babylon config -c brewery -p staging set api workspace_key <workspace_key> 
babylon config -c brewery -p staging set adx cluster_uri <uri_kusto_cluster> 
babylon config -c brewery -p staging set powerbi dashboard_view 
babylon config -c brewery -p staging set powerbi scenario_view 
babylon config -c brewery -p staging set azure team_id <team_id> 
```

In this point, you can create a new organization or retrieve an organization

* ** Create organization ** 
```bash
babylon config -c brewery -p staging set api workspace_key <changeme>
babylon api    -c brewery -p staging organizations payload create
babylon api    -c brewery -p staging organizations create <organization_name> -e <email> -r Admin
babylon azure  -c brewery -p staging storage container create <organization_id>
babylon azure  -c brewery -p staging iam set -rt Microsoft.Storage/storageAccounts \
    -ri %azure%storage_blob_reader \
    -pi %azure%team_id \
    -pt Group \
    -rn %azure%storage_account_name
```

* ** Retrieve organization ** 
```bash
babylon api   -c brewery -p staging organizations get <organization_id>
babylon azure -c brewery -p staging iam set -rt Microsoft.Storage/storageAccounts \
    -ri %azure%storage_blob_reader \
    -pi %azure%team_id \
    -pt Group \
    -rn %azure%storage_account_name
```

In this point, you can create a new ADT Instance or retrieve an ADT Instance

* ** Create ADT instance **
```bash
# by default the name is <organization_id>-<workspace_key>
babylon azure -c brewery -p staging adt instance create
```

* ** Retrieve ADT instance **
```bash
babylon config -c brewery -p staging set adt digital_twins_url <digital_twins_url>
babylon azure  -c brewery -p staging iam set \
    -rt Microsoft.DigitalTwins/digitalTwinsInstances \
    -ri %adt%built_owner_id
babylon azure  -c brewery -p staging iam set \
    -rt Microsoft.DigitalTwins/digitalTwinsInstances \
    -ri %adt%built_reader_id
babylon azure  -c brewery -p staging iam set \
    -pi %azure%team_id \
    -pt Group \
    -rt Microsoft.DigitalTwins/digitalTwinsInstances \
    -ri %adt%built_owner_id
babylon azure  -c brewery -p staging iam set \
    -pi %azure%team_id \
    -pt Group \
    -rt Microsoft.DigitalTwins/digitalTwinsInstances \
    -ri %adt%built_reader_id
babylon azure  -c brewery -p staging adt model upload dtdl/
```

* ** Azure Data Explorer database ** 

    Configuration 

    !!! warning "Requirements"
        By default this command requires a folder called `adx` containing scripts *.kql 

            ├── adx
            │   ├── script.kql
```bash
# by default the name is <organization_id>-<workspace_key>
babylon azure -c brewery -p staging adx database create
babylon azure -c brewery -p staging adx permission set -t User -r Admin %azure%user_principal_id
babylon azure -c brewery -p staging adx permission set -t Group -r Admin %azure%team_id
babylon azure -c brewery -p staging adx permission set -t App -r Admin %platform%principal_id
babylon azure -c brewery -p staging adx script run-folder adx/
```

* ** Create Eventhub namespace** 
```bash
babylon azure -c brewery -p staging arm run -f %templates%/arm/eventhub_deploy.json
babylon azure -c brewery -p staging iam set \
    -rt Microsoft.EventHub/Namespaces \
    -ri %azure%eventhub_built_data_receiver \
    -pi %adx%cluster_principal_id

babylon azure -c brewery -p staging iam set \
    -rt Microsoft.EventHub/Namespaces \
    -ri %azure%eventhub_built_data_sender \
    -pi %babylon%principal_id

babylon azure -c brewery -p staging iam set \
    -rt Microsoft.EventHub/Namespaces \
    -ri %azure%eventhub_built_data_sender \
    -pi %babylon%principal_id

babylon azure -c brewery -p staging iam set \
    -pi %azure%team_id \
    -pt Group \
    -rt Microsoft.EventHub/Namespaces \
    -ri %azure%eventhub_built_contributor_id
```

* ** Eventhub consumer group and connectors ADX database** 
```bash
# create consumer groups
babylon azure -c brewery -p staging adx consumer add "adx" "ProbesMeasures"
babylon azure -c brewery -p staging adx consumer add "adx" "ScenarioMetaData"
babylon azure -c brewery -p staging adx consumer add "adx" "ScenarioRun"
babylon azure -c brewery -p staging adx consumer add "adx" "ScenarioRunMetaData"

# create connections
babylon azure -c brewery -p staging adx connections create ProbesMeasures %adx%database_name \
    -df JSON \
    -tn ProbesMeasures \
    -cp GZip \
    -cg adx \
    -mp ProbesMeasuresMapping
babylon azure -c brewery -p staging adx connections create ScenarioMetaData %adx%database_name \
    -df CSV \
    -tn ScenarioMetadata \
    -cg adx \
    -mp ScenarioMetadataMapping
babylon azure -c brewery -p staging adx connections create ScenarioRun %adx%database_name \
    -df JSON \
    -tn SimulationTotalFacts \
    -cg adx \
    -mp SimulationTotalFactsMapping
 babylon azure -c brewery -p staging adx connections create ScenarioRunMetaData %adx%database_name \
    -df CSV \
    -tn ScenarioRunMetadata \
    -cg adx \
    -mp ScenarioRunMetadataMapping
```

* ** Retrieve eventhub key ** 

    !!! warning "Requirements"
        Azure CLI
```bash

eventkey=$(az eventhubs namespace authorization-rule keys list \
    -g <your_resource_group> \
    --namespace-name <organization_id>-<workspace_key> \
    --name RootManageSharedAccessKey \
    --query primaryKey)

babylon hvac -c <context_id> -p <platfom_id> set project eventhub $eventkey
```

* ** Deploy PowerBI ** 

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
        babylon azure -c <context_id> -p <platform_id> config set azure email <changeme>
        babylon azure -c <context_id> -p <platform_id> config set azure user_principal_id <user_principal_id>
        babylon azure -c <context_id> -p <platform_id> adx permission set -t User -r Admin %azure%user_principal_id
        babylon azure -c <context_id> -p <platform_id> token store --scope powerbi
        ```

    !!! warning 
        The last command `babylon azure -c <context_id> -p <platform_id> token store --scope powerbi` will give you a secret to set in your environment variables
        ```bash
        export BABYLON_ENCODING_KEY=<your_secret>
        ```

    !!! Macro
        ```bash
        babylon powerbi -c <context_id> -p <platform_id> workspace deploy
        ```

    [Get additional information about command](/commands/powerbi_deploy_workspace/)  

<br>

* ** Deploy Webapp ** 

    !!! warning "Requirements"
        This macro requires a github access token set in vault service.
        
        Please generate github access token using classic tokens [Github access Tokens](https://github.com/settings/tokens) and perform the following command:
        ```bash
        babylon hvac set global github token [github_pat_token]
        ```

        This macro requires a github repository with the destination branch already created  
        
        1. [create a new repository](https://github.com/new) in Github  
        1. configure your branch `<BRANCH>` with the source code. (example: https://github.com/Cosmo-Tech/azure-sample-webapp.git)
        ```bash
        git init
        echo "# empty_webapp" >> README.md
        git add README.md
        git commit -m "add readme"
        git branch -M main
        git remote add origin git@github.com:<YOUR_GITHUB_REPOSITORY>.git
        git remote add upstream https://github.com/Cosmo-Tech/azure-sample-webapp.git
        git remote set-url upstream --push "NO"
        git fetch --all --prune
        git checkout -B <BRANCH> <SOURCE_TAG>
        rm -r .github/
        git add .; git commit -m 'first commit'
        git push origin <BRANCH> -f
        ```

    Now, setup the webapp configuration

    ```bash
    babylon -c brewery -p staging config set azure function_artifact_url <uri_artifact_zip> 
    babylon -c brewery -p staging config set webapp deployment_name <changeme>
    babylon -c brewery -p staging config set webapp location <changeme>
    babylon -c brewery -p staging config set github branch <changeme>
    babylon -c brewery -p staging config set github organization <changeme>
    babylon -c brewery -p staging config set github repository <changeme>
    babylon -c brewery -p staging webapp deploy

    babylon -c brewery -p staging powerbi workspace user add %app%principal_id App Admin
    ```
    [Get additional information about command](/commands/webapp_deploy/)  

<br>

* ** Retrieve azure function key ** 

    !!! warning "Requirements"
        Azure CLI

    ```bash
    azf_key=$(az functionapp keys list \ 
        -g <youtçresource_group> \
        -n <organization_id>-<workspace_key> --query masterKey)

    babylon hvac -c <context_id> -p <platfom_id> set project func $azf_key
    ```

In this point, you can create a new solution or retrieve a solution already created

* ** Create solution ** 
```bash
babylon api -c brewery -p staging solutions payload create
babylon api -c brewery -p staging solutions create <solution_name>
```


* ** Retrieve solution ** 
```bash
babylon api -c brewery -p staging solutions get <solution_id>
```



* ** Create new Workspace ** 
```bash
babylon config -c brewery -p staging set api run_templates \
    -i "1" \
    -i "2" \
    -i "3"

babylon api -c brewery -p staging workspaces payload create
babylon api -c brewery -p staging workspaces create <changeme>


# register the key into workspace 
babylon api -c brewery -p staging workspaces send-key
```
