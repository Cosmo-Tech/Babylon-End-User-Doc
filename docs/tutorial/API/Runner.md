This is how the runner deployment file is structured

!!! example "Runner.yaml"

    ```yaml
    kind: Runner
    namespace:
      remote: true   # false by default
    spec:
      sidecars:
      payload:
        id: # mandatory if you want to launch an update, without id a new dataset will be created ; if you want a new dataset, leave this field empty
        name: "{{runner_name}}"
        runTemplateId: "{{run_template_id}}"
        solutionId: "{{services['api.solution_id']}}"
        solutionName: "{{solution_name}}"
        runTemplateName: "{{runTemplate_name}}"
        ownerName: "{{owner_name}}"
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