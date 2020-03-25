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
import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('/tmp/hooks.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


def workflow_started(inputs, *args, **kwargs):
    logger.info("called: {}/{}/{}".format(repr(inputs), repr(args), repr(kwargs)))


def workflow_succeeded(inputs, *args, **kwargs):
    logger.info("called: {}/{}/{}".format(repr(inputs), repr(args), repr(kwargs)))


def workflow_failed(inputs, *args, **kwargs):
    logger.info("called: {}/{}/{}".format(repr(inputs), repr(args), repr(kwargs)))


def workflow_cancelled(inputs, *args, **kwargs):
    logger.info("called: {}/{}/{}".format(repr(inputs), repr(args), repr(kwargs)))


def workflow_queued(inputs, *args, **kwargs):
    logger.info("called: {}/{}/{}".format(repr(inputs), repr(args), repr(kwargs)))
