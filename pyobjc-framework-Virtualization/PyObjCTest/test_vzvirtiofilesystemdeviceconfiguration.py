from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZVirtioFileSystemDeviceConfiguration(TestCase):
    @min_os_level("12.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZVirtioFileSystemDeviceConfiguration.validateTag_error_
        )
        self.assertArgIsOut(
            Virtualization.VZVirtioFileSystemDeviceConfiguration.validateTag_error_, 1
        )
