from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShadersGraph


class TestMPSGraphResizeOps(TestCase):
    def test_constants(self):
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphResizeNearest, 0)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphResizeBilinear, 1)

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
