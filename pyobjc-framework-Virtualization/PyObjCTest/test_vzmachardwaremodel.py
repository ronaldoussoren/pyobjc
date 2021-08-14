from PyObjCTools.TestSupport import TestCase, arch_only, min_os_level

import Virtualization


class TestVZMacHardwareModel(TestCase):
    @min_os_level("12.0")
    @arch_only("arm64")
    def test_methods(self):
        self.assertResultIsBOOL(Virtualization.VZMacHardwareModel.isSupported)
