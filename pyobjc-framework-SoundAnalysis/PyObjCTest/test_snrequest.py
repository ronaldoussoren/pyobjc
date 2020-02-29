import SoundAnalysis
from PyObjCTools.TestSupport import *


class TestSNRequest(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("SNRequest")
