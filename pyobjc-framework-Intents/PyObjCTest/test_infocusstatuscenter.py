from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents
import objc


class TestINFocusStatusCenter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INFocusStatusAuthorizationStatus)

    def test_constants(self):
        self.assertEqual(Intents.INFocusStatusAuthorizationStatusNotDetermined, 0)
        self.assertEqual(Intents.INFocusStatusAuthorizationStatusRestricted, 1)
        self.assertEqual(Intents.INFocusStatusAuthorizationStatusDenied, 2)
        self.assertEqual(Intents.INFocusStatusAuthorizationStatusAuthorized, 3)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBlock(
            Intents.INFocusStatusCenter.requestAuthorizationWithCompletionHandler_,
            0,
            b"v" + objc._C_NSInteger,
        )
