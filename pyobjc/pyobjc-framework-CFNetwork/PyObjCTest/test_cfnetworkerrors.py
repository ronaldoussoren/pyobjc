from PyObjCTools.TestSupport import *
from CFNetwork import *


class TestCFNetwork (TestCase):

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(kCFErrorDomainCFNetwork, unicode)
        self.failUnlessIsInstance(kCFErrorDomainWinSock, unicode)
        self.failUnlessIsInstance(kCFGetAddrInfoFailureKey, unicode)
        self.failUnlessIsInstance(kCFSOCKSStatusCodeKey, unicode)
        self.failUnlessIsInstance(kCFSOCKSVersionKey, unicode)
        self.failUnlessIsInstance(kCFSOCKSNegotiationMethodKey, unicode)
        self.failUnlessIsInstance(kCFDNSServiceFailureKey, unicode)
        self.failUnlessIsInstance(kCFFTPStatusCodeKey, unicode)

    def testConstants(self):
        self.failUnlessEqual(kCFHostErrorHostNotFound, 1)
        self.failUnlessEqual(kCFHostErrorUnknown, 2)
        self.failUnlessEqual(kCFSOCKSErrorUnknownClientVersion, 100)
        self.failUnlessEqual(kCFSOCKSErrorUnsupportedServerVersion, 101)
        self.failUnlessEqual(kCFSOCKS4ErrorRequestFailed, 110)
        self.failUnlessEqual(kCFSOCKS4ErrorIdentdFailed, 111)
        self.failUnlessEqual(kCFSOCKS4ErrorIdConflict, 112)
        self.failUnlessEqual(kCFSOCKS4ErrorUnknownStatusCode, 113)
        self.failUnlessEqual(kCFSOCKS5ErrorBadState, 120)
        self.failUnlessEqual(kCFSOCKS5ErrorBadResponseAddr, 121)
        self.failUnlessEqual(kCFSOCKS5ErrorBadCredentials, 122)
        self.failUnlessEqual(kCFSOCKS5ErrorUnsupportedNegotiationMethod, 123)
        self.failUnlessEqual(kCFSOCKS5ErrorNoAcceptableMethod, 124)
        self.failUnlessEqual(kCFNetServiceErrorUnknown, -72000)
        self.failUnlessEqual(kCFNetServiceErrorCollision, -72001)
        self.failUnlessEqual(kCFNetServiceErrorNotFound, -72002)
        self.failUnlessEqual(kCFNetServiceErrorInProgress, -72003)
        self.failUnlessEqual(kCFNetServiceErrorBadArgument, -72004)
        self.failUnlessEqual(kCFNetServiceErrorCancel, -72005)
        self.failUnlessEqual(kCFNetServiceErrorInvalid, -72006)
        self.failUnlessEqual(kCFNetServiceErrorTimeout, -72007)
        self.failUnlessEqual(kCFNetServiceErrorDNSServiceFailure, -73000)
        self.failUnlessEqual(kCFFTPErrorUnexpectedStatusCode, 200)
        self.failUnlessEqual(kCFErrorHTTPAuthenticationTypeUnsupported, 300)
        self.failUnlessEqual(kCFErrorHTTPBadCredentials, 301)
        self.failUnlessEqual(kCFErrorHTTPConnectionLost, 302)
        self.failUnlessEqual(kCFErrorHTTPParseFailure, 303)
        self.failUnlessEqual(kCFErrorHTTPRedirectionLoopDetected, 304)
        self.failUnlessEqual(kCFErrorHTTPBadURL, 305)
        self.failUnlessEqual(kCFErrorHTTPProxyConnectionFailure, 306)
        self.failUnlessEqual(kCFErrorHTTPBadProxyCredentials, 307)
        self.failUnlessEqual(kCFErrorPACFileError, 308)

if __name__ == "__main__":
    main()
