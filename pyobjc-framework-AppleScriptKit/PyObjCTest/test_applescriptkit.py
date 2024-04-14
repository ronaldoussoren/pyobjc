"""
Some simple tests to check that the framework is properly wrapped.
"""

import AppleScriptKit
import objc
from PyObjCTools.TestSupport import TestCase


class TestAppleScriptKit(TestCase):
    def testClasses(self):
        self.assertHasAttr(AppleScriptKit, "ASKPluginObject")
        self.assertIsInstance(AppleScriptKit.ASKPluginObject, objc.objc_class)


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(AppleScriptKit)
