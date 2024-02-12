# :rocket: Getting started with Babylon

This is a guide to getting started with Babylon. You'll learn how to install, run, and experiment with the Babylon.

--8<-- 'docs/guides/az_requirements.md'

--8<-- 'docs/partials/installation/from_source.md'

Now that you have a fully functional installation of Babylon, you can check the next steps to learn how to start running commands.

<br>

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

* If entries does not exist, you may need to create it (e.g for a newly deployed platform):
  We provide a tool for this, you can find it [here](https://github.com/Cosmo-Tech/backend-tf-state-to-vault)
  This needs an initial Terraform depoyment as it uses the Terraform state to parse and populate the Vault.
  Usefull informations can be found in the Readme of this repository !

### Configuration

At this point, you will need two variables to perform Babylon commands.

  - `context_id` : project name
  - `platform_id` : platform name

For example, you can try this command,

```bash
babylon config display -c brewery -p dev
```
You will see the current configuration. For now, this configuration is empty.

To retrieve `dev` configuration, you need perform this command.

```bash
babylon config init -c brewery -p dev
```

Try again the display command and verify the current configuration.


## Explore babylon

You will explore some basics commands. 

### Configuration files

```bash
# set email in azure config
babylon config set azure email example@test.com -c <context_id> -p dev
```
```bash
# get email in azure config
babylon config get azure email -c <context_id> -p dev
```

### Azure container registry and images

* ** Interact with Azure Container Registry ** 
!!! requirements
    * Docker instance
    * Vault service with `dev` and `staging` platform already configured 


1. Retrieve `dev` platform configuration
```bash
babylon config init -c <context_id> -p dev 
```

* Retrieve `staging` platform configuration
```bash
babylon config init -c <context_id> -p staging 
```

* List images from `dev` registry
```bash
babylon azure acr list -c <context_id> -p dev 
```

* Pull image from source : `dev` registry
```bash
babylon azure acr pull -c <context_id> -p dev --image <IMAGE:VERSION> 
```

* Push image to target : `staging` registry
```bash
babylon azure acr push -c <context_id> -p staging --image <IMAGE:VERSION>
```

## Config files specification

--8<-- 'docs/guides/resource_file.md'
