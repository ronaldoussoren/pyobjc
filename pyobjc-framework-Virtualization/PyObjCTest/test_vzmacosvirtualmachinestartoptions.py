from PyObjCTools.TestSupport import TestCase, min_os_level, arch_only

import Virtualization


class TestVZMacOSVirtualMachineStartOptions(TestCase):
    @min_os_level("13.0")
    @arch_only("arm64")
    def test_methods13_0(self):
        self.assertResultIsBOOL(
            Virtualization.VZMacOSVirtualMachineStartOptions.startUpFromMacOSRecovery
        )
        self.assertArgIsBOOL(
            Virtualization.VZMacOSVirtualMachineStartOptions.setStartUpFromMacOSRecovery_,
            0,
        )

    @min_os_level("27.0")
    @arch_only("arm64")
    def test_methods27_0(self):
        self.assertResultIsBOOL(
            Virtualization.VZMacOSVirtualMachineStartOptions.setGuestProvisioningOptions_error_
        )
        self.assertArgIsOut(
            Virtualization.VZMacOSVirtualMachineStartOptions.setGuestProvisioningOptions_error_,
            1,
        )
