from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import MetalPerformanceShaders
from objc import simd


class TestMPSCore_MPSNDArray(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultHasType(
            MetalPerformanceShaders.MPSNDArrayDescriptor.dimensionOrder,
            simd.vector_uchar16.__typestr__,
        )

        self.assertIsNullTerminated(
            MetalPerformanceShaders.MPSNDArrayDescriptor.descriptorWithDataType_dimensionSizes_
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSNDArrayDescriptor.reshapeWithDimensionCount_dimensionSizes_,
            1,
        )
        self.assertArgSizeInArg(
            MetalPerformanceShaders.MPSNDArrayDescriptor.reshapeWithDimensionCount_dimensionSizes_,
            1,
            0,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSNDArray.exportDataWithCommandBuffer_toBuffer_destinationDataType_offset_rowStrides_,
            4,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSNDArray.exportDataWithCommandBuffer_toBuffer_destinationDataType_offset_rowStrides_,
            4,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSNDArray.importDataWithCommandBuffer_fromBuffer_sourceDataType_offset_rowStrides_,
            4,
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSNDArray.importDataWithCommandBuffer_fromBuffer_sourceDataType_offset_rowStrides_,
            4,
        )

        self.assertArgIsOut(MetalPerformanceShaders.MPSNDArray.readBytes_strideBytes_, 0)
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSNDArray.readBytes_strideBytes_, 0
        )
        self.assertArgIsIn(MetalPerformanceShaders.MPSNDArray.readBytes_strideBytes_, 1)
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSNDArray.readBytes_strideBytes_, 1
        )

        self.assertArgIsIn(MetalPerformanceShaders.MPSNDArray.writeBytes_strideBytes_, 0)
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSNDArray.writeBytes_strideBytes_, 0
        )
        self.assertArgIsIn(MetalPerformanceShaders.MPSNDArray.writeBytes_strideBytes_, 1)
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSNDArray.writeBytes_strideBytes_, 1
        )

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNDArrayDescriptor.preferPackedRows
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNDArrayDescriptor.setPreferPackedRows_, 0
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSNDArrayDescriptor.permuteWithDimensionOrder_, 0
        )
        self.assertArgIsVariableSize(
            MetalPerformanceShaders.MPSNDArrayDescriptor.permuteWithDimensionOrder_, 0
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSNDArray.arrayViewWithDimensionCount_dimensionSizes_strides_,
            1,
        )
        self.assertArgSizeInArg(
            MetalPerformanceShaders.MPSNDArray.arrayViewWithDimensionCount_dimensionSizes_strides_,
            1,
            0,
        )
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSNDArray.arrayViewWithDimensionCount_dimensionSizes_strides_,
            2,
        )
        self.assertArgSizeInArg(
            MetalPerformanceShaders.MPSNDArray.arrayViewWithDimensionCount_dimensionSizes_strides_,
            2,
            0,
        )

    @min_sdk_level("10.15")
    def test_protocols(self):
        self.assertProtocolExists("MPSNDArrayAllocator")
