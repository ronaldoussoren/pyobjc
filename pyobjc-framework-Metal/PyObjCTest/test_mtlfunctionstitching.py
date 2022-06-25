import Metal  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestTMLFunctionStitching(TestCase):
    @min_sdk_level("12.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLFunctionStitchingAttribute")
        self.assertProtocolExists("MTLFunctionStitchingNode")
