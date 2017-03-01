#!/usr/bin/env python
# Copyright 2017, Major Hayden <major@mhtx.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Base monitoring class."""

import platform

import click

from monitorstack.cli import pass_context


@click.command('uptime', short_help='Get system uptime')
@pass_context
def cli(ctx):
    """Get system uptime."""
    with open('/proc/uptime', 'r') as f:
        output = f.read()
    uptime = output.split()[0]
    output = {
        'exit_code': 0,
        'message': 'uptime is ok',
        'measurement_name': 'system_uptime',
        'meta': {
            'platform': platform.platform()
        },
        'variables': {
            'uptime': uptime
        }
    }
    return output
