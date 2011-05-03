from PyObjCTools.TestSupport import *
from CFNetwork import *


class TestCFSocketStream (TestCase):
    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCFStreamPropertySSLPeerTrust, unicode)
        self.assertIsInstance(kCFStreamErrorDomainWinSock, (int, long))

    def testConstants(self):
        self.assertIsInstance(kCFStreamPropertySSLPeerCertificates, unicode)

        self.assertIsInstance(kCFStreamPropertySSLPeerCertificates, unicode)
        self.assertIsInstance(kCFStreamPropertySSLSettings, unicode)
        self.assertIsInstance(kCFStreamSSLLevel, unicode)
        self.assertIsInstance(kCFStreamSSLAllowsExpiredCertificates, unicode)
        self.assertIsInstance(kCFStreamSSLAllowsExpiredRoots, unicode)
        self.assertIsInstance(kCFStreamSSLAllowsAnyRoot, unicode)
        self.assertIsInstance(kCFStreamSSLValidatesCertificateChain, unicode)
        self.assertIsInstance(kCFStreamSSLPeerName, unicode)
        self.assertIsInstance(kCFStreamSSLCertificates, unicode)
        self.assertIsInstance(kCFStreamSSLIsServer, unicode)
        self.assertIsInstance(kCFStreamErrorDomainSOCKS, (int, long))

        self.assertEqual(kCFStreamErrorSOCKSSubDomainNone, 0)
        self.assertEqual(kCFStreamErrorSOCKSSubDomainVersionCode, 1)
        self.assertEqual(kCFStreamErrorSOCKS4SubDomainResponse, 2)
        self.assertEqual(kCFStreamErrorSOCKS5SubDomainUserPass, 3)
        self.assertEqual(kCFStreamErrorSOCKS5SubDomainMethod, 4)
        self.assertEqual(kCFStreamErrorSOCKS5SubDomainResponse, 5)
        self.assertEqual(kCFStreamErrorSOCKS5BadResponseAddr, 1)
        self.assertEqual(kCFStreamErrorSOCKS5BadState, 2)
        self.assertEqual(kCFStreamErrorSOCKSUnknownClientVersion, 3)
        self.assertEqual(kCFStreamErrorSOCKS4RequestFailed, 91)
        self.assertEqual(kCFStreamErrorSOCKS4IdentdFailed, 92)
        self.assertEqual(kCFStreamErrorSOCKS4IdConflict, 93)
        self.assertEqual(kSOCKS5NoAcceptableMethod, 0xFF)

        self.assertIsInstance(kCFStreamPropertySOCKSProxyHost, unicode)
        self.assertIsInstance(kCFStreamPropertySOCKSProxyPort, unicode)
        self.assertIsInstance(kCFStreamPropertySOCKSVersion, unicode)
        self.assertIsInstance(kCFStreamSocketSOCKSVersion4, unicode)
        self.assertIsInstance(kCFStreamSocketSOCKSVersion5, unicode)
        self.assertIsInstance(kCFStreamPropertySOCKSUser, unicode)
        self.assertIsInstance(kCFStreamPropertySOCKSPassword, unicode)
        self.assertIsInstance(kCFStreamErrorDomainSSL, (int, long))
        self.assertIsInstance(kCFStreamPropertySocketSecurityLevel, unicode)
        self.assertIsInstance(kCFStreamSocketSecurityLevelNone, unicode)
        self.assertIsInstance(kCFStreamSocketSecurityLevelSSLv2, unicode)
        self.assertIsInstance(kCFStreamSocketSecurityLevelSSLv3, unicode)
        self.assertIsInstance(kCFStreamSocketSecurityLevelTLSv1, unicode)
        self.assertIsInstance(kCFStreamSocketSecurityLevelNegotiatedSSL, unicode)
        self.assertIsInstance(kCFStreamPropertyShouldCloseNativeSocket, unicode)
        self.assertIsInstance(kCFStreamPropertySocketRemoteHost, unicode)
        self.assertIsInstance(kCFStreamPropertySocketRemoteNetService, unicode)
        self.assertEqual(kCFStreamSocketSecurityNone, 0)
        self.assertEqual(kCFStreamSocketSecuritySSLv2, 1)
        self.assertEqual(kCFStreamSocketSecuritySSLv3, 2)
        self.assertEqual(kCFStreamSocketSecuritySSLv23, 3)
        self.assertEqual(kCFStreamSocketSecurityTLSv1, 4)

        self.assertIsInstance(kCFStreamPropertyProxyLocalBypass, unicode)

    def testFunctions(self):
        err = CFStreamError()
        err.error = (1<<16)+2

        v = CFSocketStreamSOCKSGetErrorSubdomain(err)
        self.assertEqual(v, 1)

        v = CFSocketStreamSOCKSGetError(err)
        self.assertEqual(v, 2)

        self.assertArgIsCFRetained(CFStreamCreatePairWithSocketToCFHost, 3)
        self.assertArgIsCFRetained(CFStreamCreatePairWithSocketToCFHost, 4)
        self.assertArgIsOut(CFStreamCreatePairWithSocketToCFHost, 3)
        self.assertArgIsOut(CFStreamCreatePairWithSocketToCFHost, 4)

        host = CFHostCreateWithName(None, u"connect.apple.com")
        rd, wr = CFStreamCreatePairWithSocketToCFHost(None, host, 443, None, None)
        self.assertIsInstance(rd, CFReadStreamRef)
        self.assertIsInstance(wr, CFWriteStreamRef)

        self.assertResultIsBOOL(CFSocketStreamPairSetSecurityProtocol)
        v = CFSocketStreamPairSetSecurityProtocol(rd, wr, kCFStreamSocketSecuritySSLv23)
        self.assertIsInstance(v, bool)

        self.assertArgIsCFRetained(CFStreamCreatePairWithSocketToNetService, 2)
        self.assertArgIsCFRetained(CFStreamCreatePairWithSocketToNetService, 3)
        self.assertArgIsOut(CFStreamCreatePairWithSocketToNetService, 2)
        self.assertArgIsOut(CFStreamCreatePairWithSocketToNetService, 3)
        service = CFNetServiceCreate(None, u"pyobjc.local", u"ssh", u"pyobjc.test.local", 9999)
        rd, wr = CFStreamCreatePairWithSocketToNetService(None, service, None, None)
        self.assertIsInstance(rd, CFReadStreamRef)
        self.assertIsInstance(wr, CFWriteStreamRef)




if __name__ == "__main__":
    main()
