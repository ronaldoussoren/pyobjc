from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraphSampleGridOps(TestCase):
    @min_os_level("13.3")
    def test_methods_13_3(self):
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.sampleGridWithSourceTensor_coordinateTensor_layout_normalizeCoordinates_relativeCoordinates_alignCorners_paddingMode_samplingMode_constantValue_name_,
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.sampleGridWithSourceTensor_coordinateTensor_layout_normalizeCoordinates_relativeCoordinates_alignCorners_paddingMode_samplingMode_constantValue_name_,
            4,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.sampleGridWithSourceTensor_coordinateTensor_layout_normalizeCoordinates_relativeCoordinates_alignCorners_paddingMode_samplingMode_constantValue_name_,
            5,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.sampleGridWithSourceTensor_coordinateTensor_layout_normalizeCoordinates_relativeCoordinates_alignCorners_paddingMode_nearestRoundingMode_constantValue_name_,
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.sampleGridWithSourceTensor_coordinateTensor_layout_normalizeCoordinates_relativeCoordinates_alignCorners_paddingMode_nearestRoundingMode_constantValue_name_,
            4,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.sampleGridWithSourceTensor_coordinateTensor_layout_normalizeCoordinates_relativeCoordinates_alignCorners_paddingMode_nearestRoundingMode_constantValue_name_,
            5,
        )
