import SoundAnalysis  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestSNRequest(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("SNRequest")
