```bash
babylon init --project-folder devops --variables-file devops.yaml azure superset
```

```bash
    → Created directory: /home/user/CosmoTech/DevOps/babylon_v5_dir/devops
    ✔ Generated Build.yaml
    ✔ Generated Organization.yaml
    ✔ Generated Solution.yaml
    ✔ Generated Workspace_superset.yaml
    ✔ Generated Webapp.yaml (provider: azure)
    → Created directory: postgres/jobs
    ✔ Generated postgres/jobs/k8s_job.yaml
    ✔ Generated postgres/scripts/01_create_test_table.sql
    ✔ Generated postgres/scripts/02_seed_test_data.sql
    → Created directory: dashboard/superset
    ✔ Generated devops.yaml (provider: azure)
    ! Webapp directory not found
    → Cloning Terraform WebApp module (version 1.2.0)...
    ✔ Terraform WebApp module cloned at version 1.2.0

🚀 Project successfully initialized!
    Path: /home/user/CosmoTech/DevOps/babylon_v5_dir/devops

Next steps:
    1. Edit your variables in devops.yaml
    2. Run your first deployment command
```