"""
This is the runner for the tests defined in Modules/objc/unittest.m. Those tests
check a number lowlevel features of the bridge.

This file provides a nice unittest wrapper around the functions in that file,
the code in this file defines a class CTests that has the functions in the
unitest.m file as its methods.
"""
import unittest
from  objc.test import ctests

names = [ x for x in dir (ctests) if not x.startswith('_') ]
methods = {}


def make_test(name):
    """
    Create a method for use in a unittest, the exec is needed to get the
    proper function name
    """
    result = { 'meth': getattr(ctests, name) }
    exec  """\
def test_%s(self):
    meth()
"""%(name,) in result

    return result['test_%s'%(name,)]


for n in names:
    methods['test_%s'%(n,)] = make_test(n)

CTests = type(unittest.TestCase)('CTests', (unittest.TestCase,), methods)

if __name__ == "__main__":
    unittest.main()
