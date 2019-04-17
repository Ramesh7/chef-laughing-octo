#   Author: Jeet Parmar
#   Email: jeet@coupa.com
#   Created: Wed Apr 17 6:36:38 IST 2019

from __future__ import print_function

import argparse
import sys
from subprocess import call

from octo_hooks.util import parse_command


def check_rspec(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='ruby files to check.')
    parser.add_argument(
        '--exe',
        type=parse_command,
        default='rspec',
        help='rspec executable.',
    )
    args = parser.parse_args(argv)

    retval = 0
    specs_to_run = []
    for filename in args.filenames:
        if filename[-3:] == '.rb' and filename[:8] == 'recipes/':
            specs_to_run.append('spec/unit/recipes/{}_spec.rb'.format(filename[8:-3]))
        if filename[-3:] == '.rb' and filename[:18] == 'spec/unit/recipes/':
            specs_to_run.append(filename)
    if len(specs_to_run) and call([args.exe] + list(set(specs_to_run))) != 0:
        print('Failed to run rspec for a chef recipe.')
        retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(check_rspec())
