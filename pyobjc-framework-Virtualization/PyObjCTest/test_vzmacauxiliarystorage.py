from PyObjCTools.TestSupport import TestCase, min_os_level, arch_only

import Virtualization


class TestVZMacAuxiliaryStorage(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Virtualization.VZMacAuxiliaryStorageInitializationOptions)

    def test_constants(self):
        self.assertEqual(
            Virtualization.VZMacAuxiliaryStorageInitializationOptionAllowOverwrite,
            1 << 0,
        )

    @min_os_level("12.0")
    @arch_only("arm64")
    def testMethods12_0(self):
        self.assertArgIsOut(
            Virtualization.VZMacAuxiliaryStorage.initCreatingStorageAtURL_hardwareModel_options_error_,
            3,
        )
