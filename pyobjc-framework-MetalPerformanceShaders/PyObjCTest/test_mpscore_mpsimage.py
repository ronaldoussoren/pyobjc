from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import MetalPerformanceShaders


class TestMPSCore_MPSImageHelper(MetalPerformanceShaders.NSObject):
    def imageBatchForCommandBuffer_imageDescriptor_kernel_count_(self, a, b, c, d):
        return 1


class TestMPSCore_MPSImage(TestCase):
    @min_os_level("10.13.4")
    def test_function10_13_4(self):
        MetalPerformanceShaders.MPSImageBatchIncrementReadCount
        MetalPerformanceShaders.MPSImageBatchSynchronize

    @min_os_level("10.14")
    def test_function10_14(self):
        MetalPerformanceShaders.MPSImageBatchResourceSize

    @min_os_level("10.15")
    def test_function10_15(self):
        self.assertArgIsBlock(
            MetalPerformanceShaders.MPSImageBatchIterate,
            1,
            objc._C_NSInteger + objc._C_ID + objc._C_NSUInteger,
        )

    def test_protocols(self):
        objc.protocolNamed("MPSImageAllocator")

    @min_os_level("10.13")
    def test_methods(self):
        self.assertArgHasType(
            TestMPSCore_MPSImageHelper.imageBatchForCommandBuffer_imageDescriptor_kernel_count_,
            3,
            objc._C_NSUInteger,
        )

        self.assertArgIsOut(
            MetalPerformanceShaders.MPSImage.readBytes_dataLayout_bytesPerRow_region_featureChannelInfo_imageIndex_,
            0,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSImage.readBytes_dataLayout_bytesPerRow_region_featureChannelInfo_imageIndex_,
            0,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImage.writeBytes_dataLayout_bytesPerRow_region_featureChannelInfo_imageIndex_,
            0,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSImage.writeBytes_dataLayout_bytesPerRow_region_featureChannelInfo_imageIndex_,
            0,
        )

        self.assertArgIsOut(
            MetalPerformanceShaders.MPSImage.readBytes_dataLayout_bytesPerRow_bytesPerImage_region_featureChannelInfo_imageIndex_,
            0,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSImage.readBytes_dataLayout_bytesPerRow_bytesPerImage_region_featureChannelInfo_imageIndex_,
            0,
        )

        self.assertArgIsOut(
            MetalPerformanceShaders.MPSImage.readBytes_dataLayout_imageIndex_, 0
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSImage.readBytes_dataLayout_imageIndex_, 0
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImage.writeBytes_dataLayout_imageIndex_, 0
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSImage.writeBytes_dataLayout_imageIndex_, 0
        )

    @min_os_level("10.13.4")
    def test_methods10_13_4(self):
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImage.writeBytes_dataLayout_bytesPerRow_bytesPerImage_region_featureChannelInfo_imageIndex_,
            0,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSImage.writeBytes_dataLayout_bytesPerRow_bytesPerImage_region_featureChannelInfo_imageIndex_,
            0,
        )

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImage.writeBytes_dataLayout_bytesPerColumn_bytesPerRow_bytesPerImage_region_featureChannelInfo_imageIndex_,  # noqa : B950
            0,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSImage.writeBytes_dataLayout_bytesPerColumn_bytesPerRow_bytesPerImage_region_featureChannelInfo_imageIndex_,  # noqa : B950
            0,
        )
