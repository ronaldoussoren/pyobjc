from PyObjCTools.TestSupport import TestCase, min_os_level

import DeviceCheck


class TestDCDevice(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultIsBOOL(DeviceCheck.DCDevice.isSupported)

        self.assertArgIsBlock(
            DeviceCheck.DCDevice.generateTokenWithCompletionHandler_, 0, b"v@@"
        )
