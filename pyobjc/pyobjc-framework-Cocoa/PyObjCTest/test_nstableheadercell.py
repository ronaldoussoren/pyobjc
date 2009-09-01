from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSTableHeaderCell (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSTableHeaderCell.drawSortIndicatorWithFrame_inView_ascending_priority_, 2)

        self.failUnlessResultHasType(NSTableHeaderCell.sortIndicatorRectForBounds_, NSRect.__typestr__)
        self.failUnlessArgHasType(NSTableHeaderCell.sortIndicatorRectForBounds_, 0, NSRect.__typestr__)

if __name__ == "__main__":
    main()
