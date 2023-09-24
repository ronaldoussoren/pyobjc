from PyObjCTools.TestSupport import TestCase

import Accessibility


class TestAXCustomContentHelper(Accessibility.NSObject):
    def accessibilityCustomContentBlock(self):
        return 1

    def setAccessibilityCustomContentBlock_(self, a):
        pass


class TestAXCustomContent(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Accessibility.AXCustomContentImportance)

    def test_constants(self):
        self.assertEqual(Accessibility.AXCustomContentImportanceDefault, 0)
        self.assertEqual(Accessibility.AXCustomContentImportanceHigh, 1)

    def test_protocols(self):
        self.assertProtocolExists("AXCustomContentProvider")

    def testProtocolMethods(self):
        self.assertResultIsBlock(
            TestAXCustomContentHelper.accessibilityCustomContentBlock, b"@"
        )
        self.assertArgIsBlock(
            TestAXCustomContentHelper.setAccessibilityCustomContentBlock_, 0, b"@"
        )
