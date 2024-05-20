# SPDX-FileCopyrightText: 2024-present Laurent LAPORTE <laurent.laporte.pro@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from python_deep_dive.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="python-deep-dive")
def python_deep_dive():
    click.echo("Hello world!")
