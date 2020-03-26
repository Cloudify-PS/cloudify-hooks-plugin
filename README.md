# cloudify-hooks-plugin

Way to reproduce:
* Add such event handler to `/opt/mgmtworker/config/hooks.conf`
[Look to documentation for more information](https://docs.cloudify.co/5.0.5/working_with/manager/actionable-events/).
```yaml
hooks:
- event_type: workflow_failed
  implementation: cloudify-hooks-plugin.cloudify_hooks.tasks.workflow_failed
  description: A hook for workflow_failed
```
* build wagon and install to your manager.
[Look to documentation for more information](https://docs.cloudify.co/5.0.5/developer/writing_plugins/packaging-your-plugin/).
* check that all deployments with `autouninstall` prefix uninstalled.
```shell

```
