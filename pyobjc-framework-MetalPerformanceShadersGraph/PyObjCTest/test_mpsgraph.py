from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraph(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphOptimization)
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphOptions)
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphOptimizationProfile)
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphExecutionStage)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphOptionsNone, 0)
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphOptionsSynchronizeResults, 1
        )
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphOptionsVerbose, 2)
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphOptionsDefault,
            MetalPerformanceShadersGraph.MPSGraphOptionsSynchronizeResults,
        )

        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphOptimizationLevel0, 0)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphOptimizationLevel1, 1)

        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphOptimizationProfilePerformance, 0
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphOptimizationProfilePowerEfficiency, 1
        )

        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphExecutionStageCompleted, 0
        )

    @min_os_level("11.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphExecutionDescriptor.waitUntilCompleted
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphExecutionDescriptor.setWaitUntilCompleted_,
            0,
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphCompilationDescriptor.waitForCompilationCompletion
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphCompilationDescriptor.setWaitForCompilationCompletion_,
            0,
        )
        self.assertResultIsBlock(
            MetalPerformanceShadersGraph.MPSGraphCompilationDescriptor.compilationCompletionHandler,
            b"v@@",
        )
        self.assertArgIsBlock(
            MetalPerformanceShadersGraph.MPSGraphCompilationDescriptor.setCompilationCompletionHandler_,
            0,
            b"v@@",
        )
