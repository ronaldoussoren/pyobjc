import Metal  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestTMLFunctionStitching(TestCase):
    @min_sdk_level("12.0")
    def test_protocols(self):
        objc.protocolNamed("MTLFunctionStitchingAttribute")
        objc.protocolNamed("MTLFunctionStitchingNode")
