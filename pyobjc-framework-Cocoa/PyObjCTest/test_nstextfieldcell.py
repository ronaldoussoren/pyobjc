import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTextFieldCell(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSTextFieldBezelStyle)
        self.assertEqual(AppKit.NSTextFieldSquareBezel, 0)
        self.assertEqual(AppKit.NSTextFieldRoundedBezel, 1)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSTextFieldCell.drawsBackground)
        self.assertArgIsBOOL(AppKit.NSTextFieldCell.setDrawsBackground_, 0)
        self.assertArgIsBOOL(
            AppKit.NSTextFieldCell.setWantsNotificationForMarkedText_, 0
        )
