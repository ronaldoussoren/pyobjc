import Metal
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLFunctionHandleHelper(Metal.NSObject):
    def functionType(self):
        return 1


class TestMTLFunctionHandle(TestCase):
    @min_sdk_level("11.0")
    def test_protocols11_0(self):
        self.assertProtocolExists("MTLFunctionHandle")

    def test_methods(self):
        self.assertResultHasType(
            TestMTLFunctionHandleHelper.functionType, objc._C_NSUInteger
        )
