from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZDiskBlockDeviceStorageDeviceAttachment(TestCase):
    @min_os_level("14.0")
    def test_methods(self):
        self.assertArgIsBOOL(
            Virtualization.VZDiskBlockDeviceStorageDeviceAttachment.initWithFileHandle_readOnly_synchronizationMode_error_,
            1,
        )
        self.assertArgIsOut(
            Virtualization.VZDiskBlockDeviceStorageDeviceAttachment.initWithFileHandle_readOnly_synchronizationMode_error_,
            3,
        )
        self.assertResultIsBOOL(
            Virtualization.VZDiskBlockDeviceStorageDeviceAttachment.isReadOnly
        )
