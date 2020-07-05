import os
import unittest
from fnmatch import fnmatch
from os.path import dirname, join

from . import dejagnu


def recursiveGlob(root, pathPattern):
    """
    Recursively look for files matching 'pathPattern'. Return a list
    of matching files/directories.
    """
    result = []

    for rootpath, _dirnames, filenames in os.walk(root):
        for fn in filenames:
            if fnmatch(fn, pathPattern):
                result.append(join(rootpath, fn))
    return result


def importExternalTestCases(pathPattern="test_*.py", root=".", package=None):
    """
    Import all unittests in the PyObjC tree starting at 'root'
    """

    testFiles = recursiveGlob(root, pathPattern)
    testModules = [x[len(root) + 1 : -3].replace("/", ".") for x in testFiles]
    if package is not None:
        testModules = [(package + "." + m) for m in testModules]

    suites = []

    for modName in testModules:
        try:
            module = __import__(modName)
        except ImportError as msg:
            print("SKIP %s: %s" % (modName, msg))
            continue

        if "." in modName:
            for elem in modName.split(".")[1:]:
                module = getattr(module, elem)

        s = unittest.defaultTestLoader.loadTestsFromModule(module)
        suites.append(s)

    return unittest.TestSuite(suites)


def makeTestSuite(use_system_libffi):
    use_system_libffi = True
    import __main__

    topdir = dirname(__main__.__file__)
    deja_topdir = topdir

    deja_suite = dejagnu.testSuiteForDirectory(
        join(deja_topdir, "libffi-src/tests/testsuite/libffi.call")
    )

    plain_suite = importExternalTestCases(
        "test_*.py", join(topdir, "PyObjCTest"), package="PyObjCTest"
    )

    if use_system_libffi:
        return plain_suite

    else:
        return unittest.TestSuite((plain_suite, deja_suite))
