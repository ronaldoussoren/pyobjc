#!/usr/bin/env python

import os
import sys

from macholib.util import is_platform_file

def check_file(path):
    if not os.path.exists(path):
        print >>sys.stderr, '%s: %s: No such file or directory' % (sys.argv[0], path)
        return 1
    try:
        is_plat = is_platform_file(path)
    except IOError:
        print >>sys.stderr, '%s: %s: Permission denied' % (sys.argv[0], path)
        return 1
    else:
        if is_plat:
            print path
    return 0

def main():
    args = sys.argv[1:]
    name = os.path.basename(sys.argv[0])
    err = 0
    if not args:
        raise SystemExit("usage: %s [dir ...]" % (name,))
    for base in args:
        if os.path.isdir(base):
            for root, dirs, files in os.walk(base):
                for fn in files:
                    err |= check_file(os.path.join(root, fn))
        else:
            err |= check_file(base)
    if err:
        raise SystemExit, 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
