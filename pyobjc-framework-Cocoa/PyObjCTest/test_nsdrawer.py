
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSDrawerHelper (NSObject):
    def drawerShouldOpen_(self, sender): return 1
    def drawerShouldClose_(self, sender): return 1
    def drawerWillResizeContents_toSize_(self, a, b): return 1

class TestNSDrawer (TestCase):
    def testConstants(self):
        self.assertEqual(NSDrawerClosedState, 0)
        self.assertEqual(NSDrawerOpeningState, 1)
        self.assertEqual(NSDrawerOpenState, 2)
        self.assertEqual(NSDrawerClosingState, 3)

        self.assertIsInstance(NSDrawerWillOpenNotification, unicode)
        self.assertIsInstance(NSDrawerDidOpenNotification, unicode)
        self.assertIsInstance(NSDrawerWillCloseNotification, unicode)
        self.assertIsInstance(NSDrawerDidCloseNotification, unicode)

    def testMethods(self):
        self.assertArgHasType(NSDrawer.setMinContentSize_, 0, NSSize.__typestr__)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSDrawerHelper.drawerShouldOpen_)
        self.assertResultIsBOOL(TestNSDrawerHelper.drawerShouldClose_)
        self.assertResultHasType(TestNSDrawerHelper.drawerWillResizeContents_toSize_, NSSize.__typestr__)
        self.assertArgHasType(TestNSDrawerHelper.drawerWillResizeContents_toSize_, 1, NSSize.__typestr__)



if __name__ == "__main__":
    main()
