from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVContentKeySessionHelper(AVFoundation.NSObject):
    def contentKeySession_shouldRetryContentKeyRequest_reason_(self, a, b, c):
        return 1

    def mayRequireContentKeysForMediaDataProcessing(self):
        return 1


class TestAVContentKeySession(TestCase):
    @min_os_level("10.12.4")
    def testConstants10_12_4(self):
        self.assertIsInstance(AVFoundation.AVContentKeySystemFairPlayStreaming, unicode)

        self.assertIsInstance(
            AVFoundation.AVContentKeyRequestRetryReasonTimedOut, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVContentKeyRequestRetryReasonReceivedResponseWithExpiredLease,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVContentKeyRequestRetryReasonReceivedObsoleteContentKey,
            unicode,
        )

        self.assertEqual(AVFoundation.AVContentKeyRequestStatusRequestingResponse, 0)
        self.assertEqual(AVFoundation.AVContentKeyRequestStatusReceivedResponse, 1)
        self.assertEqual(AVFoundation.AVContentKeyRequestStatusRenewed, 2)
        self.assertEqual(AVFoundation.AVContentKeyRequestStatusRetried, 3)
        self.assertEqual(AVFoundation.AVContentKeyRequestStatusCancelled, 4)
        self.assertEqual(AVFoundation.AVContentKeyRequestStatusFailed, 5)

        self.assertIsInstance(
            AVFoundation.AVContentKeyRequestProtocolVersionsKey, unicode
        )

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVContentKeySystemClearKey, unicode)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVContentKeySystemAuthorizationToken, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVContentKeySessionServerPlaybackContextOptionProtocolVersions,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVContentKeySessionServerPlaybackContextOptionServerChallenge,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVContentKeyRequestRequiresValidationDataInSecureTokenKey,
            unicode,
        )

    def testMethods(self):
        self.assertResultIsBOOL(
            TestAVContentKeySessionHelper.contentKeySession_shouldRetryContentKeyRequest_reason_
        )
        self.assertResultIsBOOL(
            TestAVContentKeySessionHelper.mayRequireContentKeysForMediaDataProcessing
        )

    @min_os_level("10.12.4")
    def testMethods10_12_4(self):
        self.assertResultIsBOOL(
            AVFoundation.AVContentKeyRequest.canProvidePersistableContentKey
        )
        self.assertArgIsBlock(
            AVFoundation.AVContentKeyRequest.makeStreamingContentKeyRequestDataForApp_contentIdentifier_options_completionHandler_,
            3,
            b"v@@",
        )

        self.assertResultIsBOOL(
            AVFoundation.AVContentKeyRequest.respondByRequestingPersistableContentKeyRequestAndReturnError_
        )
        self.assertArgIsOut(
            AVFoundation.AVContentKeyRequest.respondByRequestingPersistableContentKeyRequestAndReturnError_,
            0,
        )

    @expectedFailure
    @min_os_level("10.14")
    def testMethods10_14(self):
        # Documented as available...
        self.assertResultIsBOOL(
            AVFoundation.AVContentKeyRequest.renewsExpiringResponseData
        )

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsBlock(
            AVFoundation.AVContentKeySession.makeSecureTokenForExpirationDateOfPersistableContentKey_completionHandler_,
            1,
            b"v@@",
        )

        self.assertResultIsBOOL(
            AVFoundation.AVContentKeyRequest.respondByRequestingPersistableContentKeyRequestAndReturnError_
        )
        self.assertArgIsOut(
            AVFoundation.AVContentKeyRequest.respondByRequestingPersistableContentKeyRequestAndReturnError_,
            0,
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            AVFoundation.AVContentKeySession.invalidatePersistableContentKey_options_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            AVFoundation.AVContentKeySession.invalidateAllPersistableContentKeysForApp_options_completionHandler_,
            2,
            b"v@@",
        )

    @min_sdk_level("10.12.4")
    def testProtocols(self):
        objc.protocolNamed("AVContentKeySessionDelegate")
        objc.protocolNamed("AVContentKeyRecipient")


if __name__ == "__main__":
    main()
