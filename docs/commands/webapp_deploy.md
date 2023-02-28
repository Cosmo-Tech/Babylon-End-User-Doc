---
hide:
- toc
---
# WebApp Deploy

`babylon webapp deploy` will create a static webapp and configure it with the sample webapp source code.

This includes:

  - Creating and configuring an Azure Static WebApp resource
  - Creating and configuring an Azure Active Directory App Registration
  - Creating an Application Insights
  - Configuring the Sample WebApp source code
  - Adding access to the PowerBI Workspace

???+ abstract "Command"
    ```bash
    babylon webapp deploy --help
    # Usage: babylon webapp deploy [OPTIONS]
    #
    #   Macro command that deploys a new webapp
    #
    #   Requires `webapp_enable_insights` in deploy config file.
    #   Requires `azure_powerbi_group_id` in platform config file.
    #   Requires `deployment_name` in deploy config file.
    # Options:
    #   -h, --help                      Show this message and exit.
    ```

???+ abstract "Steps"
    - [babylon azure staticwebapp create](https://cosmo-tech.github.io/Babylon/latest/cli/#create_10)
    - [babylon azure staticwebapp custom-domain create](https://cosmo-tech.github.io/Babylon/latest/cli/#create_11) - Optional
    - [babylon azure ad app create](https://cosmo-tech.github.io/Babylon/latest/cli/#create_5)
    - [babylon azure ad group member add](https://cosmo-tech.github.io/Babylon/latest/cli/#add) - Optional
    - [babylon azure appinsight create](https://cosmo-tech.github.io/Babylon/latest/cli/#create_8) - Optional
    - [babylon webapp download](https://cosmo-tech.github.io/Babylon/latest/cli/#download_2)
    - [babylon webapp update-workflow](https://cosmo-tech.github.io/Babylon/latest/cli/#update-workflow)
    - [babylon webapp export-config](https://cosmo-tech.github.io/Babylon/latest/cli/#export-config)
    - [babylon azure ad app password create](https://cosmo-tech.github.io/Babylon/latest/cli/#create_6) - Optional
    - [babylon powerbi workspace user add](https://cosmo-tech.github.io/Babylon/latest/cli/#add_2) - Optional
    - [babylon azure staticwebapp app-settings update](https://cosmo-tech.github.io/Babylon/latest/cli/#update_5)
