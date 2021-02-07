import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestMTLIndirectCommandBufferHelper(Metal.NSObject):
    def resetWithRange_(self, a):
        pass

    def indirectRenderCommandAtIndex_(self, a):
        return 1


class TestMTLIndirectCommandBuffer(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLIndirectCommandTypeDraw, 1 << 0)
        self.assertEqual(Metal.MTLIndirectCommandTypeDrawIndexed, 1 << 1)
        self.assertEqual(Metal.MTLIndirectCommandTypeDrawPatches, 1 << 2)
        self.assertEqual(Metal.MTLIndirectCommandTypeDrawIndexedPatches, 1 << 3)
        self.assertEqual(Metal.MTLIndirectCommandTypeConcurrentDispatch, 1 << 5)
        self.assertEqual(Metal.MTLIndirectCommandTypeConcurrentDispatchThreads, 1 << 6)

    def test_structs(self):
        v = Metal.MTLIndirectCommandBufferExecutionRange()
        self.assertEqual(v.location, 0)
        self.assertEqual(v.length, 0)

    def test_functions(self):
        v = Metal.MTLIndirectCommandBufferExecutionRangeMake(1, 2)
        self.assertIsInstance(v, Metal.MTLIndirectCommandBufferExecutionRange)
        self.assertEqual(v, Metal.MTLIndirectCommandBufferExecutionRange(1, 2))

    @min_sdk_level("10.14")
    def test_protocols(self):
        objc.protocolNamed("MTLIndirectCommandBuffer")

    def test_methods(self):
        self.assertArgHasType(
            TestMTLIndirectCommandBufferHelper.resetWithRange_,
            0,
            Metal.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandBufferHelper.indirectRenderCommandAtIndex_,
            0,
            objc._C_NSUInteger,
        )

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(
            Metal.MTLIndirectCommandBufferDescriptor.alloc().init().inheritPipelineState
        )
        self.assertArgIsBOOL(
            Metal.MTLIndirectCommandBufferDescriptor.alloc()
            .init()
            .setInheritPipelineState_,
            0,
        )

        self.assertResultIsBOOL(
            Metal.MTLIndirectCommandBufferDescriptor.alloc().init().inheritBuffers
        )
        self.assertArgIsBOOL(
            Metal.MTLIndirectCommandBufferDescriptor.alloc().init().setInheritBuffers_,
            0,
        )
