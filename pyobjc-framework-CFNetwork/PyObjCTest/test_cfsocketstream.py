import CFNetwork
from PyObjCTools.TestSupport import TestCase, min_os_level, os_release, os_level_key


class TestCFSocketStream(TestCase):
    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(
            CFNetwork.kCFStreamPropertyAllowExpensiveNetworkAccess, str
        )
        self.assertIsInstance(CFNetwork.kCFStreamPropertyConnectionIsExpensive, str)
        self.assertIsInstance(
            CFNetwork.kCFStreamPropertyAllowConstrainedNetworkAccess, str
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(CFNetwork.kCFStreamNetworkServiceTypeCallSignaling, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(CFNetwork.kCFStreamPropertySSLContext, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(CFNetwork.kCFStreamPropertyNoCellular, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyConnectionIsCellular, str)
        self.assertIsInstance(CFNetwork.kCFStreamNetworkServiceTypeResponsiveData, str)

        self.assertIsInstance(CFNetwork.kCFStreamNetworkServiceTypeAVStreaming, str)
        self.assertIsInstance(CFNetwork.kCFStreamNetworkServiceTypeResponsiveAV, str)

        self.assertIsInstance(CFNetwork.kCFStreamPropertyNoCellular, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyConnectionIsCellular, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(CFNetwork.kCFStreamNetworkServiceType, str)
        self.assertIsInstance(CFNetwork.kCFStreamNetworkServiceTypeVoIP, str)
        self.assertIsInstance(CFNetwork.kCFStreamNetworkServiceTypeVideo, str)
        self.assertIsInstance(CFNetwork.kCFStreamNetworkServiceTypeBackground, str)
        self.assertIsInstance(CFNetwork.kCFStreamNetworkServiceTypeVoice, str)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(CFNetwork.kCFStreamPropertySSLPeerTrust, str)
        self.assertIsInstance(CFNetwork.kCFStreamErrorDomainWinSock, int)

    def testConstants(self):
        self.assertIsInstance(CFNetwork.kCFStreamPropertySSLPeerCertificates, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertySSLSettings, str)
        self.assertIsInstance(CFNetwork.kCFStreamSSLLevel, str)
        self.assertIsInstance(CFNetwork.kCFStreamSSLAllowsExpiredCertificates, str)
        self.assertIsInstance(CFNetwork.kCFStreamSSLAllowsExpiredRoots, str)
        self.assertIsInstance(CFNetwork.kCFStreamSSLAllowsAnyRoot, str)
        self.assertIsInstance(CFNetwork.kCFStreamSSLValidatesCertificateChain, str)
        self.assertIsInstance(CFNetwork.kCFStreamSSLPeerName, str)
        self.assertIsInstance(CFNetwork.kCFStreamSSLCertificates, str)
        self.assertIsInstance(CFNetwork.kCFStreamSSLIsServer, str)

        self.assertEqual(CFNetwork.kCFStreamErrorSOCKSSubDomainNone, 0)
        self.assertEqual(CFNetwork.kCFStreamErrorSOCKSSubDomainVersionCode, 1)
        self.assertEqual(CFNetwork.kCFStreamErrorSOCKS4SubDomainResponse, 2)
        self.assertEqual(CFNetwork.kCFStreamErrorSOCKS5SubDomainUserPass, 3)
        self.assertEqual(CFNetwork.kCFStreamErrorSOCKS5SubDomainMethod, 4)
        self.assertEqual(CFNetwork.kCFStreamErrorSOCKS5SubDomainResponse, 5)
        self.assertEqual(CFNetwork.kCFStreamErrorSOCKS5BadResponseAddr, 1)
        self.assertEqual(CFNetwork.kCFStreamErrorSOCKS5BadState, 2)
        self.assertEqual(CFNetwork.kCFStreamErrorSOCKSUnknownClientVersion, 3)
        self.assertEqual(CFNetwork.kCFStreamErrorSOCKS4RequestFailed, 91)
        self.assertEqual(CFNetwork.kCFStreamErrorSOCKS4IdentdFailed, 92)
        self.assertEqual(CFNetwork.kCFStreamErrorSOCKS4IdConflict, 93)
        self.assertEqual(CFNetwork.kSOCKS5NoAcceptableMethod, 0xFF)

        # Moved to CoreFoundation in 10.14, still testing here for backward
        # compat reasons.
        self.assertIsInstance(CFNetwork.kCFStreamErrorDomainSOCKS, int)
        self.assertIsInstance(CFNetwork.kCFStreamPropertySOCKSProxy, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertySOCKSProxyHost, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertySOCKSProxyPort, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertySOCKSVersion, str)
        self.assertIsInstance(CFNetwork.kCFStreamSocketSOCKSVersion4, str)
        self.assertIsInstance(CFNetwork.kCFStreamSocketSOCKSVersion5, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertySOCKSUser, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertySOCKSPassword, str)
        self.assertIsInstance(CFNetwork.kCFStreamErrorDomainSSL, int)
        self.assertIsInstance(CFNetwork.kCFStreamPropertySocketSecurityLevel, str)
        self.assertIsInstance(CFNetwork.kCFStreamSocketSecurityLevelNone, str)
        self.assertIsInstance(CFNetwork.kCFStreamSocketSecurityLevelSSLv2, str)
        self.assertIsInstance(CFNetwork.kCFStreamSocketSecurityLevelSSLv3, str)
        self.assertIsInstance(CFNetwork.kCFStreamSocketSecurityLevelTLSv1, str)
        self.assertIsInstance(CFNetwork.kCFStreamSocketSecurityLevelNegotiatedSSL, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertyShouldCloseNativeSocket, str)
        #

        self.assertIsInstance(CFNetwork.kCFStreamPropertySocketRemoteHost, str)
        self.assertIsInstance(CFNetwork.kCFStreamPropertySocketRemoteNetService, str)
        self.assertEqual(CFNetwork.kCFStreamSocketSecurityNone, 0)
        self.assertEqual(CFNetwork.kCFStreamSocketSecuritySSLv2, 1)
        self.assertEqual(CFNetwork.kCFStreamSocketSecuritySSLv3, 2)
        self.assertEqual(CFNetwork.kCFStreamSocketSecuritySSLv23, 3)
        self.assertEqual(CFNetwork.kCFStreamSocketSecurityTLSv1, 4)

        self.assertIsInstance(CFNetwork.kCFStreamPropertyProxyLocalBypass, str)

    def testFunctions(self):
        err = CFNetwork.CFStreamError()
        err.error = (1 << 16) + 2

        v = CFNetwork.CFSocketStreamSOCKSGetErrorSubdomain(err)
        self.assertEqual(v, 1)

        v = CFNetwork.CFSocketStreamSOCKSGetError(err)
        self.assertEqual(v, 2)

        self.assertArgIsCFRetained(CFNetwork.CFStreamCreatePairWithSocketToCFHost, 3)
        self.assertArgIsCFRetained(CFNetwork.CFStreamCreatePairWithSocketToCFHost, 4)
        self.assertArgIsOut(CFNetwork.CFStreamCreatePairWithSocketToCFHost, 3)
        self.assertArgIsOut(CFNetwork.CFStreamCreatePairWithSocketToCFHost, 4)

        host = CFNetwork.CFHostCreateWithName(None, "connect.apple.com")
        rd, wr = CFNetwork.CFStreamCreatePairWithSocketToCFHost(
            None, host, 443, None, None
        )
        self.assertIsInstance(rd, CFNetwork.CFReadStreamRef)
        self.assertIsInstance(wr, CFNetwork.CFWriteStreamRef)

        if os_level_key(os_release()) < os_level_key("10.9"):
            self.assertResultIsBOOL(CFNetwork.CFSocketStreamPairSetSecurityProtocol)
            v = CFNetwork.CFSocketStreamPairSetSecurityProtocol(
                rd, wr, CFNetwork.kCFStreamSocketSecuritySSLv23
            )
            self.assertIsInstance(v, bool)

        self.assertArgIsCFRetained(
            CFNetwork.CFStreamCreatePairWithSocketToNetService, 2
        )
        self.assertArgIsCFRetained(
            CFNetwork.CFStreamCreatePairWithSocketToNetService, 3
        )
        self.assertArgIsOut(CFNetwork.CFStreamCreatePairWithSocketToNetService, 2)
        self.assertArgIsOut(CFNetwork.CFStreamCreatePairWithSocketToNetService, 3)
        service = CFNetwork.CFNetServiceCreate(
            None, "pyobjc.local", "ssh", "pyobjc.test.local", 9999
        )
        rd, wr = CFNetwork.CFStreamCreatePairWithSocketToNetService(
            None, service, None, None
        )
        self.assertIsInstance(rd, CFNetwork.CFReadStreamRef)
        self.assertIsInstance(wr, CFNetwork.CFWriteStreamRef)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(
            CFNetwork.kCFStreamPropertySocketExtendedBackgroundIdleMode, str
        )
