import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
from PyObjCTools.TestSupport import expectedFailure


class TestAVContentKeySessionHelper(AVFoundation.NSObject):
    def contentKeySession_shouldRetryContentKeyRequest_reason_(self, a, b, c):
        return 1

    def mayRequireContentKeysForMediaDataProcessing(self):
        return 1


class TestAVContentKeySession(TestCase):
    @min_os_level("10.12.4")
    def testConstants10_12_4(self):
        self.assertIsInstance(
            AVFoundation.AVContentKeySystemFairPlayStreaming, str
        )  # noqa: B950

        self.assertIsInstance(
            AVFoundation.AVContentKeyRequestRetryReasonTimedOut, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVContentKeyRequestRetryReasonReceivedResponseWithExpiredLease,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVContentKeyRequestRetryReasonReceivedObsoleteContentKey,
            str,  # noqa: B950
        )

        self.assertEqual(
            AVFoundation.AVContentKeyRequestStatusRequestingResponse, 0
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVContentKeyRequestStatusReceivedResponse, 1
        )  # noqa: B950
        self.assertEqual(AVFoundation.AVContentKeyRequestStatusRenewed, 2)
        self.assertEqual(AVFoundation.AVContentKeyRequestStatusRetried, 3)
        self.assertEqual(AVFoundation.AVContentKeyRequestStatusCancelled, 4)
        self.assertEqual(AVFoundation.AVContentKeyRequestStatusFailed, 5)

        self.assertIsInstance(
            AVFoundation.AVContentKeyRequestProtocolVersionsKey, str
        )  # noqa: B950

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVContentKeySystemClearKey, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVContentKeySystemAuthorizationToken, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVContentKeySessionServerPlaybackContextOptionProtocolVersions,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVContentKeySessionServerPlaybackContextOptionServerChallenge,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVContentKeyRequestRequiresValidationDataInSecureTokenKey,
            str,  # noqa: B950
        )

    def testMethods(self):
        self.assertResultIsBOOL(
            TestAVContentKeySessionHelper.contentKeySession_shouldRetryContentKeyRequest_reason_  # noqa: B950
        )
        self.assertResultIsBOOL(
            TestAVContentKeySessionHelper.mayRequireContentKeysForMediaDataProcessing  # noqa: B950
        )

    @min_os_level("10.12.4")
    def testMethods10_12_4(self):
        self.assertResultIsBOOL(
            AVFoundation.AVContentKeyRequest.canProvidePersistableContentKey
        )
        self.assertArgIsBlock(
            AVFoundation.AVContentKeyRequest.makeStreamingContentKeyRequestDataForApp_contentIdentifier_options_completionHandler_,  # noqa: B950
            3,
            b"v@@",
        )

        self.assertResultIsBOOL(
            AVFoundation.AVContentKeyRequest.respondByRequestingPersistableContentKeyRequestAndReturnError_  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVContentKeyRequest.respondByRequestingPersistableContentKeyRequestAndReturnError_,  # noqa: B950
            0,
        )

    @expectedFailure
    @min_os_level("10.14")
    def testMethods10_14(self):
        # Documented as available...
        self.assertResultIsBOOL(
            AVFoundation.AVContentKeyRequest.renewsExpiringResponseData
        )

    @min_os_level("10.12.4")
    def testMethods10_5(self):
        self.assertArgIsBlock(
            AVFoundation.AVContentKeySession.makeSecureTokenForExpirationDateOfPersistableContentKey_completionHandler_,  # noqa: B950
            1,
            b"v@@",
        )

        self.assertResultIsBOOL(
            AVFoundation.AVContentKeyRequest.respondByRequestingPersistableContentKeyRequestAndReturnError_  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVContentKeyRequest.respondByRequestingPersistableContentKeyRequestAndReturnError_,  # noqa: B950
            0,
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            AVFoundation.AVContentKeySession.invalidatePersistableContentKey_options_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            AVFoundation.AVContentKeySession.invalidateAllPersistableContentKeysForApp_options_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )

    @min_sdk_level("10.12.4")
    def testProtocols(self):
        objc.protocolNamed("AVContentKeySessionDelegate")
        objc.protocolNamed("AVContentKeyRecipient")
