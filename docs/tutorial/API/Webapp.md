
To deploy a Cosmo Tech Web App now is possible with Babylon.

Babylon now supports deploying web applications using Terraform as backend. This integration allows you to provision and manage web app infrastructure as code directly through Babylon, streamlining the deployment process.

For more details on how to deploy the web app, refer to the README file in the Terraform web app module: 👉 [Terraform Module](https://github.com/Cosmo-Tech/terraform-webapp).

Babylon automatically clones the Terraform web app repository and updates the `terraform.tfvars` file with all required variables. These variables are retrieved from the `webapp.yaml` configuration file below.

!!! example "webapp.yaml"
    ```yaml
      kind: Webapp
      namespace:
         remote: true
      spec:
      payload:
         cloud_provider: "azure"
         cluster_name: "{{cluster_name}}"
         cluster_domain: "{{cluster_domain}}"
         tenant: "{{tenant}}"
         webapp_name: "{{webapp_name}}"
         organization_id: "{{services['api.organization_id']}}"
         azure_subscription_id: "{{azure_subscription_id}}"
         azure_entra_tenant_id: "{{azure_entra_tenant_id}}"
         powerbi_app_deploy: false
    ```