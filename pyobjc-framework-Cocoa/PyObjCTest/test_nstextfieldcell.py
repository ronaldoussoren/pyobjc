import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTextFieldCell(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSTextFieldSquareBezel, 0)
        self.assertEqual(AppKit.NSTextFieldRoundedBezel, 1)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTextFieldCell.drawsBackground)
        self.assertArgIsBOOL(AppKit.NSTextFieldCell.setDrawsBackground_, 0)
        self.assertArgIsBOOL(
            AppKit.NSTextFieldCell.setWantsNotificationForMarkedText_, 0
        )
