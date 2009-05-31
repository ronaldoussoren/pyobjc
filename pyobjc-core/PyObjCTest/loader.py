import sys, os, string, glob
from os.path import basename, dirname, splitext, join, expanduser, walk
from fnmatch import fnmatch
import unittest
import dejagnu

from distutils.command.install_lib import install_lib
from distutils.errors import DistutilsOptionError


def recursiveGlob(root, pathPattern):
    """
    Recursively look for files matching 'pathPattern'. Return a list
    of matching files/directories.
    """
    result = []

    def walker(data, dirname, files):
        for fn in files:
            if fnmatch(fn, data[0]):
                data[1].append(join(dirname, fn))

    walk(root, walker, (pathPattern, result))
    return result
        

def importExternalTestCases(pathPattern="test_*.py", root=".", package=None):
    """
    Import all unittests in the PyObjC tree starting at 'root'
    """

    testFiles = recursiveGlob(root, pathPattern)
    testModules = map(lambda x:x[len(root)+1:-3].replace('/', '.'), testFiles)
    if package is not None:
        testModules = [(package + '.' + m) for m in testModules]

    suites = []
   
    for modName in testModules:
        try:
            module = __import__(modName)
        except ImportError, msg:
            print "SKIP %s: %s"%(modName, msg)
            continue

        if '.' in modName:
            for elem in modName.split('.')[1:]:
                module = getattr(module, elem)

        s = unittest.defaultTestLoader.loadTestsFromModule(module)
        suites.append(s)

    return unittest.TestSuite(suites)



def makeTestSuite():
    topdir = dirname(dirname(__file__))
    deja_suite = dejagnu.testSuiteForDirectory(join(topdir,
        'libffi-src/tests/testsuite/libffi.call'))

    plain_suite = importExternalTestCases("test_*.py",
        join(topdir, 'PyObjCTest'), package='PyObjCTest')
        
    suite = unittest.TestSuite((plain_suite, deja_suite))

    # the libffi tests don't work unless we use our own
    # copy of libffi.
    import __main__
    if __main__.USE_SYSTEM_FFI:
        return plain_suite
    return suite
