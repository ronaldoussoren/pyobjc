from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZEFIVariableStore(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Virtualization.VZEFIVariableStoreInitializationOptions)
        self.assertEqual(
            Virtualization.VZEFIVariableStoreInitializationOptionAllowOverwrite, 1 << 0
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsOut(
            Virtualization.VZEFIVariableStore.initCreatingVariableStoreAtURL_options_error_,
            2,
        )

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(
            Virtualization.VZEFIVariableStore.enableSecureBootUsingDefaultPlatformKeyWithError_
        )
        self.assertArgIsOut(
            Virtualization.VZEFIVariableStore.enableSecureBootUsingDefaultPlatformKeyWithError_,
            0,
        )

        self.assertResultIsBOOL(
            Virtualization.VZEFIVariableStore.enableSecureBootWithPlatformKey_error_
        )
        self.assertArgIsOut(
            Virtualization.VZEFIVariableStore.enableSecureBootWithPlatformKey_error_, 1
        )

        self.assertResultIsBOOL(
            Virtualization.VZEFIVariableStore.disableSecureBootWithError_
        )
        self.assertArgIsOut(
            Virtualization.VZEFIVariableStore.disableSecureBootWithError_, 0
        )

        self.assertResultIsBOOL(
            Virtualization.VZEFIVariableStore.resetSecureBootWithError_
        )
        self.assertArgIsOut(
            Virtualization.VZEFIVariableStore.resetSecureBootWithError_, 0
        )

        self.assertResultIsBOOL(
            Virtualization.VZEFIVariableStore.getSecureBootEnabled_error_
        )
        self.assertArgIsOut(
            Virtualization.VZEFIVariableStore.getSecureBootEnabled_error_, 0
        )
        self.assertArgIsOut(
            Virtualization.VZEFIVariableStore.getSecureBootEnabled_error_, 1
        )

        self.assertResultIsBOOL(
            Virtualization.VZEFIVariableStore.enrollDefaultSecureBootSignaturesWithError_
        )
        self.assertArgIsOut(
            Virtualization.VZEFIVariableStore.enrollDefaultSecureBootSignaturesWithError_,
            0,
        )

        self.assertResultIsBOOL(
            Virtualization.VZEFIVariableStore.enrollSecureBootSignatures_error_
        )
        self.assertArgIsOut(
            Virtualization.VZEFIVariableStore.enrollSecureBootSignatures_error_, 1
        )

        self.assertArgIsOut(
            Virtualization.VZEFIVariableStore.getEnrolledSecureBootSignaturesWithError_,
            0,
        )
