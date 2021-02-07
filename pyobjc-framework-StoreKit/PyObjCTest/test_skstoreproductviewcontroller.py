import StoreKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestSKStoreProductViewController(TestCase):
    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(StoreKit.SKStoreProductParameterITunesItemIdentifier, str)
        self.assertIsInstance(StoreKit.SKStoreProductParameterProductIdentifier, str)
        self.assertIsInstance(StoreKit.SKStoreProductParameterAffiliateToken, str)
        self.assertIsInstance(StoreKit.SKStoreProductParameterCampaignToken, str)
        self.assertIsInstance(StoreKit.SKStoreProductParameterProviderToken, str)
        self.assertIsInstance(
            StoreKit.SKStoreProductParameterAdvertisingPartnerToken, str
        )

    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("SKStoreProductViewControllerDelegate")

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsBlock(
            StoreKit.SKStoreProductViewController.loadProductWithParameters_completionBlock_,
            1,
            b"vZ@",
        )
