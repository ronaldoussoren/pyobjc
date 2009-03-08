
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSearchFieldCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSSearchFieldRecentsTitleMenuItemTag, 1000)
        self.failUnlessEqual(NSSearchFieldRecentsMenuItemTag, 1001)
        self.failUnlessEqual(NSSearchFieldClearRecentsMenuItemTag, 1002)
        self.failUnlessEqual(NSSearchFieldNoRecentsMenuItemTag, 1003)


if __name__ == "__main__":
    main()
