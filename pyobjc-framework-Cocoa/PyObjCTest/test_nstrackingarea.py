
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTrackingArea (TestCase):

    @min_os_level("10.5")
    def testConstants(self):
        self.failUnlessEqual(NSTrackingMouseEnteredAndExited, 0x01)
        self.failUnlessEqual(NSTrackingMouseMoved, 0x02)
        self.failUnlessEqual(NSTrackingCursorUpdate, 0x04)

        self.failUnlessEqual(NSTrackingActiveWhenFirstResponder, 0x10)
        self.failUnlessEqual(NSTrackingActiveInKeyWindow, 0x20)
        self.failUnlessEqual(NSTrackingActiveInActiveApp, 0x40)
        self.failUnlessEqual(NSTrackingActiveAlways, 0x80)

        self.failUnlessEqual(NSTrackingAssumeInside, 0x100)
        self.failUnlessEqual(NSTrackingInVisibleRect, 0x200)
        self.failUnlessEqual(NSTrackingEnabledDuringMouseDrag, 0x400)


if __name__ == "__main__":
    main()
