
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSImageCell (TestCase):
    def testConstants(self):

        self.assertEqual(NSImageAlignCenter, 0)
        self.assertEqual(NSImageAlignTop, 1)
        self.assertEqual(NSImageAlignTopLeft, 2)
        self.assertEqual(NSImageAlignTopRight, 3)
        self.assertEqual(NSImageAlignLeft, 4)
        self.assertEqual(NSImageAlignBottom, 5)
        self.assertEqual(NSImageAlignBottomLeft, 6)
        self.assertEqual(NSImageAlignBottomRight, 7)
        self.assertEqual(NSImageAlignRight, 8)

        self.assertEqual(NSImageFrameNone, 0)
        self.assertEqual(NSImageFramePhoto, 1)
        self.assertEqual(NSImageFrameGrayBezel, 2)
        self.assertEqual(NSImageFrameGroove, 3)
        self.assertEqual(NSImageFrameButton, 4)


if __name__ == "__main__":
    main()
