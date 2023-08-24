# Getting started with Babylon

This is a guide to getting started with Babylon. You'll learn how to install, run, and experiment with the Babylon.

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
Contact your babylon admin to get your uri service and your userpass.

```bash
export BABYLON_SERVICE=<uri_babylon_vault_server>
```

Now, you will need set some environment variables before interacting with Babylon cli.
To do so, perform the login command.

```bash
babylon hvac login
```
questions: 
```text
[?] Username: <username>
[?] Password: ****
[?] Organization: <organization_name>`
```

Copy the response and paste it in your environment.


### Configuration

In this point, you will need two inputs to perform Babylon commands.

  - `context_id` : project name
  - `platform_id` : platform name

For example, you can try this command,

```bash
babylon config -c brewery -p dev display
```
You will see in your terminal the current configuration.

For now, this configuration is empty.

To initialize the configuration for `dev` platform, you need perform this command.

```bash
babylon config -c brewery -p dev select
```

Try again the display command and see the current configuration.


## Explore babylon


* ** Set and get configuration variables ** 
```bash
# set email in azure config
babylon config -c brewery -p dev set azure email example@test.com
```
```bash
# get email in azure config
babylon config -c brewery -p dev get azure email
```

<br>

* ** Interact with Azure Container Registry ** 
!!! requirements
    * Docker instance in your system
    * Vault service with `dev` and `staging` platform already configured 


1. Retrieve `dev` platform configuration
```bash
babylon config -c brewery -p dev select
```

* Retrieve `staging` platform configuration
```bash
babylon config -c brewery -p staging select
```

* Listing images in registry from `dev` platform
```bash
babylon azure -c brewery -p dev acr list
```

* Pull image from source : `dev` registry
```bash
babylon azure -c brewery -p dev acr pull -i brewery_simulator:0.0.26
```

* Push image to target : `staging` registry
```bash
babylon azure -c brewery -p staging acr push -i brewery_simulator:0.0.26
```

* Display current variables
```bash
babylon config -c brewery -p staging get acr simulator_repository
babylon config -c brewery -p staging get acr simulator_version
```