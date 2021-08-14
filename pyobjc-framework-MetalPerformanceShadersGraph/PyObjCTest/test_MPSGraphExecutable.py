from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph

MPSGraphExecutableCompletionHandler = b"v@@"
MPSGraphExecutableScheduledHandler = b"v@@"


class TestMPSGraphExecutable(TestCase):
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
