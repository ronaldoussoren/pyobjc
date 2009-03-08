
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSParagraphStyle (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSLeftTabStopType, 0)
        self.failUnlessEqual(NSRightTabStopType, 1)
        self.failUnlessEqual(NSCenterTabStopType, 2)
        self.failUnlessEqual(NSDecimalTabStopType, 3)

        self.failUnlessEqual(NSLineBreakByWordWrapping,  0)
        self.failUnlessEqual(NSLineBreakByCharWrapping, 1)
        self.failUnlessEqual(NSLineBreakByClipping, 2)
        self.failUnlessEqual(NSLineBreakByTruncatingHead, 3)
        self.failUnlessEqual(NSLineBreakByTruncatingTail, 4)
        self.failUnlessEqual(NSLineBreakByTruncatingMiddle, 5)

        self.failUnlessIsInstance(NSTabColumnTerminatorsAttributeName, unicode)

if __name__ == "__main__":
    main()
