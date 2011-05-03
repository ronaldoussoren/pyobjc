from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSearchFieldCell (TestCase):
    def testConstants(self):
        self.assertEqual(NSSearchFieldRecentsTitleMenuItemTag, 1000)
        self.assertEqual(NSSearchFieldRecentsMenuItemTag, 1001)
        self.assertEqual(NSSearchFieldClearRecentsMenuItemTag, 1002)
        self.assertEqual(NSSearchFieldNoRecentsMenuItemTag, 1003)

    def testMethods(self):
        self.assertResultIsBOOL(NSSearchFieldCell.sendsWholeSearchString)
        self.assertArgIsBOOL(NSSearchFieldCell.setSendsWholeSearchString_, 0)
        self.assertResultIsBOOL(NSSearchFieldCell.sendsSearchStringImmediately)
        self.assertArgIsBOOL(NSSearchFieldCell.setSendsSearchStringImmediately_, 0)


if __name__ == "__main__":
    main()
