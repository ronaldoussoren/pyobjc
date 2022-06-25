import Metal
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLVisibleFunctionTableHelper(Metal.NSObject):
    def setFunction_atIndex_(self, a, b):
        pass

    def setFunctions_withRange_(self, a, b):
        pass

    def gpuResourceID(self):
        return 1


class TestMTLVisibleFunctionTable(TestCase):
    @min_sdk_level("11.0")
    def test_protocols11_0(self):
        self.assertProtocolExists("MTLVisibleFunctionTable")

    def test_methods(self):
        self.assertArgHasType(
            TestMTLVisibleFunctionTableHelper.setFunction_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLVisibleFunctionTableHelper.setFunctions_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLVisibleFunctionTableHelper.setFunctions_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLVisibleFunctionTableHelper.setFunctions_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertResultHasType(
            TestMTLVisibleFunctionTableHelper.gpuResourceID,
            Metal.MTLResourceID.__typestr__,
        )
