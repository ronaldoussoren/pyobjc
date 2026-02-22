from PyObjCTools.TestSupport import TestCase, expectedFailure

import HomeKit  # noqa: F401


class TestHMCameraStreamControl(TestCase):
    @expectedFailure
    def test_protocols(self):
        self.assertProtocolExists("HMCameraStreamControlDelegate")
