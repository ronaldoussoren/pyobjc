
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPopUpButtonCell (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSPopUpNoArrow, 0)
        self.failUnlessEqual(NSPopUpArrowAtCenter, 1)
        self.failUnlessEqual(NSPopUpArrowAtBottom, 2)

        self.failUnlessIsInstance(NSPopUpButtonCellWillPopUpNotification, unicode)


if __name__ == "__main__":
    main()
