The following command exists : `babylon config platform set-variable`

???+ info "Help of the command"
    ```bash
    babylon config platform set-variable --help
    # Usage: babylon config platform set-variable [OPTIONS] VARIABLE_KEY
    #                                             VARIABLE_VALUE
    #
    #   Set a platform variable with a new value
    #  
    # Options:
    #   -h, --help  Show this message and exit.
    ```

2 positional parameters are required : `VARIABLE_KEY` and `VARIABLE_VALUE`

???+ example "Set a first variable"
    ```bash
    babylon config platform set-variable VARIABLE_KEY VARIABLE_VALUE
    # Now our variable "VARIABLE_KEY" will have the value "VARIABLE_VALUE" in our config file, we can check it by displaying the config
    babylon config display
    ```
