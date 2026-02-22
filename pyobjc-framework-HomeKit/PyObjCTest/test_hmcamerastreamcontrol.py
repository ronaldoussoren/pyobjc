from PyObjCTools.TestSupport import TestCase

import HomeKit  # noqa: F401


class TestHMCameraStreamControl(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("HMCameraStreamControlDelegate")
