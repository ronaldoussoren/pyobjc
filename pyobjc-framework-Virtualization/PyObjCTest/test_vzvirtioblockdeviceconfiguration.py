from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZVirtioBlockDeviceConfiguration(TestCase):
    @min_os_level("12.3")
    def test_methods12_3(self):
        self.assertResultIsBOOL(
            Virtualization.VZVirtioBlockDeviceConfiguration.validateBlockDeviceIdentifier_error_,
        )
        self.assertArgIsOut(
            Virtualization.VZVirtioBlockDeviceConfiguration.validateBlockDeviceIdentifier_error_,
            1,
        )
