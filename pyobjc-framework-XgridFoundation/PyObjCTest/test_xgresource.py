from PyObjCTools.TestSupport import TestCase
import XgridFoundation


class TestXGResource(TestCase):
    def testConstants(self):
        self.assertEqual(XgridFoundation.XGResourceStateUninitialized, 0)
        self.assertEqual(XgridFoundation.XGResourceStateOffline, 1)
        self.assertEqual(XgridFoundation.XGResourceStateConnecting, 2)
        self.assertEqual(XgridFoundation.XGResourceStateUnavailable, 3)
        self.assertEqual(XgridFoundation.XGResourceStateAvailable, 4)
        self.assertEqual(XgridFoundation.XGResourceStateWorking, 5)
        self.assertEqual(XgridFoundation.XGResourceStatePending, 6)
        self.assertEqual(XgridFoundation.XGResourceStateStarting, 7)
        self.assertEqual(XgridFoundation.XGResourceStateStagingIn, 8)
        self.assertEqual(XgridFoundation.XGResourceStateRunning, 9)
        self.assertEqual(XgridFoundation.XGResourceStateSuspended, 10)
        self.assertEqual(XgridFoundation.XGResourceStateStagingOut, 11)
        self.assertEqual(XgridFoundation.XGResourceStateCanceled, 12)
        self.assertEqual(XgridFoundation.XGResourceStateFailed, 13)
        self.assertEqual(XgridFoundation.XGResourceStateFinished, 14)

    def testMethods(self):
        self.assertResultIsBOOL(XgridFoundation.XGResource.isUpdating)
        self.assertResultIsBOOL(XgridFoundation.XGResource.isUpdated)
