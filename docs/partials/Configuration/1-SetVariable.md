The following command exists: `babylon config set-variable [platform|deploy|secrets]`

???+ info "Help of the command"
    ```bash
    # Usage: babylon config set-variable [OPTIONS] {deploy|platform|secrets} KEY
                                   VALUE
    # Set a configuration variable
    # Options:
    #    --help  Show this message and exit.
    ```

2 positional parameters are required: `KEY` and `VALUE`

???+ example "Set a first variable"
    ```bash
    babylon config set-variable platform VARIABLE_KEY VARIABLE_VALUE
    # Now our variable "VARIABLE_KEY" will have the value "VARIABLE_VALUE" in our platform config file, we can check it by displaying the config
    babylon config display
    ```
