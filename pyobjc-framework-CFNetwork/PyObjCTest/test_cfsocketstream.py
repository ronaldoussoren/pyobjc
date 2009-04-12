from PyObjCTools.TestSupport import *
from CFNetwork import *


class TestCFSocketStream (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kCFStreamPropertySSLPeerCertificates, unicode)
        self.failUnlessIsInstance(kCFStreamPropertySSLSettings, unicode)
        self.failUnlessIsInstance(kCFStreamSSLLevel, unicode)
        self.failUnlessIsInstance(kCFStreamSSLAllowsExpiredCertificates, unicode)
        self.failUnlessIsInstance(kCFStreamSSLAllowsExpiredRoots, unicode)
        self.failUnlessIsInstance(kCFStreamSSLAllowsAnyRoot, unicode)
        self.failUnlessIsInstance(kCFStreamSSLValidatesCertificateChain, unicode)
        self.failUnlessIsInstance(kCFStreamSSLPeerName, unicode)
        self.failUnlessIsInstance(kCFStreamSSLCertificates, unicode)
        self.failUnlessIsInstance(kCFStreamSSLIsServer, unicode)
        self.failUnlessIsInstance(kCFStreamErrorDomainWinSock, (int, long))
        self.failUnlessIsInstance(kCFStreamErrorDomainSOCKS, (int, long))

        self.failUnlessEqual(kCFStreamErrorSOCKSSubDomainNone, 0)
        self.failUnlessEqual(kCFStreamErrorSOCKSSubDomainVersionCode, 1)
        self.failUnlessEqual(kCFStreamErrorSOCKS4SubDomainResponse, 2)
        self.failUnlessEqual(kCFStreamErrorSOCKS5SubDomainUserPass, 3)
        self.failUnlessEqual(kCFStreamErrorSOCKS5SubDomainMethod, 4)
        self.failUnlessEqual(kCFStreamErrorSOCKS5SubDomainResponse, 5)
        self.failUnlessEqual(kCFStreamErrorSOCKS5BadResponseAddr, 1)
        self.failUnlessEqual(kCFStreamErrorSOCKS5BadState, 2)
        self.failUnlessEqual(kCFStreamErrorSOCKSUnknownClientVersion, 3)
        self.failUnlessEqual(kCFStreamErrorSOCKS4RequestFailed, 91)
        self.failUnlessEqual(kCFStreamErrorSOCKS4IdentdFailed, 92)
        self.failUnlessEqual(kCFStreamErrorSOCKS4IdConflict, 93)
        self.failUnlessEqual(kSOCKS5NoAcceptableMethod, 0xFF)

        self.failUnlessIsInstance(kCFStreamPropertySOCKSProxyHost, unicode)
        self.failUnlessIsInstance(kCFStreamPropertySOCKSProxyPort, unicode)
        self.failUnlessIsInstance(kCFStreamPropertySOCKSVersion, unicode)
        self.failUnlessIsInstance(kCFStreamSocketSOCKSVersion4, unicode)
        self.failUnlessIsInstance(kCFStreamSocketSOCKSVersion5, unicode)
        self.failUnlessIsInstance(kCFStreamPropertySOCKSUser, unicode)
        self.failUnlessIsInstance(kCFStreamPropertySOCKSPassword, unicode)
        self.failUnlessIsInstance(kCFStreamErrorDomainSSL, (int, long))
        self.failUnlessIsInstance(kCFStreamPropertySocketSecurityLevel, unicode)
        self.failUnlessIsInstance(kCFStreamSocketSecurityLevelNone, unicode)
        self.failUnlessIsInstance(kCFStreamSocketSecurityLevelSSLv2, unicode)
        self.failUnlessIsInstance(kCFStreamSocketSecurityLevelSSLv3, unicode)
        self.failUnlessIsInstance(kCFStreamSocketSecurityLevelTLSv1, unicode)
        self.failUnlessIsInstance(kCFStreamSocketSecurityLevelNegotiatedSSL, unicode)
        self.failUnlessIsInstance(kCFStreamPropertyShouldCloseNativeSocket, unicode)
        self.failUnlessIsInstance(kCFStreamPropertySocketRemoteHost, unicode)
        self.failUnlessIsInstance(kCFStreamPropertySocketRemoteNetService, unicode)
        self.failUnlessEqual(kCFStreamSocketSecurityNone, 0)
        self.failUnlessEqual(kCFStreamSocketSecuritySSLv2, 1)
        self.failUnlessEqual(kCFStreamSocketSecuritySSLv3, 2)
        self.failUnlessEqual(kCFStreamSocketSecuritySSLv23, 3)
        self.failUnlessEqual(kCFStreamSocketSecurityTLSv1, 4)

        self.failUnlessIsInstance(kCFStreamPropertyProxyLocalBypass, unicode)

    def testFunctions(self):
        err = CFStreamError()
        err.error = (1<<16)+2

        v = CFSocketStreamSOCKSGetErrorSubdomain(err)
        self.failUnlessEqual(v, 1)

        v = CFSocketStreamSOCKSGetError(err)
        self.failUnlessEqual(v, 2)

        self.failUnlessArgIsCFRetained(CFStreamCreatePairWithSocketToCFHost, 3)
        self.failUnlessArgIsCFRetained(CFStreamCreatePairWithSocketToCFHost, 4)
        self.failUnlessArgIsOut(CFStreamCreatePairWithSocketToCFHost, 3)
        self.failUnlessArgIsOut(CFStreamCreatePairWithSocketToCFHost, 4)

        host = CFHostCreateWithName(None, u"connect.apple.com")
        rd, wr = CFStreamCreatePairWithSocketToCFHost(None, host, 443, None, None)
        self.failUnlessIsInstance(rd, CFReadStreamRef)
        self.failUnlessIsInstance(wr, CFWriteStreamRef)

        self.failUnlessResultIsBOOL(CFSocketStreamPairSetSecurityProtocol)
        v = CFSocketStreamPairSetSecurityProtocol(rd, wr, kCFStreamSocketSecuritySSLv23)
        self.failUnlessIsInstance(v, bool)

        self.failUnlessArgIsCFRetained(CFStreamCreatePairWithSocketToNetService, 2)
        self.failUnlessArgIsCFRetained(CFStreamCreatePairWithSocketToNetService, 3)
        self.failUnlessArgIsOut(CFStreamCreatePairWithSocketToNetService, 2)
        self.failUnlessArgIsOut(CFStreamCreatePairWithSocketToNetService, 3)
        service = CFNetServiceCreate(None, u"pyobjc.local", u"ssh", u"pyobjc.test.local", 9999)
        rd, wr = CFStreamCreatePairWithSocketToNetService(None, service, None, None)
        self.failUnlessIsInstance(rd, CFReadStreamRef)
        self.failUnlessIsInstance(wr, CFWriteStreamRef)




if __name__ == "__main__":
    main()
