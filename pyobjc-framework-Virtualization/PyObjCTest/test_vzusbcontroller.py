from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import Virtualization


class TestVZUSBController(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertArgIsBlock(
            Virtualization.VZUSBController.attachDevice_completionHandler_, 1, b"v@"
        )
        self.assertArgIsBlock(
            Virtualization.VZUSBController.detachDevice_completionHandler_, 1, b"v@"
        )

    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists("VZUSBControllerDelegate", Virtualization)
