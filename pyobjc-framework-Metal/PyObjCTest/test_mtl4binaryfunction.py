import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestMTL4BinaryFunctionHelper(Metal.NSObject):
    def functionType(self):
        return 1


class TestMTL4BinaryFunction(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4BinaryFunction")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMTL4BinaryFunctionHelper.functionType, objc._C_NSUInteger
        )
