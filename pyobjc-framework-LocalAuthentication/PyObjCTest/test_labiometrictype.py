from PyObjCTools.TestSupport import TestCase
import LocalAuthentication


class TestLABiometryType(TestCase):
    def test_enum(self):
        self.assertIsEnumType(LocalAuthentication.LABiometryType)
        self.assertEqual(
            LocalAuthentication.LABiometryTypeNone,
            LocalAuthentication.kLABiometryTypeNone,
        )
        self.assertEqual(
            LocalAuthentication.LABiometryNone, LocalAuthentication.LABiometryTypeNone
        )
        self.assertEqual(
            LocalAuthentication.LABiometryTypeTouchID,
            LocalAuthentication.kLABiometryTypeTouchID,
        )
        self.assertEqual(
            LocalAuthentication.LABiometryTypeFaceID,
            LocalAuthentication.kLABiometryTypeFaceID,
        )
        self.assertEqual(
            LocalAuthentication.LABiometryTypeOpticID,
            LocalAuthentication.kLABiometryTypeOpticID,
        )
