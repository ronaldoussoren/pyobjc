import Metal  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLFence(TestCase):
    @min_sdk_level("10.13")
    def test_protocols(self):
        self.assertProtocolExists("MTLFence")
