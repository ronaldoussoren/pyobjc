"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
from PyObjCTools.TestSupport import *
import ExceptionHandling


class TestExceptionHandling(TestCase):
    def testClasses(self):
        self.assertHasAttr(ExceptionHandling, "NSExceptionHandler")
        self.assertIsInstance(ExceptionHandling.NSExceptionHandler, objc.objc_class)


if __name__ == "__main__":
    main()
