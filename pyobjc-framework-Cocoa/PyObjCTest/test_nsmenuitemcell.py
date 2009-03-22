from AppKit import *
from PyObjCTools.TestSupport import *


class TestNSMenuItemCell (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSMenuItemCell.needsSizing)
        self.failUnlessArgIsBOOL(NSMenuItemCell.setNeedsSizing_, 0)
        self.failUnlessResultIsBOOL(NSMenuItemCell.needsDisplay)
        self.failUnlessArgIsBOOL(NSMenuItemCell.setNeedsDisplay_, 0)
    
if __name__ == "__main__":
    main()
