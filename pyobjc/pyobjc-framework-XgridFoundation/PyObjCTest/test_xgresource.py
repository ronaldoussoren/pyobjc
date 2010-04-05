
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGResource (TestCase):
    def testConstants(self):
        self.assertEqual(XGResourceStateUninitialized, 0)
        self.assertEqual(XGResourceStateOffline, 1)
        self.assertEqual(XGResourceStateConnecting, 2)
        self.assertEqual(XGResourceStateUnavailable, 3)
        self.assertEqual(XGResourceStateAvailable, 4)
        self.assertEqual(XGResourceStateWorking, 5)
        self.assertEqual(XGResourceStatePending, 6)
        self.assertEqual(XGResourceStateStarting, 7)
        self.assertEqual(XGResourceStateStagingIn, 8)
        self.assertEqual(XGResourceStateRunning, 9)
        self.assertEqual(XGResourceStateSuspended, 10)
        self.assertEqual(XGResourceStateStagingOut, 11)
        self.assertEqual(XGResourceStateCanceled, 12)
        self.assertEqual(XGResourceStateFailed, 13)
        self.assertEqual(XGResourceStateFinished, 14)

    def testMethods(self):
        self.assertResultIsBOOL(XGResource.isUpdating)
        self.assertResultIsBOOL(XGResource.isUpdated)


if __name__ == "__main__":
    main()
