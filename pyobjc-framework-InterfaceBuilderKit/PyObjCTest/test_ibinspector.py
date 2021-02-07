import InterfaceBuilderKit
from PyObjCTools.TestSupport import TestCase


class TestIBInspector(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(
            InterfaceBuilderKit.IBInspector.supportsMultipleObjectInspection
        )
