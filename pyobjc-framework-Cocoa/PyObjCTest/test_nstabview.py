
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTabView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTopTabsBezelBorder,  0)
        self.failUnlessEqual(NSLeftTabsBezelBorder,  1)
        self.failUnlessEqual(NSBottomTabsBezelBorder,  2)
        self.failUnlessEqual(NSRightTabsBezelBorder,  3)
        self.failUnlessEqual(NSNoTabsBezelBorder,  4)
        self.failUnlessEqual(NSNoTabsLineBorder,  5)
        self.failUnlessEqual(NSNoTabsNoBorder,  6)


if __name__ == "__main__":
    main()
