import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSTextTypesHelper(AppKit.NSObject):
    def textWritingMode(self):
        return 1


class TestNSTextTypes(TestCase):
    def test_constants(self):
        self.assertEqual(AppKit.NSTextAlignmentLeft, 0)

        if objc.arch == "arm64":
            self.assertEqual(AppKit.NSTextAlignmentCenter, 1)
            self.assertEqual(AppKit.NSTextAlignmentRight, 2)
        else:
            self.assertEqual(AppKit.NSTextAlignmentRight, 1)
            self.assertEqual(AppKit.NSTextAlignmentCenter, 2)

        self.assertEqual(AppKit.NSTextAlignmentJustified, 3)
        self.assertEqual(AppKit.NSTextAlignmentNatural, 4)

        self.assertEqual(AppKit.NSWritingDirectionNatural, -1)
        self.assertEqual(AppKit.NSWritingDirectionLeftToRight, 0)
        self.assertEqual(AppKit.NSWritingDirectionRightToLeft, 1)

        self.assertEqual(AppKit.NSTextWritingModeHorizontal, 0)
        self.assertEqual(AppKit.NSTextWritingModeVertical, 1)

    @min_sdk_level("12.0")
    def test_protocols(self):
        objc.protocolNamed("NSTextWritingModeProvider")

    def test_methods(self):
        self.assertResultHasType(
            TestNSTextTypesHelper.textWritingMode, objc._C_NSInteger
        )
