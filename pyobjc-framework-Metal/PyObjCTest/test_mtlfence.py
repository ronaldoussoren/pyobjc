from PyObjCTools.TestSupport import *

import Metal


class TestMTLFence(TestCase):
    @min_sdk_level("10.13")
    def test_protocols(self):
        objc.protocolNamed("MTLFence")
