import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestMTLCommandEncoder(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLResourceUsageRead, 1 << 0)
        self.assertEqual(Metal.MTLResourceUsageWrite, 1 << 1)
        self.assertEqual(Metal.MTLResourceUsageSample, 1 << 2)

        self.assertEqual(Metal.MTLBarrierScopeBuffers, 1 << 0)
        self.assertEqual(Metal.MTLBarrierScopeTextures, 1 << 1)
        self.assertEqual(Metal.MTLBarrierScopeRenderTargets, 1 << 2)

    @min_sdk_level("10.11")
    def test_protocols(self):
        objc.protocolNamed("MTLCommandEncoder")
