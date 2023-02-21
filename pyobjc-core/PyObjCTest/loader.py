import os
import unittest
from fnmatch import fnmatch
from os.path import dirname, join


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
            print(f"SKIP {modName}: {msg}")
            continue

        if "." in modName:
            for elem in modName.split(".")[1:]:
                module = getattr(module, elem)

        s = unittest.defaultTestLoader.loadTestsFromModule(module)
        suites.append(s)

    return unittest.TestSuite(suites)


gTopdir = dirname(dirname(__file__))


def makeTestSuite():
    plain_suite = importExternalTestCases(
        "test_*.py", join(gTopdir, "PyObjCTest"), package="PyObjCTest"
    )

    return plain_suite
