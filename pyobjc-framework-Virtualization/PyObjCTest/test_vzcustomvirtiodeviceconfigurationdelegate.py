from PyObjCTools.TestSupport import TestCase, min_sdk_level

import Virtualization


class TestVZCustomVirtioDevice(TestCase):
    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists(
            "VZCustomVirtioDeviceConfigurationDelegate", Virtualization
        )
