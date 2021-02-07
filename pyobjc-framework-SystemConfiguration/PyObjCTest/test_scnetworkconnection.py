from PyObjCTools.TestSupport import TestCase, min_os_level
import SystemConfiguration
import objc


class TestSCNetworkConnection(TestCase):
    def testTypes(self):
        self.assertIsInstance(
            SystemConfiguration.SCNetworkConnectionRef, objc.objc_class
        )

    def testConstants(self):
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionInvalid, -1)
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionDisconnected, 0)
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionConnecting, 1)
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionConnected, 2)
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionDisconnecting, 3)

        self.assertEqual(SystemConfiguration.kSCNetworkConnectionPPPDisconnected, 0)
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionPPPInitializing, 1)
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionPPPConnectingLink, 2)
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionPPPDialOnTraffic, 3)
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionPPPNegotiatingLink, 4)
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionPPPAuthenticating, 5)
        self.assertEqual(
            SystemConfiguration.kSCNetworkConnectionPPPWaitingForCallBack, 6
        )
        self.assertEqual(
            SystemConfiguration.kSCNetworkConnectionPPPNegotiatingNetwork, 7
        )
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionPPPConnected, 8)
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionPPPTerminating, 9)
        self.assertEqual(
            SystemConfiguration.kSCNetworkConnectionPPPDisconnectingLink, 10
        )
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionPPPHoldingLinkOff, 11)
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionPPPSuspended, 12)
        self.assertEqual(
            SystemConfiguration.kSCNetworkConnectionPPPWaitingForRedial, 13
        )

        self.assertEqual(SystemConfiguration.kSCNetworkConnectionBytesIn, "BytesIn")
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionBytesOut, "BytesOut")
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionPacketsIn, "PacketsIn")
        self.assertEqual(
            SystemConfiguration.kSCNetworkConnectionPacketsOut, "PacketsOut"
        )
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionErrorsIn, "ErrorsIn")
        self.assertEqual(SystemConfiguration.kSCNetworkConnectionErrorsOut, "ErrorsOut")

        self.assertEqual(
            SystemConfiguration.kSCNetworkConnectionSelectionOptionOnDemandHostName,
            "OnDemandHostName",
        )
        self.assertEqual(
            SystemConfiguration.kSCNetworkConnectionSelectionOptionOnDemandRetry,
            "OnDemandRetry",
        )

    def testFunctions(self):
        v = SystemConfiguration.SCNetworkConnectionGetTypeID()
        self.assertIsInstance(v, int)

        self.assertResultIsBOOL(
            SystemConfiguration.SCNetworkConnectionCopyUserPreferences
        )
        self.assertArgIsOut(
            SystemConfiguration.SCNetworkConnectionCopyUserPreferences, 1
        )
        self.assertArgIsOut(
            SystemConfiguration.SCNetworkConnectionCopyUserPreferences, 2
        )
        (
            v,
            servId,
            userOpts,
        ) = SystemConfiguration.SCNetworkConnectionCopyUserPreferences(None, None, None)
        if v:
            self.assertIsInstance(servId, str)
            self.assertIsInstance(
                userOpts, (SystemConfiguration.CFDictionaryRef, type(None))
            )
        else:
            self.assertTrue(servId is None)
            self.assertTrue(userOpts is None)

        def callout(ref, status, info):
            pass

        ctx = object()
        v = SystemConfiguration.SCNetworkConnectionCreateWithServiceID(
            None, "pyobjc.test.id", callout, ctx
        )

        self.assertResultIsCFRetained(
            SystemConfiguration.SCNetworkConnectionCopyServiceID
        )

        SystemConfiguration.SCNetworkConnectionGetStatus

        self.assertResultIsCFRetained(
            SystemConfiguration.SCNetworkConnectionCopyExtendedStatus
        )
        self.assertResultIsCFRetained(
            SystemConfiguration.SCNetworkConnectionCopyStatistics
        )
        self.assertResultIsBOOL(SystemConfiguration.SCNetworkConnectionStart)
        self.assertResultIsBOOL(SystemConfiguration.SCNetworkConnectionStop)
        self.assertResultIsCFRetained(
            SystemConfiguration.SCNetworkConnectionCopyUserOptions
        )
        self.assertResultIsBOOL(
            SystemConfiguration.SCNetworkConnectionScheduleWithRunLoop
        )
        self.assertResultIsBOOL(
            SystemConfiguration.SCNetworkConnectionUnscheduleFromRunLoop
        )

    @min_os_level("10.6")
    def testFunctions10_6(self):
        self.assertResultIsBOOL(SystemConfiguration.SCNetworkConnectionSetDispatchQueue)
