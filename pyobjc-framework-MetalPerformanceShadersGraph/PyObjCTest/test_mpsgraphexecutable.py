from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph

MPSGraphExecutableCompletionHandler = b"v@@"
MPSGraphExecutableScheduledHandler = b"v@@"


class TestMPSGraphExecutable(TestCase):
    def test_constants(self):
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphDeploymentPlatform)
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphDeploymentPlatformMacOS, 0
        )
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphDeploymentPlatformIOS, 1)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphDeploymentPlatformTvOS, 2)
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphDeploymentPlatformVisionOS, 3
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBlock(
            MetalPerformanceShadersGraph.MPSGraphExecutableExecutionDescriptor.scheduledHandler,
            MPSGraphExecutableScheduledHandler,
        )
        self.assertArgIsBlock(
            MetalPerformanceShadersGraph.MPSGraphExecutableExecutionDescriptor.setScheduledHandler_,
            0,
            MPSGraphExecutableScheduledHandler,
        )
        self.assertResultIsBlock(
            MetalPerformanceShadersGraph.MPSGraphExecutableExecutionDescriptor.completionHandler,
            MPSGraphExecutableCompletionHandler,
        )
        self.assertArgIsBlock(
            MetalPerformanceShadersGraph.MPSGraphExecutableExecutionDescriptor.setCompletionHandler_,
            0,
            MPSGraphExecutableCompletionHandler,
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphExecutableSerializationDescriptor.append
        )

        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphExecutableSerializationDescriptor.setAppend_,
            0,
        )
