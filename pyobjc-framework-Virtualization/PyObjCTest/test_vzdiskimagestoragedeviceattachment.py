from PyObjCTools.TestSupport import TestCase

import Virtualization


class TestVZDiskImageStorageDeviceAttachment(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(
            Virtualization.VZDiskImageStorageDeviceAttachment.initWithURL_readOnly_error_,
            1,
        )
        self.assertArgIsOut(
            Virtualization.VZDiskImageStorageDeviceAttachment.initWithURL_readOnly_error_,
            2,
        )
        self.assertResultIsBOOL(
            Virtualization.VZDiskImageStorageDeviceAttachment.isReadOnly
        )
