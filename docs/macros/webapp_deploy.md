## Behavior
`babylon webapp deploy` will create a static webapp and configure it with the sample webapp source code.
This includes:
- Creating and configuring an Azure Static WebApp resource
- Creating and configuring an Azure Active Directory App Registration
- Creating an Application Insights
- Configuring the Sample WebApp source code
- Adding access to the PowerBI Workspace

## Usage
```bash
Usage: babylon webapp deploy [OPTIONS]

  Macro command that deploys a new webapp

  Requires `webapp_enable_insights` in deploy config file.

  Requires `azure_powerbi_group_id` in platform config file.

  Requires `deployment_name` in deploy config file.

Options:
  -h, --help  Show this message and exit.
```

## Detailed steps
- [babylon azure staticwebapp create](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-azure-staticwebapp-create)
- [babylon azure staticwebapp custom-domain create](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-azure-staticwebapp-custom-domain-create) - Optional
- [babylon azure ad app create](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-azure-ad-app-create)
- [babylon azure ad group member add](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-azure-ad-group-member-add) - Optional
- [babylon azure appinsight create](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-azure-appinsight-create) - Optional
- [babylon webapp download](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-webapp-download)
- [babylon webapp update-workflow](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-webapp-update-workflow)
- [babylon webapp export-config](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-webapp-export-config)
- [babylon azure ad app password create](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-azure-ad-app-password-create) - Optional
- [babylon powerbi workspace user add](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-powerbi-workspace-user-add) - Optional
- [babylon azure staticwebapp app-settings update](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-azure-staticwebapp-app-settings-update)
