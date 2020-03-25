from cloudify import ctx
from cloudify import exceptions as cfy_exc
from cloudify.state import ctx_parameters as inputs
import time

if __name__ == '__main__':

    ctx.logger.info('sleep little bit')
    time.sleep(15)

    raise_failure = inputs.get('failure')
    if raise_failure == ctx.operation.name:
        if not ctx.instance.runtime_properties.get('failured'):
            ctx.instance.runtime_properties['failured'] = True
            raise cfy_exc.NonRecoverableError('Hey check, i am failure')
        else:
            ctx.logger.info("We alredy failured")
