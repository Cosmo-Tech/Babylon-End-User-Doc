## Azure requirements


!!! warning "Requirements"
    The following elements are required before you can use Babylon on an Azure subscription

    * **Fully set up Cosmo Tech Platform installed on your Azure Tenant**

    * **App registration for Babylon**

    Babylon uses a Service Principal to interact with the API and other resources. To do so, Babylon needs to be registered as an application in the Azure Active Directory.

    This App Registration will be used to authenticate and get the required tokens to connect to your Platform. Rights on the App Registration depends on the type of connection you want to make. 
    
    We recommend defining this app registration as a mobile and desktop application in Azure configuration with redirection URL (mostly for authenticating against Azure services.
    
    See official documentation :
    
        * https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow
        * https://learn.microsoft.com/en-us/entra/identity-platform/msal-client-application-configuration
        * https://learn.microsoft.com/en-us/onedrive/developer/rest-api/getting-started/msa-oauth?view=odsp-graph-online

    The App registration needs the following API permissions:

    !!! tip "API Permissions"
        **Microsoft Graph**  
        🔹 Application.ReadWrite.All *(Application)*  
        🔹 Application.ReadWrite.OwnedBy *(Application)*  
        🔹 Group.ReadWrite.All *(Delegated)*  
        🔹 User.Read *(Delegated)*  

        **Platform API**  
        🔹 Platform.Admin *(Application)*  



    For those concerned with specifics Azure policies, all Microsoft Graph's permissions can be deleted excepted User.Read (Delegated), but this implies that some operations would be handled manually. The platform API permission is mandatory.


    !!! important
        Babylon App registration needs at least **Contributor** role on Cosmo Tech Platform Resource Group.

