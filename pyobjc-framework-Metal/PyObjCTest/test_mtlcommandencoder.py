import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLCommandEncoderHelper(Metal.NSObject):
    def barrierAfterQueueStages_beforeStages_(self, a, b):
        pass


class TestMTLCommandEncoder(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLBarrierScope)
        self.assertIsEnumType(Metal.MTLResourceUsage)

    def test_constants(self):
        self.assertEqual(Metal.MTLResourceUsageRead, 1 << 0)
        self.assertEqual(Metal.MTLResourceUsageWrite, 1 << 1)
        self.assertEqual(Metal.MTLResourceUsageSample, 1 << 2)

        self.assertEqual(Metal.MTLBarrierScopeBuffers, 1 << 0)
        self.assertEqual(Metal.MTLBarrierScopeTextures, 1 << 1)
        self.assertEqual(Metal.MTLBarrierScopeRenderTargets, 1 << 2)

    @min_sdk_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("MTLCommandEncoder")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestMTLCommandEncoderHelper.barrierAfterQueueStages_beforeStages_, 0, b"Q"
        )
        self.assertArgHasType(
            TestMTLCommandEncoderHelper.barrierAfterQueueStages_beforeStages_, 1, b"Q"
        )
