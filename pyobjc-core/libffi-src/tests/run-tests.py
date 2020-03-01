"""
'test' action for setup.py
"""
import unittest

import dejagnu

deja_suite = dejagnu.testSuiteForDirectory("tests/testsuite/libffi.call")
suite = unittest.TestSuite((deja_suite,))
runner = unittest.TextTestRunner(verbosity=1)
runner.run(suite)
