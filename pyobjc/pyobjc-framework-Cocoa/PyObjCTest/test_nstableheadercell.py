from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSTableHeaderCell (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSTableHeaderCell.drawSortIndicatorWithFrame_inView_ascending_priority_, 2)

if __name__ == "__main__":
    main()
