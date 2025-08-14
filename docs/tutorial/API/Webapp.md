To deploy a Static Web App, you can either:

1. **Create a new Azure App Registration** handled automatically by Babylon.  
2. **Use an existing App Registration** requires manual configuration.

This behavior is controlled by the `create` key in the `sidecars.azure.app` section:

- If `create: true` → Babylon will create a new App Registration automatically.
- If `create: false` → You must manually provide:
    - `client_id` → The Azure App Registration Client ID.
    - `displayName` → The name of your App Registration.

!!! example

    ```yaml
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
    ```
!!! warning "Requirements"

    Deploying a Static Web App also requires:
    
    - A **GitHub repository** containing your application code.
    - A **destination branch** that Babylon will use for deployment.

    **Quick start:**

      1. [Create a new GitHub repository](https://github.com/new)
      2. Configure your branch `<BRANCH>` with source code, for example: [Azure sample webapp](https://github.com/Cosmo-Tech/azure-sample-webapp.git)

!!! example "Commands to configure your branch"

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
    git branch -M <BRANCH>   # e.g main 
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
    rm -r .github/ .git-hooks
    ```

    ```bash
    rm -r config.json   # ⚠️ Remove if exists
    ```

    ```bash
    git add .
    ```

    ```bash
    git commit -m "first commit"
    ```

    ```bash
    git push origin <BRANCH> -f
    ```
Now that your web app GitHub repository is configured, you can use this `webapp.yaml` file to deploy a new  static web app:

??? example "Webapp.yaml"

    ```yaml
    kind: WebApp
    namespace:
      remote: true   # false by default
      state_id: 8db6069e-e05f-42e6-b6d6-56dde124516a
      context: test
      platform:
        id: dev
        url: https://dev.api.cosmotech.com/phoenix/v3-0
    metadata:
      workspace_key: "Project1"
    spec:
      sidecars:
        github:
          organization_name: Cosmo-Tech
          repository_name: <YOUR_GITHUB_REPOSITORY>  # e.g azure-webapp-test-brewery-webapps
          branch: <BRANCH>  # e.g main
        powerbi:
          group_id: <changement>
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
                  - https://<custome_domain_of_your_static_web_app>/sign-in
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
          REACT_APP_WORKSPACES_IDS_FILTER: ""
          REACT_APP_APP_VERSION: ""
          REACT_APP_ORGANIZATION_URL: "{{services['api.organization_url']}}"
          REACT_APP_DOCUMENTATION_URL: https://cosmotech.com
          REACT_APP_SUPPORT_URL: https://support.cosmotech.com
      payload:
        name: "my-webapp-for-continuous"
        location: westeurope
        properties:
          repositoryUrl: https://github.com/<YOUR_GITHUB_REPOSITORY> 
          branch: <BRANCH>  # e.g main
          repositoryToken: "{{github_secret}}"
          buildProperties:
            appLocation: "/"
            apiLocation: api
            appArtifactLocation: build
        sku:
          name: Standard
          tier: Standard

    ```