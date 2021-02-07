import Metal
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLVisibleFunctionTableHelper(Metal.NSObject):
    def setFunction_atIndex_(self, a, b):
        pass

    def setFunctions_withRange_(self, a, b):
        pass


class TestMTLVisibleFunctionTable(TestCase):
    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("MTLVisibleFunctionTable")

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
