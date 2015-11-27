from PyObjCTools.TestSupport import *
from SystemConfiguration import *

class TestSCNetworkConnection (TestCase):
    def testTypes(self):
        self.assertIsInstance(SCNetworkConnectionRef, objc.objc_class)

    def testConstants(self):
        self.assertEqual(kSCNetworkConnectionInvalid,  -1)
        self.assertEqual(kSCNetworkConnectionDisconnected,  0)
        self.assertEqual(kSCNetworkConnectionConnecting,  1)
        self.assertEqual(kSCNetworkConnectionConnected,  2)
        self.assertEqual(kSCNetworkConnectionDisconnecting,  3)

        self.assertEqual(kSCNetworkConnectionPPPDisconnected,  0)
        self.assertEqual(kSCNetworkConnectionPPPInitializing,  1)
        self.assertEqual(kSCNetworkConnectionPPPConnectingLink,  2)
        self.assertEqual(kSCNetworkConnectionPPPDialOnTraffic,  3)
        self.assertEqual(kSCNetworkConnectionPPPNegotiatingLink,  4)
        self.assertEqual(kSCNetworkConnectionPPPAuthenticating,  5)
        self.assertEqual(kSCNetworkConnectionPPPWaitingForCallBack,  6)
        self.assertEqual(kSCNetworkConnectionPPPNegotiatingNetwork,  7)
        self.assertEqual(kSCNetworkConnectionPPPConnected,  8)
        self.assertEqual(kSCNetworkConnectionPPPTerminating,  9)
        self.assertEqual(kSCNetworkConnectionPPPDisconnectingLink,  10)
        self.assertEqual(kSCNetworkConnectionPPPHoldingLinkOff,  11)
        self.assertEqual(kSCNetworkConnectionPPPSuspended,  12)
        self.assertEqual(kSCNetworkConnectionPPPWaitingForRedial,  13)

        self.assertEqual(kSCNetworkConnectionBytesIn, b"BytesIn".decode('latin1'))
        self.assertEqual(kSCNetworkConnectionBytesOut, b"BytesOut".decode('latin1'))
        self.assertEqual(kSCNetworkConnectionPacketsIn, b"PacketsIn".decode('latin1'))
        self.assertEqual(kSCNetworkConnectionPacketsOut, b"PacketsOut".decode('latin1'))
        self.assertEqual(kSCNetworkConnectionErrorsIn, b"ErrorsIn".decode('latin1'))
        self.assertEqual(kSCNetworkConnectionErrorsOut, b"ErrorsOut".decode('latin1'))

        self.assertEqual(kSCNetworkConnectionSelectionOptionOnDemandHostName, b"OnDemandHostName".decode('latin1'))
        self.assertEqual(kSCNetworkConnectionSelectionOptionOnDemandRetry, b"OnDemandRetry".decode('latin1'))

    def testFunctions(self):
        v = SCNetworkConnectionGetTypeID()
        self.assertIsInstance(v, (int, long))

        self.assertResultIsBOOL(SCNetworkConnectionCopyUserPreferences)
        self.assertArgIsOut(SCNetworkConnectionCopyUserPreferences, 1)
        self.assertArgIsOut(SCNetworkConnectionCopyUserPreferences, 2)
        v,  servId, userOpts = SCNetworkConnectionCopyUserPreferences(None, None, None)
        if v:
            self.assertIsInstance(servId, unicode)
            self.assertIsInstance(userOpts, (CFDictionaryRef, type(None)))
        else:
            self.assertTrue(servId is None)
            self.assertTrue(userOpts is None)

        def callout(ref, status, info):
            pass
        ctx = object()
        v = SCNetworkConnectionCreateWithServiceID(None, "pyobjc.test.id", callout, ctx)

        self.assertResultIsCFRetained(SCNetworkConnectionCopyServiceID)

        SCNetworkConnectionGetStatus

        self.assertResultIsCFRetained(SCNetworkConnectionCopyExtendedStatus)
        self.assertResultIsCFRetained(SCNetworkConnectionCopyStatistics)
        self.assertResultIsBOOL(SCNetworkConnectionStart)
        self.assertResultIsBOOL(SCNetworkConnectionStop)
        self.assertResultIsCFRetained(SCNetworkConnectionCopyUserOptions)
        self.assertResultIsBOOL(SCNetworkConnectionScheduleWithRunLoop)
        self.assertResultIsBOOL(SCNetworkConnectionUnscheduleFromRunLoop)

    @min_os_level('10.6')
    def testFunctions10_6(self):
        self.assertResultIsBOOL(SCNetworkConnectionSetDispatchQueue)

if __name__ == "__main__":
    main()
