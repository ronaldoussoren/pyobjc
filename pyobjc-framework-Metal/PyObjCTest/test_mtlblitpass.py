import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTLBlitPass(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLCounterDontSample, 0xFFFFFFFFFFFFFFFF)
        self.assertEqual(Metal.MTLMaxBlitPassSampleBuffers, 4)
