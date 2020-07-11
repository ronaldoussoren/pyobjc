import Metal
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLIntersectionFunctionTableHelper(Metal.NSObject):
    def setBuffer_offset_atIndex_(self, a, b, c):
        pass

    def setBuffers_offsets_withRange_(self, a, b, c):
        pass

    def setFunction_atIndex_(self, a, b):
        pass

    def setFunctions_withRange_(self, a, b):
        pass


class TestMTLIntersectionFunctionTable(TestCase):
    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("MTLIntersectionFunctionTable")

    def test_methods(self):
        self.assertArgHasType(
            TestMTLIntersectionFunctionTableHelper.setBuffer_offset_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIntersectionFunctionTableHelper.setBuffer_offset_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIntersectionFunctionTableHelper.setBuffers_offsets_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLIntersectionFunctionTableHelper.setBuffers_offsets_withRange_, 0, 2
        )
        self.assertArgHasType(
            TestMTLIntersectionFunctionTableHelper.setBuffers_offsets_withRange_,
            1,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLIntersectionFunctionTableHelper.setBuffers_offsets_withRange_, 1, 2
        )
        self.assertArgHasType(
            TestMTLIntersectionFunctionTableHelper.setBuffers_offsets_withRange_,
            2,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLIntersectionFunctionTableHelper.setFunction_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIntersectionFunctionTableHelper.setFunction_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIntersectionFunctionTableHelper.setFunctions_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLIntersectionFunctionTableHelper.setFunctions_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLIntersectionFunctionTableHelper.setFunctions_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )
