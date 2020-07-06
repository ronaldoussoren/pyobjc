from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKPaymentAuthorizationViewController(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            PassKit.PKPaymentAuthorizationViewController.canMakePayments
        )
        self.assertResultIsBOOL(
            PassKit.PKPaymentAuthorizationViewController.canMakePaymentsUsingNetworks_
        )
        self.assertResultIsBOOL(
            PassKit.PKPaymentAuthorizationViewController.canMakePaymentsUsingNetworks_capabilities_
        )
