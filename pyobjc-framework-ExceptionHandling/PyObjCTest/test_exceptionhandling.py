"""
Some simple tests to check that the framework is properly wrapped.
"""
import ExceptionHandling
import objc
from PyObjCTools.TestSupport import TestCase


class TestExceptionHandling(TestCase):
    def testClasses(self):
        self.assertHasAttr(ExceptionHandling, "NSExceptionHandler")
        self.assertIsInstance(ExceptionHandling.NSExceptionHandler, objc.objc_class)
