from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraphResizeOps(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphResizeMode)
        self.assertIsEnumType(
            MetalPerformanceShadersGraph.MPSGraphResizeNearestRoundingMode
        )

    def test_constants(self):
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphResizeNearest, 0)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphResizeBilinear, 1)

        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphResizeNearestRoundingModeRoundPreferCeil,
            0,
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphResizeNearestRoundingModeRoundPreferFloor,
            1,
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphResizeNearestRoundingModeCeil, 2
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphResizeNearestRoundingModeFloor, 3
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphResizeNearestRoundingModeRoundToEven, 4
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphResizeNearestRoundingModeRoundToOdd, 5
        )

    def test_methods(self):
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeTensor_size_mode_centerResult_alignCorners_layout_name_,
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeTensor_size_mode_centerResult_alignCorners_layout_name_,
            4,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeWithGradientTensor_input_mode_centerResult_alignCorners_layout_name_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeWithGradientTensor_input_mode_centerResult_alignCorners_layout_name_,  # noqa: B950
            4,
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeTensor_sizeTensor_mode_centerResult_alignCorners_layout_name_,
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeTensor_sizeTensor_mode_centerResult_alignCorners_layout_name_,
            4,
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeNearestWithTensor_sizeTensor_nearestRoundingMode_centerResult_alignCorners_layout_name_,
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeNearestWithTensor_sizeTensor_nearestRoundingMode_centerResult_alignCorners_layout_name_,
            4,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeBilinearWithTensor_sizeTensor_centerResult_alignCorners_layout_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeBilinearWithTensor_sizeTensor_centerResult_alignCorners_layout_name_,
            3,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeNearestWithGradientTensor_input_nearestRoundingMode_centerResult_alignCorners_layout_name_,
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeNearestWithGradientTensor_input_nearestRoundingMode_centerResult_alignCorners_layout_name_,
            4,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeBilinearWithGradientTensor_input_centerResult_alignCorners_layout_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeBilinearWithGradientTensor_input_centerResult_alignCorners_layout_name_,
            3,
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeTensor_sizeTensor_mode_centerResult_alignCorners_name_,
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeTensor_sizeTensor_mode_centerResult_alignCorners_name_,
            4,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeNearestWithTensor_sizeTensor_nearestRoundingMode_centerResult_alignCorners_name_,
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeNearestWithTensor_sizeTensor_nearestRoundingMode_centerResult_alignCorners_name_,
            4,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeBilinearWithTensor_sizeTensor_centerResult_alignCorners_name_,
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraph.resizeBilinearWithTensor_sizeTensor_centerResult_alignCorners_name_,
            3,
        )
