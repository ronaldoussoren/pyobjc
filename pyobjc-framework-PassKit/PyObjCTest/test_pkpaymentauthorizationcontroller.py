from PyObjCTools.TestSupport import TestCase

import PassKit
import objc


class TestPKPaymentAuthorizationControllerHelper(PassKit.NSObject):
    def paymentAuthorizationController_didAuthorizePayment_handler_(self, a, b, c):
        pass

    def paymentAuthorizationController_didAuthorizePayment_completion_(self, a, b, c):
        pass

    def paymentAuthorizationController_didRequestMerchantSessionUpdate_(self, a, b):
        pass

    def paymentAuthorizationController_didSelectShippingMethod_handler_(self, a, b, c):
        pass

    def paymentAuthorizationController_didSelectShippingContact_handler_(self, a, b, c):
        pass

    def paymentAuthorizationController_didSelectPlaymentMethod_handler_(self, a, b, c):
        pass

    def paymentAuthorizationController_didSelectShippingMethod_completion_(
        self, a, b, c
    ):
        pass

    def paymentAuthorizationController_didSelectShippingContact_completion_(
        self, a, b, c
    ):
        pass

    def paymentAuthorizationController_didSelectPaymentMethod_completion_(
        self, a, b, c
    ):
        pass

    def paymentAuthorizationController_didChangeCouponCode_handler_(self, a, b, c):
        pass


class TestPKPaymentAuthorizationController(TestCase):
    def test_protocols(self):
        objc.protocolNamed("PKPaymentAuthorizationControllerDelegate")

    def test_methods(self):
        self.assertArgIsBlock(
            TestPKPaymentAuthorizationControllerHelper.paymentAuthorizationController_didAuthorizePayment_handler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPKPaymentAuthorizationControllerHelper.paymentAuthorizationController_didAuthorizePayment_completion_,
            2,
            b"vq",
        )
        self.assertArgIsBlock(
            TestPKPaymentAuthorizationControllerHelper.paymentAuthorizationController_didRequestMerchantSessionUpdate_,
            1,
            b"v@",
        )

        self.assertArgIsBlock(
            TestPKPaymentAuthorizationControllerHelper.paymentAuthorizationController_didSelectShippingMethod_handler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPKPaymentAuthorizationControllerHelper.paymentAuthorizationController_didSelectShippingContact_handler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPKPaymentAuthorizationControllerHelper.paymentAuthorizationController_didSelectShippingMethod_completion_,
            2,
            b"vq@",
        )
        self.assertArgIsBlock(
            TestPKPaymentAuthorizationControllerHelper.paymentAuthorizationController_didSelectShippingContact_completion_,
            2,
            b"vq@@",
        )
        self.assertArgIsBlock(
            TestPKPaymentAuthorizationControllerHelper.paymentAuthorizationController_didSelectPaymentMethod_completion_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPKPaymentAuthorizationControllerHelper.paymentAuthorizationController_didChangeCouponCode_handler_,
            2,
            b"v@",
        )

        self.assertResultIsBOOL(
            PassKit.PKPaymentAuthorizationController.canMakePayments
        )
        self.assertResultIsBOOL(
            PassKit.PKPaymentAuthorizationController.canMakePaymentsUsingNetworks_
        )
        self.assertResultIsBOOL(
            PassKit.PKPaymentAuthorizationController.canMakePaymentsUsingNetworks_capabilities_
        )

        self.assertArgIsBlock(
            PassKit.PKPaymentAuthorizationController.presentWithCompletion_,
            0,
            b"v" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            PassKit.PKPaymentAuthorizationController.dismissWithCompletion_, 0, b"v"
        )
