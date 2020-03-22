import Metal  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestMTLFence(TestCase):
    @min_sdk_level("10.13")
    def test_protocols(self):
        objc.protocolNamed("MTLFence")
