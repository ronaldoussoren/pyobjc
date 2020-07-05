from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc
import GameController  # noqa: F401


class TestGCDevice(TestCase):
    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("GCDevice")
