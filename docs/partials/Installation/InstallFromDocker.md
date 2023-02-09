## Get Babylon from docker

???+ warning "Prerequisites"
    | Requirement     | <!-- -->                                                                                                                                             |
    |-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **Docker**      | [![Install docker](https://img.shields.io/badge/Docker-3776AB?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/get-docker//)|


Choosing the version of Babylon you want to use you can run the following command (here for version `1.2.0`) 

???+ example "Download docker image"
    ```bash
    docker pull ghcr.io/cosmo-tech/babylon:1.2.0
    docker tag ghcr.io/cosmo-tech/babylon:1.2.0 babylon
    ```

It will download for you the required docker image, and rename it to `babylon`

???+ example "Start Babylon docker image"
    Using the following command you get in a working Babylon environment, allowing you to run any command you will like
    ```bash
    docker run -ti --rm babylon
    ```

    !!! warning
        **In this environment your changes to the files won't be persisted when you leave it.**  
        The following tips will help you set up persitance for your config, but will use knowledge of Babylon explained in future guides.

???+ tip "Persist configurations and use local content as a working dir"
    ???+ info
        This tip concern some principle of Babylon explained is other guides, you can skip it for now if you want to understand those principles before running commands using them.

    To persist configuration we will use the `--mount` option of Docker to persist our data across runs
    
    === "Persist configuration"
        ```bash
        mkdir babylon_config
        docker run -ti --rm --mount type=bind,source="$(pwd)"/babylon_config,target=/opt/babylon babylon
        ```
    This command will persist your Babylon configuration in a local `/babylon_config` folder allowing you to keep it across runs (in the same folder)

    Now if you want to use your local files as a working directory for your commands you can do the following

    === "Use local folder as working dir"
        ```bash
        docker run -ti --rm --mount type=bind,source="$(pwd)",target=/etc/babylon/workingdir babylon
        ```
    This command will use your current folder as a working directory for your babylon commands

    Combining both options allows for a persistent content and config across runs
    
    === "Combine both for persitence"
        ```bash
        docker run -ti --rm --mount type=bind,source="$(pwd)"/babylon_config,target=/opt/babylon --mount type=bind,source="$(pwd)",target=/etc/babylon/workingdir babylon
        ```

??? tip "Use aliases to make a babylon command using docker"
    !!! info
        * Only work on system having the `alias` command
        * Won't allow you to use auto-completion

    The following command will create a command `babylon` having the same use as the one you would get by installing the sources but by using docker.

    === "`babylon` alias command"
    ```bash
    alias babylon="docker run -ti --rm --mount type=bind,source=$(pwd)/babylon_config,target=/opt/babylon --mount type=bind,source=$(pwd),target=/etc/babylon/workingdir --entrypoint babylon babylon"
    ```