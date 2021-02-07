import Metal
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLFunctionHandleHelper(Metal.NSObject):
    def functionType(self):
        return 1


class TestMTLFunctionHandle(TestCase):
    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("MTLFunctionHandle")

    def test_methods(self):
        self.assertResultHasType(
            TestMTLFunctionHandleHelper.functionType, objc._C_NSUInteger
        )
