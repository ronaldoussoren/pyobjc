import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTLResourceStatePass(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLCounterDontSample, 0xffffffffffffffff)
        self.assertEqual(Metal.MTLMaxResourceStatePassSampleBuffers, 4)
