# Dummy file to make this directory a package.
import unittest
import objc
import os
import gc
import subprocess

# Have a way to disable the autorelease pool behaviour
_usepool = not os.environ.get('PYOBJC_NO_AUTORELEASE')
_useleaks = bool(os.environ.get('PyOBJC_USE_LEAKS'))
_useleaks = False
_leaksVerbose = False

def leaks():
    data = subprocess.Popen(
            ['/usr/bin/leaks', str(os.getpid())], stdout=subprocess.PIPE
        ).communicate()[0]
    return data.splitlines()


_poolclass = objc.lookUpClass('NSAutoreleasePool')
class TestCase (unittest.TestCase):
    """
    A version of TestCase that wraps every test into its own
    autorelease pool.
    """
    def run(self, *args):
        if _useleaks:
            leaksBefore = leaks()
        if _usepool:
            p = _poolclass.alloc().init()
        else:
            p = 1

        try:
            unittest.TestCase.run(self, *args)
        finally:
            gc.collect()
            del p
            
            if _useleaks:
                leaksAfter = leaks()
                if len(leaksBefore) != len(leaksAfter):
                    print "\ntest %s is leaking [%d lines]"%(self, len(leaksAfter) - len(leaksBefore))
                    if _leaksVerbose:
                        # XXX: add a smartish filter the surpresses the leaks
                        # in leaksBefore.
                        for ln in leaksAfter:
                            print ln



main = unittest.main
