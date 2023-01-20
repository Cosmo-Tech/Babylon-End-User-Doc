By running the following command you can see a lot of information
=== "Config display"
    ```bash
    babylon --bare config display
    # Configuration:
    #   dir: /home/user/.config/babylon
    #   deployment: /home/user/.config/babylon/deployments/deploy.yaml
    #       ...
    #  platform: /home/user/.config/babylon/platforms/platform.yaml
    #       ...
    #  plugins: 
    ```
Here we will focus on one line : `platform: /home/user/.config/babylon/platforms/platform.yaml`

This is the path to your local config file for your platform. You can just open it using you favorite text editor to be able to update your configuration values.