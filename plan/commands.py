# -*- coding: utf-8 -*-
"""
    plan.commands
    ~~~~~~~~~~~~~

    Command line tools for Plan.

    :copyright: (c) 2014 by Shipeng Feng.
    :license: BSD, see LICENSE for more details.
"""
import os

import click


class Echo(object):
    """Echo class for Plan.  This is used to echo some common used content
    type in the command line.
    """
    
    @classmethod
    def echo(cls, message):
        click.echo(message)

    @classmethod
    def message(cls, message):
        self.echo("[message] %s" % message)

    @classmethod
    def write(cls, message):
        self.echo("[write] %s" % message)

    @classmethod
    def fail(cls, message):
        self.echo("[fail] %s" % message)

    @classmethod
    def add(cls, message):
        self.echo("[add] %s" % message)

    @classmethod
    def done(cls):
        self.echo("[done]!")


SCHEDULE_TEMPLATE = """\
# Use this file to easily define all of your cron jobs.
#
# It's helpful to understand cron before proceeding.
# http://en.wikipedia.org/wiki/Cron

# Example:
#
# pass

# Learn more: http://github.com/fengsp/plan
"""


@click.command()
@click.option('--path', default='./schedule.py', type=click.File('wb'), 
                           help='The filepath for your schedule file.')
def quickstart(path):
    """plan-quickstart"""
    write = True
    if os.path.isfile(path.name):
        write = click.confirm("'%s' already exists, override?" % path.name)
    if write:
        Echo.add("writing '%s'" % path.name)
        path.write(SCHEDULE_TEMPLATE)
        Echo.done()


def prompt_choices(name, choices):
    """One wrapper function for click.prompt to show choices to the user.
    """
    return click.prompt(name + ' - (%s)' % ', '.join(choices), 
                      type=click.Choice(choices), default=choices[0])


if __name__ == "__main__":
    quickstart()