"""
Some simple tests to check that the framework is properly wrapped.
"""
import InterfaceBuilderKit
from PyObjCTools.TestSupport import TestCase
import objc


class TestInterfaceBuilderKit(TestCase):
    def testClasses(self):
        self.assertHasAttr(InterfaceBuilderKit, "IBDocument")
        self.assertIsInstance(InterfaceBuilderKit.IBDocument, objc.objc_class)
        self.assertHasAttr(InterfaceBuilderKit, "IBPlugin")
        self.assertIsInstance(InterfaceBuilderKit.IBPlugin, objc.objc_class)
