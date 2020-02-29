import Metal
from PyObjCTools.TestSupport import *


class TestMTLCaptureScope(TestCase):
    @min_sdk_level("10.13")
    def test_protocols(self):
        objc.protocolNamed("MTLCaptureScope")
