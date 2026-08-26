from PyObjCTools.TestSupport import TestCase, min_os_level, arch_only

import Virtualization


class TestVZMacGuestProvisioningOptions(TestCase):
    @min_os_level("27.0")
    @arch_only("arm64")
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZMacGuestProvisioningOptions.logsInAutomatically
        )
        self.assertArgIsBOOL(
            Virtualization.VZMacGuestProvisioningOptions.setLogsInAutomatically_, 0
        )

        self.assertResultIsBOOL(
            Virtualization.VZMacGuestProvisioningOptions.enablesRemoteLogin
        )
        self.assertArgIsBOOL(
            Virtualization.VZMacGuestProvisioningOptions.setEnablesRemoteLogin_, 0
        )
