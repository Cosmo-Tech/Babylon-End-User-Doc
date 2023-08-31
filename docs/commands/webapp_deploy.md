---
hide:
- toc
---
# WebApp Deploy


## Configuration

!!! warning "Requirements"
    This macro requires a github repository with the destination branch already created
    
    1. [create a new repository](https://github.com/new) in Github
    3. configure your branch `<BRANCH>` with code source (e.g https://github.com/Cosmo-Tech/azure-sample-webapp.git)
    ```bash
      git init
      echo "# empty_webapp" >> README.md
      git add README.md
      git commit -m "first commit"
      git branch -M main
      git remote add origin git@github.com:<YOUR_GITHUB_REPOSITORY>.git
      git remote add upstream https://github.com/Cosmo-Tech/azure-sample-webapp.git
      git remote set-url upstream --push "NO"
      git fetch --all --prune
      git checkout -B <BRANCH> <SOURCE_TAG>
      rm -r .github/
      git add .; git commit -m 'first commit'
      git push origin <BRANCH> -f
    ```

## Description

The macro command will create a static webapp and configure it with the webapp source code.

This includes:

  - Creating and configuring an Azure Static WebApp resource
  - Creating and configuring an Azure Active Directory App Registration
  - Configuring the WebApp source code
  - Adding access to the PowerBI Workspace


!!! important "DNS Record"
    DNS Record creation is intently not supported by Babylon.  


## Macro command

!!! Macro
    ```bash
    babylon webapp -c <context_id> -p <platfom_id> deploy
    ```

!!! Usage
    ```bash
    # Usage: babylon webapp -c <context_id> -p <platform_id> deploy [OPTIONS]
    # 
    #  Macro command allowing deployment of new webapp.
    # 
    # Options:
    # --func-arm PATH  File with arm Azure Function deployment
    # --help           Show this message and exit.
    ```
