---
description: Example from scratch for Updating a Cosmo Tech workspace with best practice
---

# Update Cosmo Tech workspace 

!!! abstract "Remember"
    we assumed that the workspace already deployed we need just to update some configuration so this guide we show beast practic to do this with all use cases!

## :material-folder: Modifying Access Control Lists in API Objects

Assuming you need to add users to the access control lists for the **Organization**, **Solution**, and **Workspace**, here is how you can do it:

Go to the workspace repository, open the project, and then edit the `variables.yaml` file.  
In this example, we add users `Alice.Alice.@email.com` and `Bob.Bob@email.com`.

!!! example "variables.yaml"

    ```yaml
    organization_security:
      default: none
      accessControlList:
        - id: admin.user@example.com
          role: admin
        - id: editor.user@example.com
          role: editor
        - id: viewer.user@example.com
          role: viewer
        - id: alice.alice.@email.com   # add Alice user as editor
          role: editor
        - id: bob.bob@email.com    # add Bob user as viewer
          role: viewer

    solution_security:
      default: none
      accessControlList:
        - id: admin.user@example.com
          role: admin
        - id: editor.user@example.com
          role: editor
        - id: viewer.user@example.com
          role: viewer
        - id: alice.alice.@email.com   # add Alice user as editor
          role: editor
        - id: bob.bob@email.com    # add Bob user as viewer
          role: viewer

    workspace_security:
      default: none
      accessControlList:
        - id: admin.user@example.com
          role: admin
        - id: editor.user@example.com
          role: editor
        - id: viewer.user@example.com
          role: viewer
        - id: alice.alice.@email.com   # add Alice user as editor
          role: editor
        - id: bob.bob@email.com   # add Bob user as viewer
          role: viewer
    ```

## :material-console: Applying Babylon Commands

After making the necessary modifications, you can now apply the changes using Babylon commands.

!!! example "Babylon Apply"

    ```bash
    source .venv/bin/activate
    ```
    ```bash
    babylon namespace use -c test -t dev -s 73a90433
    ```
    ```bash
    babylon apply --organization --var-file variables.yaml project/
    ```
    ```bash
    babylon apply --solution --var-file variables.yaml project/
    ```
    ```bash
    babylon apply --workspace --var-file variables.yaml project/
    ```