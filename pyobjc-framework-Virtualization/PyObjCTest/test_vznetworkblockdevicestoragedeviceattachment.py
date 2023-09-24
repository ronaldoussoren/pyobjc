from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import Virtualization


class TestVZNetworkBlockDeviceStorageDeviceAttachment(TestCase):
    @min_os_level("14.0")
    def test_methods(self):
        self.assertArgIsBOOL(
            Virtualization.VZNetworkBlockDeviceStorageDeviceAttachment.initWithURL_timeout_forcedReadOnly_synchronizationMode_error_,
            2,
        )
        self.assertArgIsOut(
            Virtualization.VZNetworkBlockDeviceStorageDeviceAttachment.initWithURL_timeout_forcedReadOnly_synchronizationMode_error_,
            4,
        )

        self.assertArgIsOut(
            Virtualization.VZNetworkBlockDeviceStorageDeviceAttachment.initWithURL_error_,
            1,
        )

        self.assertResultIsBOOL(
            Virtualization.VZNetworkBlockDeviceStorageDeviceAttachment.validateURL_error_
        )
        self.assertArgIsOut(
            Virtualization.VZNetworkBlockDeviceStorageDeviceAttachment.validateURL_error_,
            1,
        )

        self.assertResultIsBOOL(
            Virtualization.VZNetworkBlockDeviceStorageDeviceAttachment.isForcedReadOnly
        )

    @min_sdk_level("14.0")
    def test_protocols(self):
        self.assertProtocolExists("VZNetworkBlockDeviceStorageDeviceAttachmentDelegate")
