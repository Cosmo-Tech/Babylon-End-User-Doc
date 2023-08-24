---
hide:
- toc
---
# WebApp Deploy

## Description

The macro command will create a static webapp and configure it with the webapp source code.

This includes:

  - Creating and configuring an Azure Static WebApp resource
  - Creating and configuring an Azure Active Directory App Registration
  - Configuring the WebApp source code
  - Adding access to the PowerBI Workspace


!!! important "DNS Record"
    DNS Record creation is intently not supported by Babylon.  


## Configuration

!!! warning "Requirements"
    This macro requires a github repository with the destination branch already created.
    
    1. [create a new repository](https://github.com/new) in Github
    3. configure your branch `<BRANCH>` with code source (e.g https://github.com/Cosmo-Tech/azure-sample-webapp.git)
    
    ```bash
    git init
    ```

    ```bash
    echo "# empty_webapp" >> README.md
    ```
    
    ```bash
    git add README.md
    ```
    
    ```bash
    git commit -m "first commit"
    ```
    
    ```bash
    git branch -M <BRANCH>
    ```
    
    ```bash
    git remote add origin git@github.com:<YOUR_GITHUB_REPOSITORY>.git
    ```
    
    ```bash
    git remote add upstream https://github.com/Cosmo-Tech/azure-sample-webapp.git
    ```
    
    ```bash
    git remote set-url upstream --push "NO"
    ```
    
    ```bash
    git fetch --all --tags --prune
    ```
    
    ```bash
    git checkout -B <BRANCH> <SOURCE_TAG>
    ```
    
    ```bash
    rm -r .github/
    ```
    
    ```bash
    git add .; git commit -m 'first commit'
    ```
    
    ```bash
    git push origin <BRANCH> -f
    ```

## Macro command

!!! Macro
    ```bash
    babylon webapp deploy -c <context_id> -p <platfom_id> 
    ```

!!! Usage
    ```bash
    # Usage: babylon webapp deploy [OPTIONS]
    #
    #  Macro command that deploys a new webapp

    # Options:
    #   -c, --context TEXT   Context Name  [required]
    #   -p, --platform TEXT  Platform Name  [required]
    #   --arm-path PATH
    #   --help               Show this message and exit.
    ```
