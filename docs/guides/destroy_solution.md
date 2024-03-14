If you don't need a Cosmo Tech solution anymore, you can destroy it with all resources using 
`babylon destroy` command. It will automatically delete following resources:<br>
- scenarios and scenarioruns<br>
- datasets<br>
- adx database<br>
- event hub<br>
- azure function<br>
- powerbi workspace<br>
- workspace<br>
- run templates<br>
- solution<br>

By default, it will destroy resources referenced in state saved in namespace file, but you can define a specific state as option:

```bash
babylon destroy --state-to-destroy <path-to-specific-state>
```
