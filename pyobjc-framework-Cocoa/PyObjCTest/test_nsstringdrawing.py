
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSStringDrawing (TestCase):
    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(NSStringDrawingTruncatesLastVisibleLine, (1 << 5))

    def testConstants(self):
        self.assertEqual(NSStringDrawingUsesLineFragmentOrigin, (1 << 0))
        self.assertEqual(NSStringDrawingUsesFontLeading, (1 << 1))
        self.assertEqual(NSStringDrawingDisableScreenFontSubstitution, (1 << 2))
        self.assertEqual(NSStringDrawingUsesDeviceMetrics, (1 << 3))
        self.assertEqual(NSStringDrawingOneShot, (1 << 4))

if __name__ == "__main__":
    main()
