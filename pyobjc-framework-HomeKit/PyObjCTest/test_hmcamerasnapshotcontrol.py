from PyObjCTools.TestSupport import TestCase

import HomeKit  # noqa: F401


class TestHMCameraSnapshotControl(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("HMCameraSnapshotControlDelegate")
