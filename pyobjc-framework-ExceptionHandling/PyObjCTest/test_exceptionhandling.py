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


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(ExceptionHandling)
