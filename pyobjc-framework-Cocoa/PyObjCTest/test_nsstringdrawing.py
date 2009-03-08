
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSStringDrawing (TestCase):
    @min_os_level("10.5")
    def testConstants10_5(self):
        self.failUnlessEqual(NSStringDrawingTruncatesLastVisibleLine, (1 << 5))

    def testConstants(self):
        self.failUnlessEqual(NSStringDrawingUsesLineFragmentOrigin, (1 << 0))
        self.failUnlessEqual(NSStringDrawingUsesFontLeading, (1 << 1))
        self.failUnlessEqual(NSStringDrawingDisableScreenFontSubstitution, (1 << 2))
        self.failUnlessEqual(NSStringDrawingUsesDeviceMetrics, (1 << 3))
        self.failUnlessEqual(NSStringDrawingOneShot, (1 << 4))

if __name__ == "__main__":
    main()
