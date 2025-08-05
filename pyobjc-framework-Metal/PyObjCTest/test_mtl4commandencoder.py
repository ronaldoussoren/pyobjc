import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTL4CommandEncoderHelper(Metal.NSObject):
    def barrierAfterQueueStages_beforeStages_visibilityOptions_(self, a, b, c):
        pass

    def barrierAfterStages_beforeQueueStages_visibilityOptions_(self, a, b, c):
        pass

    def barrierAfterEncoderStages_beforeEncoderStages_visibilityOptions_(self, a, b, c):
        pass

    def updateFence_afterEncoderStages_(self, a, b):
        pass

    def waitForFence_beforeEncoderStages_(self, a, b):
        pass

    def updateTextureMappings_heap_options_count_(self, a, b, c, d):
        pass


class TestMTL4CommandEncoder(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Metal.MTL4VisibilityOptions)
        self.assertEqual(Metal.MTL4VisibilityOptionNone, 0)
        self.assertEqual(Metal.MTL4VisibilityOptionDevice, 1 << 0)
        self.assertEqual(Metal.MTL4VisibilityOptionResourceAlias, 1 << 1)

    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4CommandEncoder")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestMTL4CommandEncoderHelper.barrierAfterQueueStages_beforeStages_visibilityOptions_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4CommandEncoderHelper.barrierAfterQueueStages_beforeStages_visibilityOptions_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4CommandEncoderHelper.barrierAfterQueueStages_beforeStages_visibilityOptions_,
            2,
            b"q",
        )

        self.assertArgHasType(
            TestMTL4CommandEncoderHelper.barrierAfterStages_beforeQueueStages_visibilityOptions_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4CommandEncoderHelper.barrierAfterStages_beforeQueueStages_visibilityOptions_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4CommandEncoderHelper.barrierAfterStages_beforeQueueStages_visibilityOptions_,
            2,
            b"q",
        )

        self.assertArgHasType(
            TestMTL4CommandEncoderHelper.barrierAfterEncoderStages_beforeEncoderStages_visibilityOptions_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4CommandEncoderHelper.barrierAfterEncoderStages_beforeEncoderStages_visibilityOptions_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4CommandEncoderHelper.barrierAfterEncoderStages_beforeEncoderStages_visibilityOptions_,
            2,
            b"q",
        )

        self.assertArgHasType(
            TestMTL4CommandEncoderHelper.updateFence_afterEncoderStages_, 1, b"Q"
        )
        self.assertArgHasType(
            TestMTL4CommandEncoderHelper.waitForFence_beforeEncoderStages_, 1, b"Q"
        )
