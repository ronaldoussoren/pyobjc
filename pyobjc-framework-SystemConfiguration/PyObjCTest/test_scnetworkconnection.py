from PyObjCTools.TestSupport import *
from SystemConfiguration import *

class TestSCNetworkConnection (TestCase):
    def testTypes(self):
        self.failUnlessIsInstance(SCNetworkConnectionRef, objc.objc_class)

    def testConstants(self):
        self.failUnlessEqual(kSCNetworkConnectionInvalid,  -1)
        self.failUnlessEqual(kSCNetworkConnectionDisconnected,  0)
        self.failUnlessEqual(kSCNetworkConnectionConnecting,  1)
        self.failUnlessEqual(kSCNetworkConnectionConnected,  2)
        self.failUnlessEqual(kSCNetworkConnectionDisconnecting,  3)

        self.failUnlessEqual(kSCNetworkConnectionPPPDisconnected,  0)
        self.failUnlessEqual(kSCNetworkConnectionPPPInitializing,  1)
        self.failUnlessEqual(kSCNetworkConnectionPPPConnectingLink,  2)
        self.failUnlessEqual(kSCNetworkConnectionPPPDialOnTraffic,  3)
        self.failUnlessEqual(kSCNetworkConnectionPPPNegotiatingLink,  4)
        self.failUnlessEqual(kSCNetworkConnectionPPPAuthenticating,  5)
        self.failUnlessEqual(kSCNetworkConnectionPPPWaitingForCallBack,  6)
        self.failUnlessEqual(kSCNetworkConnectionPPPNegotiatingNetwork,  7)
        self.failUnlessEqual(kSCNetworkConnectionPPPConnected,  8)
        self.failUnlessEqual(kSCNetworkConnectionPPPTerminating,  9)
        self.failUnlessEqual(kSCNetworkConnectionPPPDisconnectingLink,  10)
        self.failUnlessEqual(kSCNetworkConnectionPPPHoldingLinkOff,  11)
        self.failUnlessEqual(kSCNetworkConnectionPPPSuspended,  12)
        self.failUnlessEqual(kSCNetworkConnectionPPPWaitingForRedial,  13)

        self.failUnlessEqual(kSCNetworkConnectionBytesIn, u"BytesIn")
        self.failUnlessEqual(kSCNetworkConnectionBytesOut, u"BytesOut")
        self.failUnlessEqual(kSCNetworkConnectionPacketsIn, u"PacketsIn")
        self.failUnlessEqual(kSCNetworkConnectionPacketsOut, u"PacketsOut")
        self.failUnlessEqual(kSCNetworkConnectionErrorsIn, u"ErrorsIn")
        self.failUnlessEqual(kSCNetworkConnectionErrorsOut, u"ErrorsOut")

    def testFunctions(self):
        v = SCNetworkConnectionGetTypeID()
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultIsBOOL(SCNetworkConnectionCopyUserPreferences)
        self.failUnlessArgIsOut(SCNetworkConnectionCopyUserPreferences, 1)
        self.failUnlessArgIsOut(SCNetworkConnectionCopyUserPreferences, 2)
        v,  servId, userOpts = SCNetworkConnectionCopyUserPreferences(None, None, None)
        if v:
            self.failUnlessIsInstance(servId, unicode)
            self.failUnlessIsInstance(userOpts, CFDictionaryRef)
        else:
            self.failUnless(servId is None)
            self.failUnless(userOpts is None)

        def callout(ref, status, info):
            pass
        ctx = object()
        v = SCNetworkConnectionCreateWithServiceID(None, "pyobjc.test.id", callout, ctx)

        self.failUnlessResultIsCFRetained(SCNetworkConnectionCopyServiceID)

        # FIXME: Need test for this
        SCNetworkConnectionGetStatus

        self.failUnlessResultIsCFRetained(SCNetworkConnectionCopyExtendedStatus)
        self.failUnlessResultIsCFRetained(SCNetworkConnectionCopyStatistics)
        self.failUnlessResultIsBOOL(SCNetworkConnectionStart)
        self.failUnlessResultIsBOOL(SCNetworkConnectionStop)
        self.failUnlessResultIsCFRetained(SCNetworkConnectionCopyUserOptions)
        self.failUnlessResultIsBOOL(SCNetworkConnectionScheduleWithRunLoop)
        self.failUnlessResultIsBOOL(SCNetworkConnectionUnscheduleFromRunLoop)


if __name__ == "__main__":
    main()
