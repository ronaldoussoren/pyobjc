import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetResourceLoaderHelper(AVFoundation.NSObject):
    def resourceLoader_shouldWaitForLoadingOfRequestedResource_(self, rl, r):
        return 1

    def resourceLoader_shouldWaitForRenewalOfRequestedResource_(self, rl, r):
        return 1

    def resourceLoader_shouldWaitForResponseToAuthenticationChallenge_(
        self, rl, r
    ):  # noqa: B950
        return 1


class TestAVAssetResourceLoader(TestCase):
    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(
            AVFoundation.AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey,  # noqa: B950
            str,
        )

    @min_os_level("10.9")
    def testProtocols(self):
        self.assertProtocolExists("AVAssetResourceLoaderDelegate")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestAVAssetResourceLoaderHelper.resourceLoader_shouldWaitForLoadingOfRequestedResource_,  # noqa: B950
            objc._C_NSBOOL,
        )

    @min_os_level("10.10")
    def testProtocols10_10(self):
        self.assertResultHasType(
            TestAVAssetResourceLoaderHelper.resourceLoader_shouldWaitForRenewalOfRequestedResource_,  # noqa: B950
            objc._C_NSBOOL,
        )
        self.assertResultHasType(
            TestAVAssetResourceLoaderHelper.resourceLoader_shouldWaitForResponseToAuthenticationChallenge_,  # noqa: B950
            objc._C_NSBOOL,
        )

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetResourceLoadingRequest.isFinished
        )  # noqa: B950

        self.assertResultIsBOOL(
            AVFoundation.AVAssetResourceLoadingRequest.isCancelled
        )  # noqa: B950

        self.assertResultIsBOOL(
            AVFoundation.AVAssetResourceLoadingContentInformationRequest.isByteRangeAccessSupported  # noqa: B950
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetResourceLoadingContentInformationRequest.setByteRangeAccessSupported_,  # noqa: B950
            0,
        )

        self.assertArgIsOut(
            AVFoundation.AVAssetResourceLoadingRequest.streamingContentKeyRequestDataForApp_contentIdentifier_options_error_,  # noqa: B950
            3,
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetResourceLoadingDataRequest.requestsAllDataToEndOfResource  # noqa: B950
        )

        self.assertResultIsBOOL(
            AVFoundation.AVAssetResourceLoader.preloadsEligibleContentKeys
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetResourceLoader.setPreloadsEligibleContentKeys_, 0
        )

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetResourceLoadingRequestor.providesExpiredSessionReports  # noqa: B950
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsOut(
            AVFoundation.AVAssetResourceLoadingRequest.persistentContentKeyFromKeyVendorResponse_options_error_,  # noqa: B950
            2,
        )

    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetResourceLoadingContentInformationRequest.isEntireLengthAvailableOnDemand
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetResourceLoadingContentInformationRequest.setEntireLengthAvailableOnDemand_,
            0,
        )
