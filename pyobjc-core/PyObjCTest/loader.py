import sys, os, string, glob
from os.path import basename, dirname, splitext, join, expanduser
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

    for rootpath, dirnames, filenames in os.walk(root):
        for fn in filenames:
            if fnmatch(fn, pathPattern):
                result.append(join(rootpath, fn))
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
    import __main__
    topdir = dirname(__main__.__file__)
    if sys.version_info[0] == 3:
        del sys.path[1]
        deja_topdir = dirname(dirname(topdir))
    else:
        deja_topdir = topdir
    deja_suite = dejagnu.testSuiteForDirectory(join(deja_topdir,
        'libffi-src/tests/testsuite/libffi.call'))

    plain_suite = importExternalTestCases("test_*.py",
        join(topdir, 'PyObjCTest'), package='PyObjCTest')

    version_suite = importExternalTestCases("test%d_*.py"%(sys.version_info[0],),
        join(topdir, 'PyObjCTest'), package='PyObjCTest')
        
    suite = unittest.TestSuite((plain_suite, version_suite, deja_suite))

    # the libffi tests don't work unless we use our own
    # copy of libffi.
    import __main__
    if __main__.USE_SYSTEM_FFI:
        return unittest.TestSuite((plain_suite, version_suite))
    return suite
