import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTrackingArea(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertEqual(AppKit.NSTrackingMouseEnteredAndExited, 0x01)
        self.assertEqual(AppKit.NSTrackingMouseMoved, 0x02)
        self.assertEqual(AppKit.NSTrackingCursorUpdate, 0x04)

        self.assertEqual(AppKit.NSTrackingActiveWhenFirstResponder, 0x10)
        self.assertEqual(AppKit.NSTrackingActiveInKeyWindow, 0x20)
        self.assertEqual(AppKit.NSTrackingActiveInActiveApp, 0x40)
        self.assertEqual(AppKit.NSTrackingActiveAlways, 0x80)

        self.assertEqual(AppKit.NSTrackingAssumeInside, 0x100)
        self.assertEqual(AppKit.NSTrackingInVisibleRect, 0x200)
        self.assertEqual(AppKit.NSTrackingEnabledDuringMouseDrag, 0x400)
