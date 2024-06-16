from PyObjCTools.TestSupport import TestCase
import LocalAuthentication


class TestLACompanionType(TestCase):
    def test_enum(self):
        self.assertIsEnumType(LocalAuthentication.LACompanionType)
        self.assertEqual(
            LocalAuthentication.LACompanionTypeWatch,
            LocalAuthentication.kLACompanionTypeWatch,
        )
        self.assertEqual(
            LocalAuthentication.LACompanionTypeMac,
            LocalAuthentication.kLACompanionTypeMac,
        )
