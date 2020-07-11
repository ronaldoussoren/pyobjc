import StoreKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSKCloudServiceController(TestCase):
    def test_constants(self):
        self.assertEqual(StoreKit.SKCloudServiceAuthorizationStatusNotDetermined, 0)
        self.assertEqual(StoreKit.SKCloudServiceAuthorizationStatusDenied, 1)
        self.assertEqual(StoreKit.SKCloudServiceAuthorizationStatusRestricted, 2)
        self.assertEqual(StoreKit.SKCloudServiceAuthorizationStatusAuthorized, 3)

        self.assertEqual(StoreKit.SKCloudServiceCapabilityNone, 0)
        self.assertEqual(StoreKit.SKCloudServiceCapabilityMusicCatalogPlayback, 1 << 0)
        self.assertEqual(
            StoreKit.SKCloudServiceCapabilityMusicCatalogSubscriptionEligible, 1 << 1
        )
        self.assertEqual(
            StoreKit.SKCloudServiceCapabilityAddToCloudMusicLibrary, 1 << 8
        )

    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(
            StoreKit.SKCloudServiceCapabilitiesDidChangeNotification, str
        )
        self.assertIsInstance(
            StoreKit.SKStorefrontCountryCodeDidChangeNotification, str
        )
        self.assertIsInstance(StoreKit.SKStorefrontIdentifierDidChangeNotification, str)

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsBlock(
            StoreKit.SKCloudServiceController.requestAuthorization_,
            0,
            b"v" + objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            StoreKit.SKCloudServiceController.requestCapabilitiesWithCompletionHandler_,
            0,
            b"v" + objc._C_NSUInteger + b"@",
        )
        self.assertArgIsBlock(
            StoreKit.SKCloudServiceController.requestStorefrontCountryCodeWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            StoreKit.SKCloudServiceController.requestStorefrontIdentifierWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            StoreKit.SKCloudServiceController.requestUserTokenForDeveloperToken_completionHandler_,
            1,
            b"v@@",
        )
