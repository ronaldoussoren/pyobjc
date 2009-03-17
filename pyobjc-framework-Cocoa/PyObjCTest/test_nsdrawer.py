
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSDrawerHelper (NSObject):
    def drawerShouldOpen_(self, sender): return 1
    def drawerShouldClose_(self, sender): return 1
    def drawerWillResizeContents_toSize_(self, a, b): return 1

class TestNSDrawer (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSDrawerClosedState, 0)
        self.failUnlessEqual(NSDrawerOpeningState, 1)
        self.failUnlessEqual(NSDrawerOpenState, 2)
        self.failUnlessEqual(NSDrawerClosingState, 3)

        self.failUnlessIsInstance(NSDrawerWillOpenNotification, unicode)
        self.failUnlessIsInstance(NSDrawerDidOpenNotification, unicode)
        self.failUnlessIsInstance(NSDrawerWillCloseNotification, unicode)
        self.failUnlessIsInstance(NSDrawerDidCloseNotification, unicode)

    def testMethods(self):
        self.failUnlessArgHasType(NSDrawer.setMinContentSize_, 0, NSSize.__typestr__)

    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestNSDrawerHelper.drawerShouldOpen_)
        self.failUnlessResultIsBOOL(TestNSDrawerHelper.drawerShouldClose_)
        self.failUnlessResultHasType(TestNSDrawerHelper.drawerWillResizeContents_toSize_, NSSize.__typestr__)
        self.failUnlessArgHasType(TestNSDrawerHelper.drawerWillResizeContents_toSize_, 1, NSSize.__typestr__)



if __name__ == "__main__":
    main()
