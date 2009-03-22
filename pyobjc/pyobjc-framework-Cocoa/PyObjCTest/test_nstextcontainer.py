
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextContainer (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSLineSweepLeft, 0)
        self.failUnlessEqual(NSLineSweepRight, 1)
        self.failUnlessEqual(NSLineSweepDown, 2)
        self.failUnlessEqual(NSLineSweepUp, 3)
        self.failUnlessEqual(NSLineDoesntMove, 0)
        self.failUnlessEqual(NSLineMovesLeft, 1)
        self.failUnlessEqual(NSLineMovesRight, 2)
        self.failUnlessEqual(NSLineMovesDown, 3)
        self.failUnlessEqual(NSLineMovesUp, 4)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTextContainer.widthTracksTextView)
        self.failUnlessArgIsBOOL(NSTextContainer.setWidthTracksTextView_, 0)
        self.failUnlessResultIsBOOL(NSTextContainer.heightTracksTextView)
        self.failUnlessArgIsBOOL(NSTextContainer.setHeightTracksTextView_, 0)
        self.failUnlessResultIsBOOL(NSTextContainer.isSimpleRectangularTextContainer)
        self.failUnlessResultIsBOOL(NSTextContainer.containsPoint_)


if __name__ == "__main__":
    main()
