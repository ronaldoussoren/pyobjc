import CoreMotion
from PyObjCTools.TestSupport import TestCase


class TestCMAccelerometer(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreMotion.CMAuthorizationStatus)
        self.assertEqual(CoreMotion.CMAuthorizationStatusNotDetermined, 0)
        self.assertEqual(CoreMotion.CMAuthorizationStatusRestricted, 1)
        self.assertEqual(CoreMotion.CMAuthorizationStatusDenied, 2)
        self.assertEqual(CoreMotion.CMAuthorizationStatusAuthorized, 3)
