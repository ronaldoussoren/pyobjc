import StoreKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestSKStoreProductViewController(TestCase):
    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(StoreKit.SKStoreProductParameterITunesItemIdentifier, str)
        self.assertIsInstance(StoreKit.SKStoreProductParameterProductIdentifier, str)
        self.assertIsInstance(StoreKit.SKStoreProductParameterAffiliateToken, str)
        self.assertIsInstance(StoreKit.SKStoreProductParameterCampaignToken, str)
        self.assertIsInstance(StoreKit.SKStoreProductParameterProviderToken, str)
        self.assertIsInstance(
            StoreKit.SKStoreProductParameterAdvertisingPartnerToken, str
        )

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            StoreKit.SKStoreProductParameterCustomProductPageIdentifier, str
        )

    @min_sdk_level("11.0")
    def test_protocols11_0(self):
        self.assertProtocolExists("SKStoreProductViewControllerDelegate")

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsBlock(
            StoreKit.SKStoreProductViewController.loadProductWithParameters_completionBlock_,
            1,
            b"vZ@",
        )
