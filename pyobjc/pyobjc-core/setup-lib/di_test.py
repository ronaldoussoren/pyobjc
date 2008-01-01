"""
'test' action for setup.py
"""
# XXX - use setuptools test suite support
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

class cmd_test (install_lib):

    description = "run the unittests"

    user_options = install_lib.user_options + [
        ('verbosity=', None, 'runner verbosity'),
        ('include-gui-tests', None, 'include GUI related tests [default]'),
        ('no-include-gui-tests', None, 'don\'t include GUI related tests'),
        ('test-installed', None, 'test build tree'),
        ('no-test-installed', None, 'test installed PyObjC'),
        ('package=', None, 'test package (default is all)'),
    ]

    boolean_options = install_lib.boolean_options + ['include-gui-tests']
    negative_opt = {
        'no-include-gui-tests': 'include-gui-tests',
        'no-test-installed': 'test-installed',
    }
    negative_opt.update(install_lib.negative_opt)

    def initialize_options(self):
        install_lib.initialize_options(self)
        self.verbosity = 1
        self.include_gui_tests = None
        self.test_installed = None
        self.package = None

    def finalize_options(self):
        install_lib.finalize_options(self)
        if self.include_gui_tests is None:
            self.include_gui_tests = 1

        if self.test_installed is None:
            self.test_installed = 0

        if isinstance(self.verbosity, (str, unicode)):
            self.verbosity = int(self.verbosity)

    def run (self):

        # Make sure we have built everything we need first
        if not self.test_installed:
            self.build()

        # Run the tests
        self.test()

    def get_test_dir(self):
        if self.test_installed:
            import objc
            return os.path.dirname(os.path.dirname(objc.__file__))

        if self.package is None:
            return self.build_dir
        return os.path.join(self.build_dir, self.package.replace('.', '/'))
    
    def test (self):
        import sys

        # Add the build_dir to the start of our module-search-path, and
        # remove it when we're done.
        if not self.test_installed:
            if not os.path.isdir(self.build_dir):
                self.warn("'%s' does not exist -- cannot test" %
                          self.build_dir)
                return
            sys.path.insert(0, self.build_dir)
        try:
            deja_suite = dejagnu.testSuiteForDirectory(
                'libffi-src/tests/testsuite/libffi.call')

            plain_suite = importExternalTestCases("test_*.py",
                self.get_test_dir(), package=self.package)
            
            if self.include_gui_tests:
                gui_suite = importExternalTestCases("guitest_*.py",
                    self.get_test_dir(), package=self.package)
                suite = unittest.TestSuite((plain_suite, gui_suite, deja_suite))
            else:
                suite = unittest.TestSuite((plain_suite, deja_suite))

            runner = unittest.TextTestRunner(verbosity=self.verbosity)
            runner.run(suite)
        
        finally:
            if self.test_installed:
                del sys.path[0]

cmdclass = dict(test=cmd_test)
