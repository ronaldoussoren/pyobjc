
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSImageCell (TestCase):
    def testConstants(self):

        self.failUnlessEqual(NSImageAlignCenter, 0)
        self.failUnlessEqual(NSImageAlignTop, 1)
        self.failUnlessEqual(NSImageAlignTopLeft, 2)
        self.failUnlessEqual(NSImageAlignTopRight, 3)
        self.failUnlessEqual(NSImageAlignLeft, 4)
        self.failUnlessEqual(NSImageAlignBottom, 5)
        self.failUnlessEqual(NSImageAlignBottomLeft, 6)
        self.failUnlessEqual(NSImageAlignBottomRight, 7)
        self.failUnlessEqual(NSImageAlignRight, 8)

        self.failUnlessEqual(NSImageFrameNone, 0)
        self.failUnlessEqual(NSImageFramePhoto, 1)
        self.failUnlessEqual(NSImageFrameGrayBezel, 2)
        self.failUnlessEqual(NSImageFrameGroove, 3)
        self.failUnlessEqual(NSImageFrameButton, 4)


if __name__ == "__main__":
    main()
