from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLError (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSURLErrorDomain, unicode)
        self.assertIsInstance(NSErrorFailingURLStringKey, unicode)

        self.assertEqual(NSURLErrorUnknown, -1)
        self.assertEqual(NSURLErrorCancelled, -999)
        self.assertEqual(NSURLErrorBadURL, -1000)
        self.assertEqual(NSURLErrorTimedOut, -1001)
        self.assertEqual(NSURLErrorUnsupportedURL, -1002)
        self.assertEqual(NSURLErrorCannotFindHost, -1003)
        self.assertEqual(NSURLErrorCannotConnectToHost, -1004)
        self.assertEqual(NSURLErrorNetworkConnectionLost, -1005)
        self.assertEqual(NSURLErrorDNSLookupFailed, -1006)
        self.assertEqual(NSURLErrorHTTPTooManyRedirects, -1007)
        self.assertEqual(NSURLErrorResourceUnavailable, -1008)
        self.assertEqual(NSURLErrorNotConnectedToInternet, -1009)
        self.assertEqual(NSURLErrorRedirectToNonExistentLocation, -1010)
        self.assertEqual(NSURLErrorBadServerResponse, -1011)
        self.assertEqual(NSURLErrorUserCancelledAuthentication, -1012)
        self.assertEqual(NSURLErrorUserAuthenticationRequired, -1013)
        self.assertEqual(NSURLErrorZeroByteResource, -1014)
        self.assertEqual(NSURLErrorCannotDecodeRawData, -1015)
        self.assertEqual(NSURLErrorCannotDecodeContentData, -1016)
        self.assertEqual(NSURLErrorCannotParseResponse, -1017)
        self.assertEqual(NSURLErrorFileDoesNotExist, -1100)
        self.assertEqual(NSURLErrorFileIsDirectory, -1101)
        self.assertEqual(NSURLErrorNoPermissionsToReadFile, -1102)
        self.assertEqual(NSURLErrorSecureConnectionFailed, -1200)
        self.assertEqual(NSURLErrorServerCertificateHasBadDate, -1201)
        self.assertEqual(NSURLErrorServerCertificateUntrusted, -1202)
        self.assertEqual(NSURLErrorServerCertificateHasUnknownRoot, -1203)
        self.assertEqual(NSURLErrorServerCertificateNotYetValid, -1204)
        self.assertEqual(NSURLErrorClientCertificateRejected, -1205)
        self.assertEqual(NSURLErrorCannotLoadFromNetwork, -2000)
        self.assertEqual(NSURLErrorCannotCreateFile, -3000)
        self.assertEqual(NSURLErrorCannotOpenFile, -3001)
        self.assertEqual(NSURLErrorCannotCloseFile, -3002)
        self.assertEqual(NSURLErrorCannotWriteToFile, -3003)
        self.assertEqual(NSURLErrorCannotRemoveFile, -3004)
        self.assertEqual(NSURLErrorCannotMoveFile, -3005)
        self.assertEqual(NSURLErrorDownloadDecodingFailedMidStream, -3006)
        self.assertEqual(NSURLErrorDownloadDecodingFailedToComplete, -3007)


    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertEqual(NSURLErrorDataLengthExceedsMaximum, -1103)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSURLErrorFailingURLErrorKey, unicode)
        self.assertIsInstance(NSURLErrorFailingURLStringErrorKey, unicode)

        self.assertEqual(NSURLErrorClientCertificateRequired, -1206)

if __name__ == "__main__":
    main()
