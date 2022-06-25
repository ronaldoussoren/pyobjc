import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestMTLParallelRenderCommandEncoderHelper(Metal.NSObject):
    def setColorStoreAction_atIndex_(self, a, b):
        pass

    def setDepthStoreAction_(self, a):
        pass

    def setStencilStoreAction_(self, a):
        pass

    def setColorStoreActionOptions_atIndex_(self, a, b):
        pass

    def setDepthStoreActionOptions_(self, a):
        pass

    def setStencilStoreActionOptions_(self, a):
        pass


class TestMTLParallelRenderCommandEncoder(TestCase):
    @min_sdk_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("MTLParallelRenderCommandEncoder")

    def test_methods(self):
        self.assertArgHasType(
            TestMTLParallelRenderCommandEncoderHelper.setColorStoreAction_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLParallelRenderCommandEncoderHelper.setDepthStoreAction_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLParallelRenderCommandEncoderHelper.setStencilStoreAction_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLParallelRenderCommandEncoderHelper.setColorStoreActionOptions_atIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLParallelRenderCommandEncoderHelper.setColorStoreActionOptions_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLParallelRenderCommandEncoderHelper.setDepthStoreActionOptions_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLParallelRenderCommandEncoderHelper.setStencilStoreActionOptions_,
            0,
            objc._C_NSUInteger,
        )
