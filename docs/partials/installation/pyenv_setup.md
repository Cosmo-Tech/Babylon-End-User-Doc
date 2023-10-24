
* Setup a `pyenv`

    **Automatic installer**
    
    ```bash
    curl https://pyenv.run | bash
    ```

    **Setup your shell environment for pyenv**

    ```bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    source ~/.bashrc
    ```

    **Now you can create a venv with `pyenv`**
    ```bash
    pyenv virtualenv <babylon_env_name>
    ```

    **Activate your new venv**
    ```bash
    pyenv activate <babylon_env_name>
    ```