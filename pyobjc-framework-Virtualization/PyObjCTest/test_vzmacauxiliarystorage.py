from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZMacAuxiliaryStorage(TestCase):
    def test_constants(self):
        self.assertEqual(
            Virtualization.VZMacAuxiliaryStorageInitializationOptionAllowOverwrite,
            1 << 0,
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertArgIsOut(
            Virtualization.VZMacAuxiliaryStorage.initCreatingStorageAtURL_hardwareModel_options_error_,
            3,
        )
