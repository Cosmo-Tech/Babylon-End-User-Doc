??? example "Organization.yaml"

      ```yaml
      kind: Organization
      namespace:
        remote: true   # false by default
        state_id: 8db6069e-e05f-42e6-b6d6-56dde124516a
        context: test
        platform:
          id: dev
          url: https://dev.api.cosmotech.com/phoenix/v3-0
      ```

The deployment configuration must define the following keys:

- **`kind`**  
  Specifies the type of resource to deploy.  
  Accepted values: `Organization`, `Solution`, `Workspace`, `WebApp`.  
  > ⚠️ The resource type must always start with a **capital letter**.

- **`namespace`**  
  Provides metadata that uniquely identifies the deployment, including:  
      - `state_id`  
      - `context_id`  
      - `platform_id`

- **`remote`**  
  A boolean flag indicating whether the state should be stored **locally only** (`false`, default) or **both locally and in the cloud** (`true`)

- **`spec`**  
  Defines the resource configuration. The details are specified under the **`payload`** section.  

For example, in an **Organization** deployment file:

??? example "Organization.yaml"

    ```yaml
    kind: Organization
    namespace:
      remote: true   # false by default
      state_id: 8db6069e-e05f-42e6-b6d6-56dde124516a
      context: test
      platform:
        id: dev
        url: https://dev.api.cosmotech.com/phoenix/v3-0
    spec:
      payload:
        name: My new Organization
        security: {{security}}

    ```

All keys in this file can be templated with `{{}}` syntax for objects and `"{{}}"` for strings, as `security` section of this file. Corresponding
values must be stored in `_variables.yaml_` file at the same level that your project See 👉 [Examples](../../Examples/Example_Deploy_CosmoTech_workspace.md):

```yaml
security:
  default: viewer
  accessControlList:
    - id: user1@email.com
      role: admin
    - id: user2@email.com
      role: editor
    - id: user3@email.com
      role: viewer
```