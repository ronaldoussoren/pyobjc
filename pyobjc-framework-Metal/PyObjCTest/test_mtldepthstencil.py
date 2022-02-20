import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestMTLDepthStencil(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLCompareFunction)
        self.assertIsEnumType(Metal.MTLStencilOperation)

    def test_constants(self):
        self.assertEqual(Metal.MTLCompareFunctionNever, 0)
        self.assertEqual(Metal.MTLCompareFunctionLess, 1)
        self.assertEqual(Metal.MTLCompareFunctionEqual, 2)
        self.assertEqual(Metal.MTLCompareFunctionLessEqual, 3)
        self.assertEqual(Metal.MTLCompareFunctionGreater, 4)
        self.assertEqual(Metal.MTLCompareFunctionNotEqual, 5)
        self.assertEqual(Metal.MTLCompareFunctionGreaterEqual, 6)
        self.assertEqual(Metal.MTLCompareFunctionAlways, 7)

        self.assertEqual(Metal.MTLStencilOperationKeep, 0)
        self.assertEqual(Metal.MTLStencilOperationZero, 1)
        self.assertEqual(Metal.MTLStencilOperationReplace, 2)
        self.assertEqual(Metal.MTLStencilOperationIncrementClamp, 3)
        self.assertEqual(Metal.MTLStencilOperationDecrementClamp, 4)
        self.assertEqual(Metal.MTLStencilOperationInvert, 5)
        self.assertEqual(Metal.MTLStencilOperationIncrementWrap, 6)
        self.assertEqual(Metal.MTLStencilOperationDecrementWrap, 7)

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertResultIsBOOL(
            Metal.MTLDepthStencilDescriptor.alloc().init().isDepthWriteEnabled
        )
        self.assertArgIsBOOL(
            Metal.MTLDepthStencilDescriptor.alloc().init().setDepthWriteEnabled_, 0
        )

    @min_sdk_level("10.11")
    def test_protocols(self):
        objc.protocolNamed("MTLDepthStencilState")
