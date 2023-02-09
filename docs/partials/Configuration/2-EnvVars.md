You can use the following environment variable to replace your default configuration folder by a custom one: `BABYLON_CONFIG_DIRECTORY`

By setting that value to an absolute path you will access it wherever you are in your system, 
but if you want to keep a simple configuration change depending on the folder where you are, 
you can instead set it to a relative path, 
which will allow you to change your configuration everytime you move to another folder.

???+ tip "use `direnv`"
    You can use tools like [![direnv](https://img.shields.io/badge/direnv-%23121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/direnv/direnv) to set alternate values for your envvar and easily switch while moving around folders