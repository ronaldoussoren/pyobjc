from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZUSBPassthroughDevice(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertArgIsOut(
            Virtualization.VZUSBPassthroughDevice.initWithConfiguration_error_, 1
        )
