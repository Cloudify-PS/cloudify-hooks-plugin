# cloudify-hooks-plugin

content for /opt/mgmtworker/config/hooks.conf

```yaml
hooks:
  - event_type: workflow_started
    implementation: cloudify-hooks-plugin.cloudify_hooks.tasks.workflow_started
    inputs:
      action: workflow_started
    description: A test task for workflow_started
  - event_type: workflow_succeeded
    implementation: cloudify-hooks-plugin.cloudify_hooks.tasks.workflow_succeeded
    inputs:
      action: workflow_succeeded
    description: A test task for workflow_succeeded
  - event_type: workflow_failed
    implementation: cloudify-hooks-plugin.cloudify_hooks.tasks.workflow_failed
    inputs:
      action: workflow_failed
    description: A test task for workflow_failed
  - event_type: workflow_cancelled
    implementation: cloudify-hooks-plugin.cloudify_hooks.tasks.workflow_cancelled
    inputs:
      action: workflow_cancelled
    description: A test task for workflow_cancelled
  - event_type: workflow_queued
    implementation: cloudify-hooks-plugin.cloudify_hooks.tasks.workflow_queued
    inputs:
      action: workflow_queued
    description: A test task for workflow_queued
```
