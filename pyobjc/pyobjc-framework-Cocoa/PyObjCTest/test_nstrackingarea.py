
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTrackingArea (TestCase):

    @min_os_level("10.5")
    def testConstants(self):
        self.assertEqual(NSTrackingMouseEnteredAndExited, 0x01)
        self.assertEqual(NSTrackingMouseMoved, 0x02)
        self.assertEqual(NSTrackingCursorUpdate, 0x04)

        self.assertEqual(NSTrackingActiveWhenFirstResponder, 0x10)
        self.assertEqual(NSTrackingActiveInKeyWindow, 0x20)
        self.assertEqual(NSTrackingActiveInActiveApp, 0x40)
        self.assertEqual(NSTrackingActiveAlways, 0x80)

        self.assertEqual(NSTrackingAssumeInside, 0x100)
        self.assertEqual(NSTrackingInVisibleRect, 0x200)
        self.assertEqual(NSTrackingEnabledDuringMouseDrag, 0x400)


if __name__ == "__main__":
    main()
