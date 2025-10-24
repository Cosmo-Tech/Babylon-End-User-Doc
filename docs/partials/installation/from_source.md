### **Get Babylon from source**

!!! warning "Requirements"
    --8<-- 'docs/partials/installation/prerequisites.md'

We will go through the process of getting a version of Babylon before the installation.

--8<-- 'docs/partials/installation/from_git.md'

## Install Babylon

You can install Babylon globally on your system:

!!! example 
    ```bash
    python3 -m venv ~/babylonenv
    source ~/babylonenv/bin/activate
    pip install .
    ```
Alternatively, follow these steps if you want to install Babylon in development mode:

!!! example 
    ```bash
    python3 -m venv ~/babylonenv
    source ~/babylonenv/bin/activate
    pip install -e .
    ```
