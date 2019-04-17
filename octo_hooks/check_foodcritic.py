#   Author: Jeet Parmar
#   Email: jeet@coupa.com
#   Created: Wed Apr 17 3:36:38 IST 2019

from __future__ import print_function

import argparse
import sys
from subprocess import call

from octo_hooks.util import parse_command


def check_foodcritic(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Cookbook path to check.')
    parser.add_argument(
        '--exe',
        type=parse_command,
        default='foodcritic',
        help='foodcritic executable',
    )
    args = parser.parse_args(argv)

    retval = 0
    if len(args.filenames):  # pragma: no cover
        if call([args.exe, '--epic-fail', 'any', '.']) != 0:
            print('Failed to run foodcritic for cookbook.')
            retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(check_foodcritic())
