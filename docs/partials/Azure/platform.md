You need to have a fully set up Cosmo Tech Platform installed on your Azure Tenant.

To help you with the installation you can look at the following course on Allbound  
[![Deploy Managed App](https://img.shields.io/badge/Deploy_Managed_App-3776AB?style=for-the-badge)](https://cosmotech.allbound.com/learn/deploy-my-cosmo-tech-managed-application-from-microsoft-azure-marketplace/)

You need an App Registration on your Azure Tenant. This App Registration will be used to authenticate and get the required tokens to connect to your Platform.   
Rights on the App Registration depends on the type of connection you want to make.
  - For the API you will need delegate rights on the Cosmotech API App.
  - For Azure Container Registry you will need read and write rights on the Azure Container Registry.