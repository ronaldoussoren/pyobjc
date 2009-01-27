'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import ExceptionHandling

class TestExceptionHandling (TestCase):
    def testClasses(self):
        self.assert_(hasattr(ExceptionHandling, 'NSExceptionHandler'))
        self.assert_(isinstance(ExceptionHandling.NSExceptionHandler, objc.objc_class))

if __name__ == "__main__":
    main()
