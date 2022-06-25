from PyObjCTools.TestSupport import TestCase, min_sdk_level
import GameController  # noqa: F401


class TestGCDevice(TestCase):
    @min_sdk_level("11.0")
    def test_protocols11_0(self):
        self.assertProtocolExists("GCDevice")
