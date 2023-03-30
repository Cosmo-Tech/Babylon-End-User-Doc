# Terraform Cloud Requirements

???+ warning "Requirements"
    The following elements are required before you can use Babylon on Terraform Cloud  
     - A Terraform Cloud organization token, for workspace creation or configuration  
     - A Terraform Cloud user token, for workspace configuration or execution

## Allow access to Terraform Cloud
Babylon uses the Terraform Cloud tokens to authenticate users and allow them to interact with the API.  
For operation on workspaces you will need to [add a oauth token](https://developer.hashicorp.com/terraform/tutorials/cloud/github-oauth) to terraform-cloud in the webapp.  
Once this oauth token you will add its id to your workspace configuration with babylon.  
- [babylon terraform-cloud workspace create](https://cosmo-tech.github.io/Babylon/2.1.0/cli/#create_16)


You can use the following commands to setup your token secrets in your `.secrets.yaml.encrypt` file for `Babylon` to use it directly !  
  - [babylon terraform-cloud login](https://cosmo-tech.github.io/Babylon/latest/cli/#login_1)  
  - [babylon terraform-cloud logout](https://cosmo-tech.github.io/Babylon/latest/cli/#logout_1)  
