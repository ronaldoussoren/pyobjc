from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSMenuItemCell (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSMenuItemCell.needsSizing)
        self.assertArgIsBOOL(NSMenuItemCell.setNeedsSizing_, 0)
        self.assertResultIsBOOL(NSMenuItemCell.needsDisplay)
        self.assertArgIsBOOL(NSMenuItemCell.setNeedsDisplay_, 0)
    
if __name__ == "__main__":
    main()
