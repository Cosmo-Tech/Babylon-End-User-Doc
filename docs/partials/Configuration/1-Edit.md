The following command exists: `babylon config platform edit`

It will allow you to open your configuration file directly in a file editor.

???+ info "Help of the command"
    ```bash
    babylon config platform edit --help
    # <Usage: babylon config platform edit [OPTIONS] [PLATFORM]
    #
    # Open editor to edit variables in given platform
    #
    # will open default platform if no argument is passed
    #  
    # Options:
    #   -h, --help  Show this message and exit.
    ```

1 positional parameter is optional: `PLATFORM`

`PLATFORM` by the path to a platform file to open, if it is not present your current platform file will be opened.

???+ example "Set a first variable"
    Running the command will open a text editor of the file, you can then add the values you want to each keys
    ```bash
    babylon config platform edit
    ```
    ![Screenshot of nano with file content](../assets/PlatformConfigFileNano.png)