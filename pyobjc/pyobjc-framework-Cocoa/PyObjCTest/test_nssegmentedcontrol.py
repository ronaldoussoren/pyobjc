
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

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSSegmentedControl.selectSegmentWithTag_)
        self.failUnlessArgIsBOOL(NSSegmentedControl.setSelected_forSegment_, 0)
        self.failUnlessResultIsBOOL(NSSegmentedControl.isSelectedForSegment_)
        self.failUnlessArgIsBOOL(NSSegmentedControl.setEnabled_forSegment_, 0)
        self.failUnlessResultIsBOOL(NSSegmentedControl.isEnabledForSegment_)

if __name__ == "__main__":
    main()
