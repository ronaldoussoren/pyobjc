"""
'test' action for setup.py
"""
# XXX - use setuptools test suite support
import sys, os, string, glob
from os.path import basename, dirname, splitext, join, expanduser, walk
from fnmatch import fnmatch
import unittest
import dejagnu

deja_suite = dejagnu.testSuiteForDirectory('tests/testsuite/libffi.call')
suite = unittest.TestSuite((deja_suite, ))
runner = unittest.TextTestRunner(verbosity=1)
runner.run(suite)
