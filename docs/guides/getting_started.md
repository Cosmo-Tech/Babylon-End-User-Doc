# :rocket: Getting started with Babylon

This is a guide to getting started with Babylon. You'll learn how to install, run, and experiment with the Babylon.

--8<-- 'docs/guides/az_requirements.md'

--8<-- 'docs/partials/installation/from_source.md'

Now that you have a fully functional installation of Babylon, you can check the next steps to learn how to start running commands.

## Setup Babylon


Babylon use a [Vault](https://www.vaultproject.io/) service and provides a group of commands that can be used.

The first thing to do in order to check if Babylon is working properly:
```bash
babylon --help
```

### Setup environment variables

The vault service is required to work with babylon cli.
Contact your babylon admin to get your **URI** service and your **userpass**.

* Set **URI** vault service.
  ```bash
  export BABYLON_SERVICE=<uri_babylon_vault_server>
  ```

  Now, you will need set some environment variables before interacting with Babylon cli.
  To do so, perform the login command.

* Login and get an access token.  
  ```bash
  babylon hvac login
  ```
  questions: 
  ```text
  [?] Username: <username>
  [?] Password: ****
  [?] Organization: <organization_name>
  ```
  Copy the response and paste it in your environment.

* If entries does not exist, you may need to create it (e.g. for a newly deployed platform):
  We provide a tool for this, you can find it [here](https://github.com/Cosmo-Tech/backend-tf-state-to-vault)
  This needs an initial Terraform deployment as it uses the Terraform state to parse and populate the Vault.
  Useful information can be found in the Readme of this repository !

### Configuration

At this point, you will need three variables to perform Babylon commands.

  - `context_id` : project name
  - `platform_id` : platform name
  - `state_id`: state name

`context_id` and `state_id` can be strings of your choice,
but they cannot contain special characters. `platform_id` represents the id of the platform, such as dev, staging, etc.
To initialize it, perform this command:
  ```bash
  babylon namespace use -c <context_id> -p <platform_id> -s <state_id>
  ```
It will be saved in a local file /home/.config/cosmotech/babylon/namespace.yaml

You can now test Babylon by performing a simple command, e.g.:
  ```bash
  babylon api organizations get-all
  ```
Initial configuration will be retrieved from vault and saved in Azure Storage
and in local file `/home/.config/cosmotech/babylon/state_id.yaml`


## State file specification

--8<-- 'docs/guides/resource_file.md'
