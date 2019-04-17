#   Author: Jeet Parmar
#   Email: jeet@coupa.com
#   Created: Wed Apr 17 12:36:38 IST 2019

from __future__ import print_function

import argparse
import sys
from subprocess import call

from pre_commit_hooks.util import parse_command


def check_cookstyle(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='chef files to check with cookstyles')
    parser.add_argument(
        '--exe',
        type=parse_command,
        default='cookstyle',
        help='cookstyle executable',
    )
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:  # pragma: no cover
        if filename[-3:] == '.rb':
            if call([args.exe, '-a', '-D', filename]) != 0:
                print('{}: Failed to run cookstyle.'.format(filename))
                retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(check_cookstyle())
