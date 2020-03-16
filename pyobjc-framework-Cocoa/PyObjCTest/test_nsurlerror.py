import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSURLError(TestCase):
    def testConstants(self):
        self.assertIsInstance(Foundation.NSURLErrorDomain, str)
        self.assertIsInstance(Foundation.NSErrorFailingURLStringKey, str)

        self.assertEqual(Foundation.NSURLErrorUnknown, -1)
        self.assertEqual(Foundation.NSURLErrorCancelled, -999)
        self.assertEqual(Foundation.NSURLErrorBadURL, -1000)
        self.assertEqual(Foundation.NSURLErrorTimedOut, -1001)
        self.assertEqual(Foundation.NSURLErrorUnsupportedURL, -1002)
        self.assertEqual(Foundation.NSURLErrorCannotFindHost, -1003)
        self.assertEqual(Foundation.NSURLErrorCannotConnectToHost, -1004)
        self.assertEqual(Foundation.NSURLErrorNetworkConnectionLost, -1005)
        self.assertEqual(Foundation.NSURLErrorDNSLookupFailed, -1006)
        self.assertEqual(Foundation.NSURLErrorHTTPTooManyRedirects, -1007)
        self.assertEqual(Foundation.NSURLErrorResourceUnavailable, -1008)
        self.assertEqual(Foundation.NSURLErrorNotConnectedToInternet, -1009)
        self.assertEqual(Foundation.NSURLErrorRedirectToNonExistentLocation, -1010)
        self.assertEqual(Foundation.NSURLErrorBadServerResponse, -1011)
        self.assertEqual(Foundation.NSURLErrorUserCancelledAuthentication, -1012)
        self.assertEqual(Foundation.NSURLErrorUserAuthenticationRequired, -1013)
        self.assertEqual(Foundation.NSURLErrorZeroByteResource, -1014)
        self.assertEqual(Foundation.NSURLErrorCannotDecodeRawData, -1015)
        self.assertEqual(Foundation.NSURLErrorCannotDecodeContentData, -1016)
        self.assertEqual(Foundation.NSURLErrorCannotParseResponse, -1017)
        self.assertEqual(Foundation.NSURLErrorFileDoesNotExist, -1100)
        self.assertEqual(Foundation.NSURLErrorFileIsDirectory, -1101)
        self.assertEqual(Foundation.NSURLErrorNoPermissionsToReadFile, -1102)
        self.assertEqual(Foundation.NSURLErrorSecureConnectionFailed, -1200)
        self.assertEqual(Foundation.NSURLErrorServerCertificateHasBadDate, -1201)
        self.assertEqual(Foundation.NSURLErrorServerCertificateUntrusted, -1202)
        self.assertEqual(Foundation.NSURLErrorServerCertificateHasUnknownRoot, -1203)
        self.assertEqual(Foundation.NSURLErrorServerCertificateNotYetValid, -1204)
        self.assertEqual(Foundation.NSURLErrorClientCertificateRejected, -1205)
        self.assertEqual(Foundation.NSURLErrorCannotLoadFromNetwork, -2000)
        self.assertEqual(Foundation.NSURLErrorCannotCreateFile, -3000)
        self.assertEqual(Foundation.NSURLErrorCannotOpenFile, -3001)
        self.assertEqual(Foundation.NSURLErrorCannotCloseFile, -3002)
        self.assertEqual(Foundation.NSURLErrorCannotWriteToFile, -3003)
        self.assertEqual(Foundation.NSURLErrorCannotRemoveFile, -3004)
        self.assertEqual(Foundation.NSURLErrorCannotMoveFile, -3005)
        self.assertEqual(Foundation.NSURLErrorDownloadDecodingFailedMidStream, -3006)
        self.assertEqual(Foundation.NSURLErrorDownloadDecodingFailedToComplete, -3007)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(Foundation.NSURLErrorDataLengthExceedsMaximum, -1103)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Foundation.NSURLErrorFailingURLPeerTrustErrorKey, str)
        self.assertIsInstance(Foundation.NSURLErrorFailingURLErrorKey, str)
        self.assertIsInstance(Foundation.NSURLErrorFailingURLStringErrorKey, str)

        self.assertEqual(Foundation.NSURLErrorClientCertificateRequired, -1206)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(Foundation.NSURLErrorInternationalRoamingOff, -1018)
        self.assertEqual(Foundation.NSURLErrorCallIsActive, -1019)
        self.assertEqual(Foundation.NSURLErrorDataNotAllowed, -1020)
        self.assertEqual(Foundation.NSURLErrorRequestBodyStreamExhausted, -1021)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(
            Foundation.NSURLErrorBackgroundTaskCancelledReasonKey, str
        )

        self.assertEqual(
            Foundation.NSURLErrorCancelledReasonUserForceQuitApplication, 0
        )
        self.assertEqual(
            Foundation.NSURLErrorCancelledReasonBackgroundUpdatesDisabled, 1
        )
        self.assertEqual(
            Foundation.NSURLErrorCancelledReasonInsufficientSystemResources, 2
        )

        self.assertEqual(
            Foundation.NSURLErrorBackgroundSessionRequiresSharedContainer, -995
        )
        self.assertEqual(
            Foundation.NSURLErrorBackgroundSessionInUseByAnotherProcess, -996
        )
        self.assertEqual(Foundation.NSURLErrorBackgroundSessionWasDisconnected, -997)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(
            Foundation.NSURLErrorAppTransportSecurityRequiresSecureConnection, -1022
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertEqual(Foundation.NSURLErrorFileOutsideSafeArea, -1104)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(Foundation.NSURLErrorNetworkUnavailableReasonKey, str)

        self.assertEqual(Foundation.NSURLErrorNetworkUnavailableReasonCellular, 0)
        self.assertEqual(Foundation.NSURLErrorNetworkUnavailableReasonExpensive, 1)
        self.assertEqual(Foundation.NSURLErrorNetworkUnavailableReasonConstrained, 2)
