import Metal
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLFunctionLogHelper(Metal.NSObject):
    def line(self):
        pass

    def column(self):
        pass

    def type(self):  # noqa: A003
        return 1


class TestMTLFunctionLog(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Metal.MTLFunctionLogType)
        self.assertEqual(Metal.MTLFunctionLogTypeValidation, 0)

    @min_sdk_level("11.0")
    def test_protocols11_0(self):
        self.assertProtocolExists("MTLLogContainer", Metal)
        self.assertProtocolExists("MTLFunctionLogDebugLocation", Metal)
        self.assertProtocolExists("MTLFunctionLog", Metal)

    def test_protocol_methods(self):
        self.assertResultHasType(TestMTLFunctionLogHelper.line, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLFunctionLogHelper.column, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLFunctionLogHelper.type, objc._C_NSInteger)
