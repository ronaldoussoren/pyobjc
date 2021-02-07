from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders

MPSCopyAllocator = b"@@@@"  # XXX: "Returns retained"


class TestMPSImage_MPSImageKernel(TestCase):
    @min_os_level("10.13")
    def test_methods(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSUnaryImageKernel.encodeToCommandBuffer_inPlaceTexture_fallbackCopyAllocator_
        )
        self.assertArgIsBlock(
            MetalPerformanceShaders.MPSUnaryImageKernel.encodeToCommandBuffer_inPlaceTexture_fallbackCopyAllocator_,
            2,
            MPSCopyAllocator,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSBinaryImageKernel.encodeToCommandBuffer_primaryTexture_inPlaceSecondaryTexture_fallbackCopyAllocator_  # noqa: B950
        )
        self.assertArgIsBlock(
            MetalPerformanceShaders.MPSBinaryImageKernel.encodeToCommandBuffer_primaryTexture_inPlaceSecondaryTexture_fallbackCopyAllocator_,  # noqa: B950
            3,
            MPSCopyAllocator,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSBinaryImageKernel.encodeToCommandBuffer_inPlacePrimaryTexture_secondaryTexture_fallbackCopyAllocator_  # noqa: B950
        )
        self.assertArgIsBlock(
            MetalPerformanceShaders.MPSBinaryImageKernel.encodeToCommandBuffer_inPlacePrimaryTexture_secondaryTexture_fallbackCopyAllocator_,  # noqa: B950
            3,
            MPSCopyAllocator,
        )
