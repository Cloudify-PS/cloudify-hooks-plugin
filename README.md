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
Or use precreated [wagon](https://github.com/Cloudify-PS/cloudify-hooks-plugin/releases/download/1.0.0/cloudify_hooks_plugin-1.0.0-py27-none-linux_x86_64-centos-Core.wgn)
and [plugin.yaml](https://github.com/Cloudify-PS/cloudify-hooks-plugin/releases/download/1.0.0/plugin.yaml).
* check that all deployments with `autouninstall` prefix uninstalled.
```shell
# will be uninstalled after install
cfy install cloudify_hooks/examples/check-failure.yaml -b autouninstall_check1
# will save alive as deployments is not failed
cfy install cloudify_hooks/examples/check-failure.yaml -b autouninstall_check2 -i raise_failure_first=ignore_action
# will be stay failed
cfy install cloudify_hooks/examples/check-failure.yaml -b noprefix_check3
```
