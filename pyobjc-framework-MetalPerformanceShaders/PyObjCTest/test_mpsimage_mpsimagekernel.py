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

        self.assertResultHasType(
            MetalPerformanceShaders.MPSBinaryImageKernel.clipRect,
            MetalPerformanceShaders.MTLRegion.__typestr__,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSBinaryImageKernel.setClipRect_,
            0,
            MetalPerformanceShaders.MTLRegion.__typestr__,
        )
        self.assertResultHasType(
            MetalPerformanceShaders.MPSBinaryImageKernel.primaryOffset,
            MetalPerformanceShaders.MPSOffset.__typestr__,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSBinaryImageKernel.setPrimaryOffset_,
            0,
            MetalPerformanceShaders.MPSOffset.__typestr__,
        )
        self.assertResultHasType(
            MetalPerformanceShaders.MPSBinaryImageKernel.secondaryOffset,
            MetalPerformanceShaders.MPSOffset.__typestr__,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSBinaryImageKernel.setSecondaryOffset_,
            0,
            MetalPerformanceShaders.MPSOffset.__typestr__,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSBinaryImageKernel.primarySourceRegionForDestinationSize_,
            0,
            MetalPerformanceShaders.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            MetalPerformanceShaders.MPSBinaryImageKernel.secondarySourceRegionForDestinationSize_,
            0,
            MetalPerformanceShaders.MTLSize.__typestr__,
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
