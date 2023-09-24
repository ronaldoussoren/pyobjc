from PyObjCTools.TestSupport import TestCase, min_os_level, arch_only

import Virtualization


class TestVZVirtualMachineConfiguration(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZVirtualMachineConfiguration.validateWithError_
        )
        self.assertArgIsOut(
            Virtualization.VZVirtualMachineConfiguration.validateWithError_, 0
        )

    @arch_only("arm64")
    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            Virtualization.VZVirtualMachineConfiguration.validateSaveRestoreSupportWithError_
        )
        self.assertArgIsOut(
            Virtualization.VZVirtualMachineConfiguration.validateSaveRestoreSupportWithError_,
            0,
        )
