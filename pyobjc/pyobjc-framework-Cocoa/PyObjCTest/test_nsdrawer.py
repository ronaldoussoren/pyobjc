
from PyObjCTools.TestSupport import *
from AppKit import *

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



if __name__ == "__main__":
    main()
