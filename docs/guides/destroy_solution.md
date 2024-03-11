If you don't need a solution anymore, you can destroy it with all resources using 
`babylon destroy` command. It will automatically delete following resources:
- scenarios and scenarioruns
- datasets
- adx database
- event hub
- azure function
- powerbi workspace
- workspace
- run templates
- solution

By default, it will destroy the state saved in namespace file, but you can define a specific state as option:

```bash
babylon destroy --state-to-destroy <path-to-specific-state>
```
