from PyObjCTools.TestSupport import TestCase
import objc
import MetalPerformanceShaders


class TestMPSCore_MPSCommandBufferHelper(MetalPerformanceShaders.NSObject):
    def retireHeap_cacheDelay_(self, a, b):
        pass


class TestMPSCore_MPSCommandBuffer(TestCase):
    def test_protocols(self):
        objc.protocolNamed("MPSHeapProvider")

    def test_methods(self):
        self.assertArgHasType(
            TestMPSCore_MPSCommandBufferHelper.retireHeap_cacheDelay_, 1, objc._C_DBL
        )
