If you want you can set up a virtual environment in python using the library `venv` to keep your Babylon dependencies in a single location.
=== "Set up a `venv`"
    ```bash
    # Make sure you have the library venv installed
    pip install --user venv
    # Create a venv in the folder `.venv`
    python -m venv .venv
    ```
Now you can activate your venv (created in the folder `.venv`) and follow the rest of this tutorial.
=== "Activate on unix systems"
    ```bash
    source .venv/bin/activate
    ```
=== "Activate on windows (`cmd.exe`)"
    ```cmd
    .venv\Scripts\activate.bat
    ```
=== "Activate on windows (`PowerShell`)"
    ```PowerShell
    .venv\Scripts\Activate.ps1
    ```
!!! warning
    Once you install Babylon in a venv you will need to activate this venv every time you want to use Babylon.