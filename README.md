# cloudify-hooks-plugin

content for /opt/mgmtworker/config/hooks.conf

```yaml
hooks:
  - event_type: workflow_failed
    implementation: cloudify-hooks-plugin.cloudify_hooks.tasks.workflow_failed
    inputs:
      action: workflow_failed
    description: A test task for workflow_failed
```
