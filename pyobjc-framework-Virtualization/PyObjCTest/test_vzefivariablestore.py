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
