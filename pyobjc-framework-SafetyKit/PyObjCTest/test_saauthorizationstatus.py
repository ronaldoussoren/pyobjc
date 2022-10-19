from PyObjCTools.TestSupport import TestCase

import SafetyKit


class TestSAAuthorizationStatus(TestCase):
    def test_constants(self):
        self.assertIsEnumType(SafetyKit.SAAuthorizationStatus)
        self.assertEqual(SafetyKit.SAAuthorizationStatusNotDetermined, 0)
        self.assertEqual(SafetyKit.SAAuthorizationStatusDenied, 1)
        self.assertEqual(SafetyKit.SAAuthorizationStatusAuthorized, 2)
