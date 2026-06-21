from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZGuestProvisioningOptions(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZGuestProvisioningOptions.validateWithError_
        )
        self.assertArgIsOut(
            Virtualization.VZGuestProvisioningOptions.validateWithError_, 0
        )
