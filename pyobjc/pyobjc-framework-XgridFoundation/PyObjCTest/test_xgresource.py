
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGResource (TestCase):
    def testConstants(self):
        self.failUnlessEqual(XGResourceStateUninitialized, 0)
        self.failUnlessEqual(XGResourceStateOffline, 1)
        self.failUnlessEqual(XGResourceStateConnecting, 2)
        self.failUnlessEqual(XGResourceStateUnavailable, 3)
        self.failUnlessEqual(XGResourceStateAvailable, 4)
        self.failUnlessEqual(XGResourceStateWorking, 5)
        self.failUnlessEqual(XGResourceStatePending, 6)
        self.failUnlessEqual(XGResourceStateStarting, 7)
        self.failUnlessEqual(XGResourceStateStagingIn, 8)
        self.failUnlessEqual(XGResourceStateRunning, 9)
        self.failUnlessEqual(XGResourceStateSuspended, 10)
        self.failUnlessEqual(XGResourceStateStagingOut, 11)
        self.failUnlessEqual(XGResourceStateCanceled, 12)
        self.failUnlessEqual(XGResourceStateFailed, 13)
        self.failUnlessEqual(XGResourceStateFinished, 14)

    def testMethods(self):
        self.failUnlessResultIsBOOL(XGResource.isUpdating)
        self.failUnlessResultIsBOOL(XGResource.isUpdated)


if __name__ == "__main__":
    main()
