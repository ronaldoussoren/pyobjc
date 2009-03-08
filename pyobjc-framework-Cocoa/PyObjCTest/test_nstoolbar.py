
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSToolbar (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSToolbarDisplayModeDefault, 0)
        self.failUnlessEqual(NSToolbarDisplayModeIconAndLabel, 1)
        self.failUnlessEqual(NSToolbarDisplayModeIconOnly, 2)
        self.failUnlessEqual(NSToolbarDisplayModeLabelOnly, 3)

        self.failUnlessEqual(NSToolbarSizeModeDefault, 0)
        self.failUnlessEqual(NSToolbarSizeModeRegular, 1)
        self.failUnlessEqual(NSToolbarSizeModeSmall, 2)

        self.failUnlessIsInstance(NSToolbarWillAddItemNotification, unicode)
        self.failUnlessIsInstance(NSToolbarDidRemoveItemNotification, unicode)

if __name__ == "__main__":
    main()
