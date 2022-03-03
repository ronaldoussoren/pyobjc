from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc
import MetalPerformanceShaders


class TestMPSCore_MPSCommandBufferHelper(MetalPerformanceShaders.NSObject):
    def retireHeap_cacheDelay_(self, a, b):
        pass


class TestMPSCore_MPSCommandBuffer(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("MPSHeapProvider")

    def test_methods(self):
        self.assertArgHasType(
            TestMPSCore_MPSCommandBufferHelper.retireHeap_cacheDelay_, 1, objc._C_DBL
        )
