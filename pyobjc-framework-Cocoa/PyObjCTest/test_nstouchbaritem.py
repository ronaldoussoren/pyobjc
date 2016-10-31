from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTouchBarItem (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertResultIsBOOL(NSTouchBarItem.isVisible)
        #self.assertArgIsBOOL(NSTouchBarItem.setVisible_, 0)

    @min_sdk_level('10.12')
    def testConstants(self):
        self.assertEqual(NSTouchBarItemPriorityHigh, 1000.0)
        self.assertEqual(NSTouchBarItemPriorityNormal, 0.0)
        self.assertEqual(NSTouchBarItemPriorityLow, -1000.0)

        self.assertIsInstance(NSTouchBarItemIdentifierFixedSpaceSmall, unicode)
        self.assertIsInstance(NSTouchBarItemIdentifierFixedSpaceLarge, unicode)
        self.assertIsInstance(NSTouchBarItemIdentifierFlexibleSpace, unicode)
        self.assertIsInstance(NSTouchBarItemIdentifierOtherItemsProxy, unicode)

if __name__ == "__main__":
    main()
