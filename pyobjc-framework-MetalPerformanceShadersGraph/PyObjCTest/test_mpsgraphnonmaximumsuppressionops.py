from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraphNonMaximumSuppressionOps(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            MetalPerformanceShadersGraph.MPSGraphNonMaximumSuppressionCoordinateMode
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphNonMaximumSuppressionCoordinateModeCornersHeightFirst,
            0,
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphNonMaximumSuppressionCoordinateModeCornersWidthFirst,
            1,
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphNonMaximumSuppressionCoordinateModeCentersHeightFirst,
            2,
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphNonMaximumSuppressionCoordinateModeCentersWidthFirst,
            3,
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.nonMaximumSuppressionWithBoxesTensor_scoresTensor_IOUThreshold_scoreThreshold_perClassSuppression_coordinateMode_name_,
            4,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.nonMaximumSuppressionWithBoxesTensor_scoresTensor_classIndicesTensor_IOUThreshold_scoreThreshold_perClassSuppression_coordinateMode_name_,
            5,
        )
