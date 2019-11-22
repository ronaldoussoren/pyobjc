from PyObjCTools.TestSupport import *

import SoundAnalysis


class TestSNRequest(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("SNRequest")
