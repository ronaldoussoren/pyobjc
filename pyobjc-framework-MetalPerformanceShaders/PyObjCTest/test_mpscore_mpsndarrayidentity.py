from PyObjCTools.TestSupport import TestCase, min_os_level
import MetalPerformanceShaders


class TestMPSCore_MPSNDArrayIdentity(TestCase):
    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSNDArrayIdentity.reshapeWithCommandBuffer_sourceArray_dimensionCount_dimensionSizes_destinationArray_,
            3,
        )
        self.assertArgSizeInArg(
            MetalPerformanceShaders.MPSNDArrayIdentity.reshapeWithCommandBuffer_sourceArray_dimensionCount_dimensionSizes_destinationArray_,
            2,
        )

        self.assertArgIsIn(
            MetalPerformanceShaders.MPSNDArrayIdentity.reshapeWithCommandEncoder_sourceArray_dimensionCount_dimensionSizes_destinationArray_,
            3,
        )
        self.assertArgSizeInArg(
            MetalPerformanceShaders.MPSNDArrayIdentity.reshapeWithCommandEncoder_sourceArray_dimensionCount_dimensionSizes_destinationArray_,
            2,
        )
