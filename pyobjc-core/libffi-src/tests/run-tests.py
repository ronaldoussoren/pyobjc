"""
'test' action for setup.py
"""
import glob
import os
import string
import sys
import unittest
from fnmatch import fnmatch
from os.path import basename, dirname, expanduser, join, splitext, walk

import dejagnu

deja_suite = dejagnu.testSuiteForDirectory("tests/testsuite/libffi.call")
suite = unittest.TestSuite((deja_suite,))
runner = unittest.TextTestRunner(verbosity=1)
runner.run(suite)
