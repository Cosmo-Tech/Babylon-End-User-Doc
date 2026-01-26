### **Get Babylon from source**

!!! warning "Requirements"
    --8<-- 'docs/partials/installation/prerequisites.md'

We will go through the process of getting a version of Babylon before the installation.

--8<-- 'docs/partials/installation/from_git.md'

## Install Babylon
There are two ways to install Babylon: using **uv** or using **venv**. Currently, the recommended method is **uv**.<br>
You can follow the official instructions here: [UV Installation Guide](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1).


You can install Babylon globally on your system:

!!! uv example

    === "🖥️ Windows"
        After the installation of **uv**, it is highly recommended to reopen a new terminal window!
        ```bash
        uv venv .venv
        .\.venv\Scripts\activate
        uv pip install .
        ```
    === "🐧 Linux"

        ```bash
        uv .venv
        source .venv/bin/activate
        uv pip install .
        ```

!!! py example 

    === "🖥️ Windows"

        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        pip install .
        ```
    === "🐧 Linux"
    
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        pip install .
        ```
Alternatively, follow these steps if you want to install Babylon in development mode:

!!! uv example
    ```bash
    uv pip install -e . --group dev
    ```

!!! py example
    ```bash
    pip install -e .
    ```
