from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraphPoolingOps(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(
            MetalPerformanceShadersGraph.MPSGraphPoolingReturnIndicesMode
        )

    def test_constants(self):
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphPoolingReturnIndicesNone, 0
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphPoolingReturnIndicesGlobalFlatten1D, 1
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphPoolingReturnIndicesGlobalFlatten2D, 2
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphPoolingReturnIndicesGlobalFlatten3D, 3
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphPoolingReturnIndicesGlobalFlatten4D, 4
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphPoolingReturnIndicesLocalFlatten1D, 5
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphPoolingReturnIndicesLocalFlatten2D, 6
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphPoolingReturnIndicesLocalFlatten3D, 7
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphPoolingReturnIndicesLocalFlatten4D, 8
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphPooling4DOpDescriptor.ceilMode
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphPooling4DOpDescriptor.setCeilMode_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphPooling4DOpDescriptor.includeZeroPadToAverage
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphPooling4DOpDescriptor.setIncludeZeroPadToAverage_,
            0,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphPooling4DOpDescriptor.ceilMode
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphPooling4DOpDescriptor.setCeilMode_,
            0,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphPooling4DOpDescriptor.includeZeroPadToAverage
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphPooling4DOpDescriptor.setIncludeZeroPadToAverage_,
            0,
        )
