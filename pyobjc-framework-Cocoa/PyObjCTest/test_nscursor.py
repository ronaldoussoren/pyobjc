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

        self.assertIsEnumType(AppKit.NSCursorFrameResizePosition)
        self.assertEqual(AppKit.NSCursorFrameResizePositionTop, 1 << 0)
        self.assertEqual(AppKit.NSCursorFrameResizePositionLeft, 1 << 1)
        self.assertEqual(AppKit.NSCursorFrameResizePositionBottom, 1 << 2)
        self.assertEqual(AppKit.NSCursorFrameResizePositionRight, 1 << 3)
        self.assertEqual(
            AppKit.NSCursorFrameResizePositionTopLeft,
            AppKit.NSCursorFrameResizePositionTop
            | AppKit.NSCursorFrameResizePositionLeft,
        )
        self.assertEqual(
            AppKit.NSCursorFrameResizePositionTopRight,
            AppKit.NSCursorFrameResizePositionTop
            | AppKit.NSCursorFrameResizePositionRight,
        )
        self.assertEqual(
            AppKit.NSCursorFrameResizePositionBottomLeft,
            AppKit.NSCursorFrameResizePositionBottom
            | AppKit.NSCursorFrameResizePositionLeft,
        )
        self.assertEqual(
            AppKit.NSCursorFrameResizePositionBottomRight,
            AppKit.NSCursorFrameResizePositionBottom
            | AppKit.NSCursorFrameResizePositionRight,
        )

        self.assertIsEnumType(AppKit.NSCursorFrameResizeDirections)
        self.assertEqual(AppKit.NSCursorFrameResizeDirectionsInward, 1 << 0)
        self.assertEqual(AppKit.NSCursorFrameResizeDirectionsOutward, 1 << 1)
        self.assertEqual(
            AppKit.NSCursorFrameResizeDirectionsAll,
            AppKit.NSCursorFrameResizeDirectionsInward
            | AppKit.NSCursorFrameResizeDirectionsOutward,
        )
