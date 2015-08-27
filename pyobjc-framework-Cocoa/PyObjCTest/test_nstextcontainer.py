
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextContainer (TestCase):
    def testConstants(self):
        self.assertEqual(NSLineSweepLeft, 0)
        self.assertEqual(NSLineSweepRight, 1)
        self.assertEqual(NSLineSweepDown, 2)
        self.assertEqual(NSLineSweepUp, 3)

        self.assertEqual(NSLineDoesntMove, 0)
        self.assertEqual(NSLineMovesLeft, 1)
        self.assertEqual(NSLineMovesRight, 2)
        self.assertEqual(NSLineMovesDown, 3)
        self.assertEqual(NSLineMovesUp, 4)

    def testMethods(self):
        self.assertResultIsBOOL(NSTextContainer.widthTracksTextView)
        self.assertArgIsBOOL(NSTextContainer.setWidthTracksTextView_, 0)
        self.assertResultIsBOOL(NSTextContainer.heightTracksTextView)
        self.assertArgIsBOOL(NSTextContainer.setHeightTracksTextView_, 0)
        self.assertResultIsBOOL(NSTextContainer.isSimpleRectangularTextContainer)
        self.assertResultIsBOOL(NSTextContainer.containsPoint_)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertArgIsOut(NSTextContainer.lineFragmentRectForProposedRect_atIndex_writingDirection_remainingRect_, 3)


if __name__ == "__main__":
    main()
