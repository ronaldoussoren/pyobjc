from PyObjCTools.TestSupport import *
from SystemConfiguration import *

try:
    unicode
except NameError:
    unicode = str

try:
    long
except NameError:
    long = int

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

    def testFunctions(self):
        v = SCNetworkConnectionGetTypeID()
        self.assertIsInstance(v, (int, long))

        self.assertResultIsBOOL(SCNetworkConnectionCopyUserPreferences)
        self.assertArgIsOut(SCNetworkConnectionCopyUserPreferences, 1)
        self.assertArgIsOut(SCNetworkConnectionCopyUserPreferences, 2)
        v,  servId, userOpts = SCNetworkConnectionCopyUserPreferences(None, None, None)
        if v:
            self.assertIsInstance(servId, unicode)
            self.assertIsInstance(userOpts, CFDictionaryRef)
        else:
            self.assertTrue(servId is None)
            self.assertTrue(userOpts is None)

        def callout(ref, status, info):
            pass
        ctx = object()
        v = SCNetworkConnectionCreateWithServiceID(None, "pyobjc.test.id", callout, ctx)

        self.assertResultIsCFRetained(SCNetworkConnectionCopyServiceID)

        # FIXME: Need test for this
        SCNetworkConnectionGetStatus

        self.assertResultIsCFRetained(SCNetworkConnectionCopyExtendedStatus)
        self.assertResultIsCFRetained(SCNetworkConnectionCopyStatistics)
        self.assertResultIsBOOL(SCNetworkConnectionStart)
        self.assertResultIsBOOL(SCNetworkConnectionStop)
        self.assertResultIsCFRetained(SCNetworkConnectionCopyUserOptions)
        self.assertResultIsBOOL(SCNetworkConnectionScheduleWithRunLoop)
        self.assertResultIsBOOL(SCNetworkConnectionUnscheduleFromRunLoop)


if __name__ == "__main__":
    main()
