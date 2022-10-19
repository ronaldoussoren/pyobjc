from PyObjCTools.TestSupport import TestCase

import SafetyKit


class TestSAError(TestCase):
    def test_constants(self):
        self.assertIsInstance(SafetyKit.SAErrorDomain, str)

        self.assertIsEnumType(SafetyKit.SAErrorCode)
        self.assertEqual(SafetyKit.SAErrorNotAuthorized, 1)
        self.assertEqual(SafetyKit.SAErrorNotAllowed, 2)
        self.assertEqual(SafetyKit.SAErrorInvalidArgument, 3)
        self.assertEqual(SafetyKit.SAErrorOperationFailed, 4)
