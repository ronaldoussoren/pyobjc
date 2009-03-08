
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
        self.fail("- (NSRect)lineFragmentRectForProposedRect:(NSRect)proposedRect sweepDirection:(NSLineSweepDirection)sweepDirection movementDirection:(NSLineMovementDirection)movementDirection remainingRect:(NSRectPointer)remainingRect;")




if __name__ == "__main__":
    main()
