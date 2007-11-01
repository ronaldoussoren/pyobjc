"""
This is the runner for the tests defined in Modules/objc/unittest.m. Those tests
check a number lowlevel features of the bridge.

This file provides a nice unittest wrapper around the functions in that file,
the code in this file defines a class CTests that has the functions in the
unitest.m file as its methods.
"""
import objc.test, sys, platform
from  objc.test import ctests

names = [ x for x in dir (ctests) if not x.startswith('_') ]
methods = {}


def make_test(name):
    """
    Create a method for use in a unittest, the exec is needed to get the
    proper function name
    """
    result = { 'meth': getattr(ctests, name) }

    if sys.platform == 'darwin' and name == 'CheckNSInvoke' and platform.machine() == 'Power Macintosh':
        # There is a bug in Apple's implementation of NSInvocation
        # surpress the test failure until Apple fixes the class.
        # Don't change the C-code, the same function is used to disable
        # parts of the unittests that trigger the bug.
        def test_CheckNSInvoke(self):
            try:
                ctests.CheckNSInvoke()
            except AssertionError:
                return

            raise AssertionError, "NSInvocation works!"

        return test_CheckNSInvoke

    exec  """\
def test_%s(self):
    meth()
"""%(name,) in result

    return result['test_%s'%(name,)]


for n in names:
    methods['test_%s'%(n,)] = make_test(n)

CTests = type(objc.test.TestCase)('CTests', (objc.test.TestCase,), methods)

if __name__ == "__main__":
    objc.test.main()
