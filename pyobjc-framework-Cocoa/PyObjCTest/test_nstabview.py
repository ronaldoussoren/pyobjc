
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTabViewHelper (NSObject):
    def tabView_shouldSelectTabViewItem_(self, tv, it): return 1

class TestNSTabView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTopTabsBezelBorder,  0)
        self.failUnlessEqual(NSLeftTabsBezelBorder,  1)
        self.failUnlessEqual(NSBottomTabsBezelBorder,  2)
        self.failUnlessEqual(NSRightTabsBezelBorder,  3)
        self.failUnlessEqual(NSNoTabsBezelBorder,  4)
        self.failUnlessEqual(NSNoTabsLineBorder,  5)
        self.failUnlessEqual(NSNoTabsNoBorder,  6)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTabView.allowsTruncatedLabels)
        self.failUnlessResultIsBOOL(NSTabView.drawsBackground)
        self.failUnlessArgIsBOOL(NSTabView.setAllowsTruncatedLabels_, 0)
        self.failUnlessArgIsBOOL(NSTabView.setDrawsBackground_, 0)

    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestNSTabViewHelper.tabView_shouldSelectTabViewItem_)


if __name__ == "__main__":
    main()
