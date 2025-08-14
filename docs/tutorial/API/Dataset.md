To deploy one or multiple datasets, one yaml file is needed by dataset. Four _sourceType_ of datasets are
available:

- ADT - creates dataset from ADT
- AzureStorage - creates dataset with Azure Storage
- File - creates dataset from a local file
- None - creates an empty dataset

??? example "Dataset.yaml"

    ```yaml
    kind: Dataset
    namespace:
      remote: true   # false by default
      state_id: 8db6069e-e05f-42e6-b6d6-56dde124516a
      context: test
      platform:
        id: dev
        url: https://dev.api.cosmotech.com/phoenix/v3-0
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
            - id: user1@email.com
              role: admin
            - id: user2@email.com
              role: editor
            - id: user3@email.com
              role: viewer
    ```
!!! warning "Note current usage"
    
    - To create a dataset, we currently use the **API endpoint** to register a new dataset.
    - Connector ID (must be also created via API see API Connector section)

    ??? example "API INPUT"

        ```yaml
          name: mydataset
          description: Some description of your dataset
          tags:
            - dataset
            - File Storage
          connector:
            id: c-q5qv7xcsqv64
            parametersValues:
              AZURE_STORAGE_CONTAINER_BLOB_PREFIX: "%WORKSPACE_FILE%/default_parameters/<mydataset>/data.xlsx"
          security:
            default: editor
            accessControlList:
              - id: user1@email.com
                role: admin
              - id: user2@email.com
                role: editor
              - id: user3@email.com
                role: viewer
        ```