from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSURLError (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSURLErrorDomain, unicode)
        self.failUnlessIsInstance(NSErrorFailingURLStringKey, unicode)

        self.failUnlessEqual(NSURLErrorUnknown, -1)
        self.failUnlessEqual(NSURLErrorCancelled, -999)
        self.failUnlessEqual(NSURLErrorBadURL, -1000)
        self.failUnlessEqual(NSURLErrorTimedOut, -1001)
        self.failUnlessEqual(NSURLErrorUnsupportedURL, -1002)
        self.failUnlessEqual(NSURLErrorCannotFindHost, -1003)
        self.failUnlessEqual(NSURLErrorCannotConnectToHost, -1004)
        self.failUnlessEqual(NSURLErrorNetworkConnectionLost, -1005)
        self.failUnlessEqual(NSURLErrorDNSLookupFailed, -1006)
        self.failUnlessEqual(NSURLErrorHTTPTooManyRedirects, -1007)
        self.failUnlessEqual(NSURLErrorResourceUnavailable, -1008)
        self.failUnlessEqual(NSURLErrorNotConnectedToInternet, -1009)
        self.failUnlessEqual(NSURLErrorRedirectToNonExistentLocation, -1010)
        self.failUnlessEqual(NSURLErrorBadServerResponse, -1011)
        self.failUnlessEqual(NSURLErrorUserCancelledAuthentication, -1012)
        self.failUnlessEqual(NSURLErrorUserAuthenticationRequired, -1013)
        self.failUnlessEqual(NSURLErrorZeroByteResource, -1014)
        self.failUnlessEqual(NSURLErrorCannotDecodeRawData, -1015)
        self.failUnlessEqual(NSURLErrorCannotDecodeContentData, -1016)
        self.failUnlessEqual(NSURLErrorCannotParseResponse, -1017)
        self.failUnlessEqual(NSURLErrorFileDoesNotExist, -1100)
        self.failUnlessEqual(NSURLErrorFileIsDirectory, -1101)
        self.failUnlessEqual(NSURLErrorNoPermissionsToReadFile, -1102)
        self.failUnlessEqual(NSURLErrorSecureConnectionFailed, -1200)
        self.failUnlessEqual(NSURLErrorServerCertificateHasBadDate, -1201)
        self.failUnlessEqual(NSURLErrorServerCertificateUntrusted, -1202)
        self.failUnlessEqual(NSURLErrorServerCertificateHasUnknownRoot, -1203)
        self.failUnlessEqual(NSURLErrorServerCertificateNotYetValid, -1204)
        self.failUnlessEqual(NSURLErrorClientCertificateRejected, -1205)
        self.failUnlessEqual(NSURLErrorCannotLoadFromNetwork, -2000)
        self.failUnlessEqual(NSURLErrorCannotCreateFile, -3000)
        self.failUnlessEqual(NSURLErrorCannotOpenFile, -3001)
        self.failUnlessEqual(NSURLErrorCannotCloseFile, -3002)
        self.failUnlessEqual(NSURLErrorCannotWriteToFile, -3003)
        self.failUnlessEqual(NSURLErrorCannotRemoveFile, -3004)
        self.failUnlessEqual(NSURLErrorCannotMoveFile, -3005)
        self.failUnlessEqual(NSURLErrorDownloadDecodingFailedMidStream, -3006)
        self.failUnlessEqual(NSURLErrorDownloadDecodingFailedToComplete, -3007)


    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessEqual(NSURLErrorDataLengthExceedsMaximum, -1103)

if __name__ == "__main__":
    main()
