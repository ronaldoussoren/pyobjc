import StoreKit
from PyObjCTools.TestSupport import TestCase


class TestStoreKitDefines(TestCase):
    def test_defines(self):
        self.assertIsInstance(StoreKit.StoreKitBundle, StoreKit.NSBundle)
        self.assertIsInstance(StoreKit.SKLocalizedString("hello"), str)
