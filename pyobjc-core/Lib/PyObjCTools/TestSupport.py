"""
Helper code for implementing unittests.

This module is unsupported and is primairily used in the PyObjC
testsuite.
"""
import plistlib as _pl
import unittest as _unittest
import objc
import os as _os
import gc as _gc
import subprocess as _subprocess

# Have a way to disable the autorelease pool behaviour
_usepool = not _os.environ.get('PYOBJC_NO_AUTORELEASE')
_useleaks = bool(_os.environ.get('PyOBJC_USE_LEAKS'))
_useleaks = False
_leaksVerbose = False

_os_release = None
def os_release():
    """
    Returns '10.5' on all releases of Leopard, simularly for other
    major releases.
    """
    global _os_release
    if _os_release is not None:
        return _os_release

    pl = _pl.readPlist('/System/Library/CoreServices/SystemVersion.plist')
    v = pl['ProductVersion']
    return '.'.join(v.split('.')[:2])


def min_os_level(release):
    """
    Usage::

        class Tests (unittest.TestCase):

            @min_os_level('10.6')
            def testSnowLeopardCode(self):
                pass
    """
    if os_release() >= release:
        def decorator(function):
            return function

    else:
        def decorator(function):
            def result(self):
                pass

            result.func_name = function.func_name
            return result





def _leaks():
    data = _subprocess.Popen(
            ['/usr/bin/leaks', str(_os.getpid())], stdout=_subprocess.PIPE
        ).communicate()[0]
    return data.splitlines()


_poolclass = objc.lookUpClass('NSAutoreleasePool')

class TestCase (_unittest.TestCase):
    """
    A version of TestCase that wraps every test into its own
    autorelease pool.

    This also adds a number of useful assertion methods
    """
    def failUnlessIsInstance(self, value, types, message=None):
        self.failUnless(isinstance(value, types), message)

    def failIfIsInstance(self, value, types, message=None):
        self.failUnless(isinstance(value, types), message)

    assertIsInstance = failUnlessIsInstance

    if not hasattr(_unittest.TestCase, "assertAlmostEquals"):
        def assertAlmostEquals(self, val1, val2, message=None):
            self.failUnless(abs (val1 - val2) < 0.00001, message)



    def run(self, *args):
        if _useleaks:
            leaksBefore = _leaks()
        if _usepool:
            p = _poolclass.alloc().init()
        else:
            p = 1

        try:
            _unittest.TestCase.run(self, *args)
        finally:
            _gc.collect()
            del p
            _gc.collect()
            
            if _useleaks:
                leaksAfter = _leaks()
                if len(leaksBefore) != len(leaksAfter):
                    print "\ntest %s is leaking [%d lines]"%(self, len(leaksAfter) - len(leaksBefore))
                    if _leaksVerbose:
                        # XXX: add a smartish filter the surpresses the leaks
                        # in leaksBefore.
                        for ln in leaksAfter:
                            print ln

main = _unittest.main
