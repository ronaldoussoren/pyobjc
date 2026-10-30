from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZCustomVirtioDevice(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertArgIsBlock(
            Virtualization.VZCustomVirtioDevice.updateDeviceSpecificConfiguration_completionHandler_,
            1,
            b"v@",
        )
