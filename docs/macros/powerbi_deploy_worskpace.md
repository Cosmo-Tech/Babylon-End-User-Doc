## Behavior
`babylon powerbi deploy-workspace` will deploy a PowerBI workspace and populate it with reports
This includes:
- Creating a PowerBI workspace
- Uploading all reports from a folder
- Updating dataset parameters
- Updating dataset azure credentials

## Usage
```bash
Usage: babylon powerbi deploy-workspace [OPTIONS] WORKSPACE_NAME

  Macro command allowing full deployment of a power bi workspace

  Require a local folder named `powerbi-reports` and will initialize a full
  workspace with the given reports

Options:
  -f, --report-folder DIRECTORY   Override folder containing your .pbix files
  -p, --report-parameter <QUERYSTRING QUERYSTRING>...
                                  Add a combination <Key Value> that will be
                                  sent as parameter to all your datasets
  -h, --help                      Show this message and exit.
```

## Detailed steps
- [babylon powerbi workspace create](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-powerbi-workspace-create)
- [babylon powerbi report upload](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-powerbi-report-upload)
- [babylon powerbi dataset parameters update](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-powerbi-dataset-parameters-update)
- [babylon powerbi dataset update-credentials](https://cosmo-tech.github.io/Babylon/latest/cli/#babylon-powerbi-dataset-update-credentials)
