from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZCustomVirtioDeviceConfiguration(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZCustomVirtioDeviceConfiguration.supportsSaveRestore
        )
        self.assertArgIsBOOL(
            Virtualization.VZCustomVirtioDeviceConfiguration.setSupportsSaveRestore_, 0
        )
