
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSToolbarItem (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSToolbarItemVisibilityPriorityStandard, 0)
        self.failUnlessEqual(NSToolbarItemVisibilityPriorityLow, -1000)
        self.failUnlessEqual(NSToolbarItemVisibilityPriorityHigh, 1000)
        self.failUnlessEqual(NSToolbarItemVisibilityPriorityUser, 2000)

        self.failUnlessIsInstance(NSToolbarSeparatorItemIdentifier, unicode)
        self.failUnlessIsInstance(NSToolbarSpaceItemIdentifier, unicode)
        self.failUnlessIsInstance(NSToolbarFlexibleSpaceItemIdentifier, unicode)
        self.failUnlessIsInstance(NSToolbarShowColorsItemIdentifier, unicode)
        self.failUnlessIsInstance(NSToolbarShowFontsItemIdentifier, unicode)
        self.failUnlessIsInstance(NSToolbarCustomizeToolbarItemIdentifier, unicode)
        self.failUnlessIsInstance(NSToolbarPrintItemIdentifier, unicode)


if __name__ == "__main__":
    main()
