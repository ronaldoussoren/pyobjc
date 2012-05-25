from PyObjCTools.TestSupport import *
from CFNetwork import *

try:
    long
except NameError:
    long = int

try:
    unicode
except NameError:
    unicode = str


class TestCFNetwork (TestCase):

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCFErrorDomainCFNetwork, unicode)
        self.assertIsInstance(kCFErrorDomainWinSock, unicode)
        self.assertIsInstance(kCFGetAddrInfoFailureKey, unicode)
        self.assertIsInstance(kCFSOCKSStatusCodeKey, unicode)
        self.assertIsInstance(kCFSOCKSVersionKey, unicode)
        self.assertIsInstance(kCFSOCKSNegotiationMethodKey, unicode)
        self.assertIsInstance(kCFDNSServiceFailureKey, unicode)
        self.assertIsInstance(kCFFTPStatusCodeKey, unicode)
        self.assertIsInstance(kCFURLErrorFailingURLErrorKey, unicode)
        self.assertIsInstance(kCFURLErrorFailingURLStringErrorKey, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCFErrorPACFileAuth, 309)
        self.assertEqual(kCFErrorHTTPSProxyConnectionFailure, 310)

        self.assertEqual(kCFURLErrorUnknown, -998)
        self.assertEqual(kCFURLErrorCancelled, -999)
        self.assertEqual(kCFURLErrorBadURL, -1000)
        self.assertEqual(kCFURLErrorTimedOut, -1001)
        self.assertEqual(kCFURLErrorUnsupportedURL, -1002)
        self.assertEqual(kCFURLErrorCannotFindHost, -1003)
        self.assertEqual(kCFURLErrorCannotConnectToHost, -1004)
        self.assertEqual(kCFURLErrorNetworkConnectionLost, -1005)
        self.assertEqual(kCFURLErrorDNSLookupFailed, -1006)
        self.assertEqual(kCFURLErrorHTTPTooManyRedirects, -1007)
        self.assertEqual(kCFURLErrorResourceUnavailable, -1008)
        self.assertEqual(kCFURLErrorNotConnectedToInternet, -1009)
        self.assertEqual(kCFURLErrorRedirectToNonExistentLocation, -1010)
        self.assertEqual(kCFURLErrorBadServerResponse, -1011)
        self.assertEqual(kCFURLErrorUserCancelledAuthentication, -1012)
        self.assertEqual(kCFURLErrorUserAuthenticationRequired, -1013)
        self.assertEqual(kCFURLErrorZeroByteResource, -1014)
        self.assertEqual(kCFURLErrorCannotDecodeRawData, -1015)
        self.assertEqual(kCFURLErrorCannotDecodeContentData, -1016)
        self.assertEqual(kCFURLErrorCannotParseResponse, -1017)
        self.assertEqual(kCFURLErrorInternationalRoamingOff, -1018)
        self.assertEqual(kCFURLErrorCallIsActive, -1019)
        self.assertEqual(kCFURLErrorDataNotAllowed, -1020)
        self.assertEqual(kCFURLErrorRequestBodyStreamExhausted, -1021)
        self.assertEqual(kCFURLErrorFileDoesNotExist, -1100)
        self.assertEqual(kCFURLErrorFileIsDirectory, -1101)
        self.assertEqual(kCFURLErrorNoPermissionsToReadFile, -1102)
        self.assertEqual(kCFURLErrorDataLengthExceedsMaximum, -1103)
        self.assertEqual(kCFURLErrorSecureConnectionFailed, -1200)
        self.assertEqual(kCFURLErrorServerCertificateHasBadDate, -1201)
        self.assertEqual(kCFURLErrorServerCertificateUntrusted, -1202)
        self.assertEqual(kCFURLErrorServerCertificateHasUnknownRoot, -1203)
        self.assertEqual(kCFURLErrorServerCertificateNotYetValid, -1204)
        self.assertEqual(kCFURLErrorClientCertificateRejected, -1205)
        self.assertEqual(kCFURLErrorClientCertificateRequired, -1206)
        self.assertEqual(kCFURLErrorCannotLoadFromNetwork, -2000)
        self.assertEqual(kCFURLErrorCannotCreateFile, -3000)
        self.assertEqual(kCFURLErrorCannotOpenFile, -3001)
        self.assertEqual(kCFURLErrorCannotCloseFile, -3002)
        self.assertEqual(kCFURLErrorCannotWriteToFile, -3003)
        self.assertEqual(kCFURLErrorCannotRemoveFile, -3004)
        self.assertEqual(kCFURLErrorCannotMoveFile, -3005)
        self.assertEqual(kCFURLErrorDownloadDecodingFailedMidStream, -3006)
        self.assertEqual(kCFURLErrorDownloadDecodingFailedToComplete, -3007)
        self.assertEqual(kCFHTTPCookieCannotParseCookieFile, -4000)



    def testConstants(self):
        self.assertEqual(kCFHostErrorHostNotFound, 1)
        self.assertEqual(kCFHostErrorUnknown, 2)
        self.assertEqual(kCFSOCKSErrorUnknownClientVersion, 100)
        self.assertEqual(kCFSOCKSErrorUnsupportedServerVersion, 101)
        self.assertEqual(kCFSOCKS4ErrorRequestFailed, 110)
        self.assertEqual(kCFSOCKS4ErrorIdentdFailed, 111)
        self.assertEqual(kCFSOCKS4ErrorIdConflict, 112)
        self.assertEqual(kCFSOCKS4ErrorUnknownStatusCode, 113)
        self.assertEqual(kCFSOCKS5ErrorBadState, 120)
        self.assertEqual(kCFSOCKS5ErrorBadResponseAddr, 121)
        self.assertEqual(kCFSOCKS5ErrorBadCredentials, 122)
        self.assertEqual(kCFSOCKS5ErrorUnsupportedNegotiationMethod, 123)
        self.assertEqual(kCFSOCKS5ErrorNoAcceptableMethod, 124)
        self.assertEqual(kCFNetServiceErrorUnknown, -72000)
        self.assertEqual(kCFNetServiceErrorCollision, -72001)
        self.assertEqual(kCFNetServiceErrorNotFound, -72002)
        self.assertEqual(kCFNetServiceErrorInProgress, -72003)
        self.assertEqual(kCFNetServiceErrorBadArgument, -72004)
        self.assertEqual(kCFNetServiceErrorCancel, -72005)
        self.assertEqual(kCFNetServiceErrorInvalid, -72006)
        self.assertEqual(kCFNetServiceErrorTimeout, -72007)
        self.assertEqual(kCFNetServiceErrorDNSServiceFailure, -73000)
        self.assertEqual(kCFFTPErrorUnexpectedStatusCode, 200)
        self.assertEqual(kCFErrorHTTPAuthenticationTypeUnsupported, 300)
        self.assertEqual(kCFErrorHTTPBadCredentials, 301)
        self.assertEqual(kCFErrorHTTPConnectionLost, 302)
        self.assertEqual(kCFErrorHTTPParseFailure, 303)
        self.assertEqual(kCFErrorHTTPRedirectionLoopDetected, 304)
        self.assertEqual(kCFErrorHTTPBadURL, 305)
        self.assertEqual(kCFErrorHTTPProxyConnectionFailure, 306)
        self.assertEqual(kCFErrorHTTPBadProxyCredentials, 307)
        self.assertEqual(kCFErrorPACFileError, 308)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(kCFStreamErrorHTTPSProxyFailureUnexpectedResponseToCONNECTMethod, 311)

if __name__ == "__main__":
    main()
