
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTabViewItem (TestCase):
    def testConstants(self):
        self.assertEqual(NSSelectedTab, 0)
        self.assertEqual(NSBackgroundTab, 1)
        self.assertEqual(NSPressedTab, 2)

    def testMethods(self):
        self.assertArgIsBOOL(NSTabViewItem.drawLabel_inRect_, 0)
        self.assertArgIsBOOL(NSTabViewItem.sizeOfLabel_, 0)

if __name__ == "__main__":
    main()
