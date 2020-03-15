import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSCursor(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(AppKit.NSCursor.setHiddenUntilMouseMoves_, 0)
        self.assertArgIsBOOL(AppKit.NSCursor.setOnMouseExited_, 0)
        self.assertArgIsBOOL(AppKit.NSCursor.setOnMouseEntered_, 0)
        self.assertResultIsBOOL(AppKit.NSCursor.isSetOnMouseExited)
        self.assertResultIsBOOL(AppKit.NSCursor.isSetOnMouseEntered)

    def testConstants(self):
        self.assertEqual(AppKit.NSAppKitVersionNumberWithCursorSizeSupport, 682.0)
