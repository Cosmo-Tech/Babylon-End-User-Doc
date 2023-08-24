# Azure requirements

!!! warning "Requirements"
    The following elements are required before you can use Babylon on an Azure subscription
    === "Platform requirements"
    --8<-- "docs/partials/azure/platform.md"

## App registration for Babylon CLI

Babylon uses a Service Principal to interact with the API and other resources. To do so, Babylon needs to be registered as an application in the Azure Active Directory.

The App registration will need rights on resources you will have to grant.

* **Microsoft Graph**
    - Application.ReadWrite.All
    - Application.ReadWrite.OwnedBy
    - Group.ReadWrite.All
    - User.Read
    - User.Read.All

* **Platform Api**
    - Platform.Admin