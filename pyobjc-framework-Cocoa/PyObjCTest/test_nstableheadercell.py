from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSTableHeaderCell (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(NSTableHeaderCell.drawSortIndicatorWithFrame_inView_ascending_priority_, 2)

        self.assertResultHasType(NSTableHeaderCell.sortIndicatorRectForBounds_, NSRect.__typestr__)
        self.assertArgHasType(NSTableHeaderCell.sortIndicatorRectForBounds_, 0, NSRect.__typestr__)

if __name__ == "__main__":
    main()
