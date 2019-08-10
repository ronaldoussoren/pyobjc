"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
from PyObjCTools.TestSupport import *
import InterfaceBuilderKit


class TestInterfaceBuilderKit(TestCase):
    def testClasses(self):
        self.assertHasAttr(InterfaceBuilderKit, "IBDocument")
        self.assertIsInstance(InterfaceBuilderKit.IBDocument, objc.objc_class)
        self.assertHasAttr(InterfaceBuilderKit, "IBPlugin")
        self.assertIsInstance(InterfaceBuilderKit.IBPlugin, objc.objc_class)


if __name__ == "__main__":
    main()
