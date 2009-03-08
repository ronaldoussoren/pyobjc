
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSegmentedControl (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSSegmentStyleAutomatic, 0)
        self.failUnlessEqual(NSSegmentStyleRounded, 1)
        self.failUnlessEqual(NSSegmentStyleTexturedRounded, 2)
        self.failUnlessEqual(NSSegmentStyleRoundRect, 3)
        self.failUnlessEqual(NSSegmentStyleTexturedSquare, 4)
        self.failUnlessEqual(NSSegmentStyleCapsule, 5)
        self.failUnlessEqual(NSSegmentStyleSmallSquare, 6)


if __name__ == "__main__":
    main()
