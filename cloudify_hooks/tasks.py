########
# Copyright (c) 2014-2020 Cloudify Platform Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from cloudify import ctx
from cloudify import manager
from cloudify.decorators import workflow


# callback name from hooks config
@workflow
def workflow_failed(inputs, *args, **kwargs):
    # get current context
    _ctx = kwargs.get('ctx', ctx)

    # dump current parameters
    _ctx.logger.info("called: {}/{}/{}"
                     .format(repr(inputs), repr(args), repr(kwargs)))

    # get client from current manager
    client = manager.get_rest_client()

    if (
        # prefix of deployments for uninstall
        inputs.get('deployment_id').startswith('autouninstall') and
        # if workflow is install
        inputs.get('workflow_id') == 'install'
    ):
        # mark that we going to uninstall to logs
        _ctx.logger.info("Going to uninstall {}"
                         .format(inputs.get('deployment_id')))
        # send uninstall event
        client.executions.start(inputs.get('deployment_id'), 'uninstall')
