import StoreKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSKProductStorePromotionController(TestCase):
    def test_constants(self):
        self.assertEqual(StoreKit.SKProductStorePromotionVisibilityDefault, 0)
        self.assertEqual(StoreKit.SKProductStorePromotionVisibilityShow, 1)
        self.assertEqual(StoreKit.SKProductStorePromotionVisibilityHide, 2)

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsBlock(
            StoreKit.SKProductStorePromotionController.fetchStorePromotionVisibilityForProduct_completionHandler_,
            1,
            b"v" + objc._C_NSInteger + b"@",
        )
        self.assertArgIsBlock(
            StoreKit.SKProductStorePromotionController.updateStorePromotionVisibility_forProduct_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            StoreKit.SKProductStorePromotionController.fetchStorePromotionOrderWithCompletionHandler_,
            0,
            b"v@@",
        )

        self.assertArgIsBlock(
            StoreKit.SKProductStorePromotionController.updateStorePromotionOrder_completionHandler_,
            1,
            b"v@",
        )
