import StoreKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSKDownload(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(StoreKit.SKProductPeriodUnit)

    def test_constants(self):
        self.assertEqual(StoreKit.SKProductPeriodUnitDay, 0)
        self.assertEqual(StoreKit.SKProductPeriodUnitWeek, 1)
        self.assertEqual(StoreKit.SKProductPeriodUnitMonth, 2)
        self.assertEqual(StoreKit.SKProductPeriodUnitYear, 3)

    def test_methods(self):
        self.assertResultIsBOOL(StoreKit.SKProduct.downloadable)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(StoreKit.SKProduct.isDownloadable)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(StoreKit.SKProduct.isFamilyShareable)
