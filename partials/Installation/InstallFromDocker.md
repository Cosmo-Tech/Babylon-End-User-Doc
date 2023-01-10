## Get Babylon from docker

Choosing the version of Babylon you want to use you can run the following command (here for version `1.2.0`) 

=== "Download docker image"
    ```bash
    docker pull ghcr.io/cosmo-tech/babylon:1.2.0
    docker tag ghcr.io/cosmo-tech/babylon:1.2.0 babylon
    ```

It will download for you the required docker image, and rename it to `babylon`

=== "Start Babylon docker image"
    ```bash
    docker run -ti babylon
    ```