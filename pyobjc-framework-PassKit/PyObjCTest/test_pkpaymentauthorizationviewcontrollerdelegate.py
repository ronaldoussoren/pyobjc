from PyObjCTools.TestSupport import TestCase

import PassKit  # noqa: F401
import objc


class TestPKAddPaymentPassRequestHelper(PassKit.NSObject):
    def paymentAuthorizationViewController_didAuthorizePayment_handler_(self, a, b, c):
        pass

    def paymentAuthorizationViewController_didRequestMerchantSessionUpdate_(self, a, b):
        pass

    def paymentAuthorizationViewController_didSelectShippingMethod_handler_(
        self, a, b, c
    ):
        pass

    def paymentAuthorizationViewController_didSelectShippingContact_handler_(
        self, a, b, c
    ):
        pass

    def paymentAuthorizationViewController_didSelectPaymentMethod_handler_(
        self, a, b, c
    ):
        pass

    def paymentAuthorizationViewController_didAuthorizePayment_completion_(
        self, a, b, c
    ):
        pass

    def paymentAuthorizationViewController_didSelectShippingMethod_completion_(
        self, a, b, c
    ):
        pass

    def paymentAuthorizationViewController_didSelectShippingAddress_completion_(
        self, a, b, c
    ):
        pass

    def paymentAuthorizationViewController_didSelectShippingContact_completion_(
        self, a, b, c
    ):
        pass

    def paymentAuthorizationViewController_didSelectPaymentMethod_completion_(
        self, a, b, c
    ):
        pass

    def paymentAuthorizationViewController_didChangeCouponCode_handler_(self, a, b, c):
        pass


class TestPKAddPaymentPassRequest(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("PKPaymentAuthorizationViewControllerDelegate")

    def test_methods(self):
        self.assertArgIsBlock(
            TestPKAddPaymentPassRequestHelper.paymentAuthorizationViewController_didAuthorizePayment_handler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPKAddPaymentPassRequestHelper.paymentAuthorizationViewController_didRequestMerchantSessionUpdate_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPKAddPaymentPassRequestHelper.paymentAuthorizationViewController_didSelectShippingMethod_handler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPKAddPaymentPassRequestHelper.paymentAuthorizationViewController_didSelectShippingContact_handler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPKAddPaymentPassRequestHelper.paymentAuthorizationViewController_didSelectPaymentMethod_handler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPKAddPaymentPassRequestHelper.paymentAuthorizationViewController_didAuthorizePayment_completion_,
            2,
            b"v" + objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            TestPKAddPaymentPassRequestHelper.paymentAuthorizationViewController_didSelectShippingMethod_completion_,
            2,
            b"v" + objc._C_NSInteger + b"@",
        )
        self.assertArgIsBlock(
            TestPKAddPaymentPassRequestHelper.paymentAuthorizationViewController_didSelectShippingContact_completion_,
            2,
            b"v" + objc._C_NSInteger + b"@@",
        )
        self.assertArgIsBlock(
            TestPKAddPaymentPassRequestHelper.paymentAuthorizationViewController_didSelectPaymentMethod_completion_,
            2,
            b"v@",
        )

        self.assertArgIsBlock(
            TestPKAddPaymentPassRequestHelper.paymentAuthorizationViewController_didChangeCouponCode_handler_,
            2,
            b"v@",
        )
