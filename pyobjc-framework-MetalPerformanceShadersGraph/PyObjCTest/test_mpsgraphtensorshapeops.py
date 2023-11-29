from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraphTensorShapeOps(TestCase):
    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.depthToSpace2DTensor_widthAxisTensor_heightAxisTensor_depthAxisTensor_blockSize_usePixelShuffleOrder_name_,  # noqa: B950
            5,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.depthToSpace2DTensor_widthAxis_heightAxis_depthAxis_blockSize_usePixelShuffleOrder_name_,  # noqa: B950
            5,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.spaceToDepth2DTensor_widthAxis_heightAxis_depthAxis_blockSize_usePixelShuffleOrder_name_,  # noqa: B950
            5,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.depthToSpace2DTensor_widthAxis_heightAxis_depthAxis_blockSize_usePixelShuffleOrder_name_,  # noqa: B950
            5,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.depthToSpace2DTensor_widthAxis_heightAxis_depthAxis_blockSize_usePixelShuffleOrder_name_,  # noqa: B950
            5,
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.spaceToBatchTensor_spatialAxes_batchAxis_blockDimensions_usePixelShuffleOrder_name_,  # noqa: B950
            4,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.spaceToBatchTensor_spatialAxes_batchAxis_blockDimensions_usePixelShuffleOrder_name_,  # noqa: B950
            4,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.spaceToBatchTensor_spatialAxes_batchAxis_blockDimensions_usePixelShuffleOrder_name_,  # noqa: B950
            4,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.batchToSpaceTensor_spatialAxesTensor_batchAxisTensor_blockDimensionsTensor_usePixelShuffleOrder_name_,  # noqa: B950
            4,
        )
