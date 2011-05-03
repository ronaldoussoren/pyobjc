
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSegmentedControl (TestCase):
    def testConstants(self):
        self.assertEqual(NSSegmentStyleAutomatic, 0)
        self.assertEqual(NSSegmentStyleRounded, 1)
        self.assertEqual(NSSegmentStyleTexturedRounded, 2)
        self.assertEqual(NSSegmentStyleRoundRect, 3)
        self.assertEqual(NSSegmentStyleTexturedSquare, 4)
        self.assertEqual(NSSegmentStyleCapsule, 5)
        self.assertEqual(NSSegmentStyleSmallSquare, 6)

    def testMethods(self):
        self.assertResultIsBOOL(NSSegmentedControl.selectSegmentWithTag_)
        self.assertArgIsBOOL(NSSegmentedControl.setSelected_forSegment_, 0)
        self.assertResultIsBOOL(NSSegmentedControl.isSelectedForSegment_)
        self.assertArgIsBOOL(NSSegmentedControl.setEnabled_forSegment_, 0)
        self.assertResultIsBOOL(NSSegmentedControl.isEnabledForSegment_)

if __name__ == "__main__":
    main()
