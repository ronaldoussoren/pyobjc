#!/usr/bin/env python
#
# Assemble all available unit tests from external modules
# into one suite. Slightly generalised from a similar tool
# included in the PyUnit distribution. Also suitable for
# GUI test runners.
#
# Dinu Gherman
#
# Some minor changes by Ronald Oussoren


import os
import sys
import glob
import unittest
from os.path import basename, dirname, splitext, join, expanduser, walk
from fnmatch import fnmatch

def recursiveGlob(root, pathPattern):
    result = []

    def walker(data, dirname, files):
        for fn in files:
            if fnmatch(fn, data[0]):
                data[1].append(join(dirname, fn))

    walk(root, walker, (pathPattern, result))
    return result
        


def importExternalTestCases(pathPattern="test_*.py", root="."):
    "Imports test cases from external files into the local namespace."

    testFiles = recursiveGlob(root, pathPattern)
    
    # import files and transfer TestCase instances into global namespace
    TC = unittest.TestCase
    for path in testFiles:
        sys.path.insert(0, dirname(path))
        modName = splitext(basename(path))[0]
        module = __import__(modName)
        items = module.__dict__.items()
        items = filter(lambda (k,v):type(v) == type(TC), items)
        items = filter(lambda (k,v):issubclass(v, TC), items)
        for k, v in items:
            globals()[k] = v
        del sys.path[0]


if __name__ == '__main__':
    # import tests, default root folder is the one of this file(!)
    args = sys.argv
    root = join(dirname(dirname(args[0])), "Lib")

    # overwrite with user-specific root folder, if provided
    if '-r' in args:
        root = args[args.index('-r') + 1]
    # import the tests
    importExternalTestCases("test_*.py", root)
    # please unittest
    del sys.argv[1:]
    # run tests
    unittest.main()

#else:
#    # GUI tools need to be told which root folder to use
#    importExternalTestCases("test_*.py", "~/Desktop/pyobjc")
