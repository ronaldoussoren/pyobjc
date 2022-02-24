from PyObjCTools.TestSupport import TestCase
import CallKit


class TestCXHandle(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CallKit.CXHandleType)

    def test_constants(self):
        self.assertEqual(CallKit.CXHandleTypeGeneric, 1)
        self.assertEqual(CallKit.CXHandleTypePhoneNumber, 2)
        self.assertEqual(CallKit.CXHandleTypeEmailAddress, 3)

    def test_methods(self):
        self.assertResultIsBOOL(CallKit.CXHandle.isEqualToHandle_)
