from PyObjCTools.TestSupport import TestCase, min_os_level

import PassKit


class TestPKConstants(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(PassKit.PKContactField, str)
        self.assertIsTypedEnum(PassKit.PKEncryptionScheme, str)

    def test_enum_types(self):
        self.assertIsEnumType(PassKit.PKPaymentAuthorizationStatus)
        self.assertIsEnumType(PassKit.PKPaymentButtonStyle)
        self.assertIsEnumType(PassKit.PKPaymentButtonType)
        self.assertIsEnumType(PassKit.PKRadioTechnology)

    def test_constants(self):
        self.assertIsInstance(PassKit.PKEncryptionSchemeECC_V2, str)
        self.assertIsInstance(PassKit.PKEncryptionSchemeRSA_V2, str)

        self.assertIsInstance(PassKit.PKPaymentNetworkAmex, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkCarteBancaire, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkCarteBancaires, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkCartesBancaires, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkChinaUnionPay, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkDiscover, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkEftpos, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkElectron, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkElo, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkIDCredit, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkInterac, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkJCB, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkMada, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkMaestro, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkMasterCard, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkPrivateLabel, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkQuicPay, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkSuica, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkVisa, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkVPay, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkBarcode, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkGirocard, str)

        self.assertIsInstance(PassKit.PKContactFieldPostalAddress, str)
        self.assertIsInstance(PassKit.PKContactFieldEmailAddress, str)
        self.assertIsInstance(PassKit.PKContactFieldPhoneNumber, str)
        self.assertIsInstance(PassKit.PKContactFieldName, str)
        self.assertIsInstance(PassKit.PKContactFieldPhoneticName, str)

        self.assertEqual(PassKit.PKPaymentAuthorizationStatusSuccess, 0)
        self.assertEqual(PassKit.PKPaymentAuthorizationStatusFailure, 1)

        self.assertEqual(
            PassKit.PKPaymentAuthorizationStatusInvalidBillingPostalAddress, 2
        )
        self.assertEqual(
            PassKit.PKPaymentAuthorizationStatusInvalidShippingPostalAddress, 3
        )
        self.assertEqual(PassKit.PKPaymentAuthorizationStatusInvalidShippingContact, 4)

        self.assertEqual(PassKit.PKPaymentAuthorizationStatusPINRequired, 5)
        self.assertEqual(PassKit.PKPaymentAuthorizationStatusPINIncorrect, 6)
        self.assertEqual(PassKit.PKPaymentAuthorizationStatusPINLockout, 7)

        self.assertEqual(PassKit.PKPaymentButtonStyleWhite, 0)
        self.assertEqual(PassKit.PKPaymentButtonStyleWhiteOutline, 1)
        self.assertEqual(PassKit.PKPaymentButtonStyleBlack, 2)
        self.assertEqual(PassKit.PKPaymentButtonStyleAutomatic, 3)

        self.assertEqual(PassKit.PKPaymentButtonTypePlain, 0)
        self.assertEqual(PassKit.PKPaymentButtonTypeBuy, 1)
        self.assertEqual(PassKit.PKPaymentButtonTypeSetUp, 2)
        self.assertEqual(PassKit.PKPaymentButtonTypeInStore, 3)
        self.assertEqual(PassKit.PKPaymentButtonTypeDonate, 4)
        self.assertEqual(PassKit.PKPaymentButtonTypeCheckout, 5)
        self.assertEqual(PassKit.PKPaymentButtonTypeBook, 6)
        self.assertEqual(PassKit.PKPaymentButtonTypeSubscribe, 7)
        self.assertEqual(PassKit.PKPaymentButtonTypeReload, 8)
        self.assertEqual(PassKit.PKPaymentButtonTypeAddMoney, 9)
        self.assertEqual(PassKit.PKPaymentButtonTypeTopUp, 10)
        self.assertEqual(PassKit.PKPaymentButtonTypeOrder, 11)
        self.assertEqual(PassKit.PKPaymentButtonTypeRent, 12)
        self.assertEqual(PassKit.PKPaymentButtonTypeSupport, 13)
        self.assertEqual(PassKit.PKPaymentButtonTypeContribute, 14)
        self.assertEqual(PassKit.PKPaymentButtonTypeTip, 15)
        self.assertEqual(PassKit.PKPaymentButtonTypeContinue, 16)

    @min_os_level("11.5")
    def test_constants11_5(self):
        self.assertIsInstance(PassKit.PKPaymentNetworkMir, str)

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(PassKit.PKPaymentNetworkWaon, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkNanaco, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkBancomat, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkBancontact, str)

    @min_os_level("13.3")
    def test_constants13_3(self):
        self.assertIsInstance(PassKit.PKPaymentNetworkPostFinance, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(PassKit.PKPaymentNetworkPagoBancomat, str)

    @min_os_level("12.2")
    def test_constants12_1(self):
        # SDK Says available in 10.1, but not available there
        self.assertIsInstance(PassKit.PKPaymentNetworkDankort, str)

    @min_os_level("14.4")
    def test_constants14_4(self):
        self.assertIsInstance(PassKit.PKPaymentNetworkMeeza, str)

    @min_os_level("14.5")
    def test_constants14_5(self):
        self.assertIsInstance(PassKit.PKPaymentNetworkNAPAS, str)
        self.assertIsInstance(PassKit.PKPaymentNetworkBankAxept, str)
