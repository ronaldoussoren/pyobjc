from PyObjCTools.TestSupport import TestCase, min_os_level

import ClassKit


class TestCLSActivity(TestCase):
    def test_constants(self):
        self.assertEqual(ClassKit.CLSErrorCodeNone, 0)
        self.assertEqual(ClassKit.CLSErrorCodeClassKitUnavailable, 1)
        self.assertEqual(ClassKit.CLSErrorCodeInvalidArgument, 2)
        self.assertEqual(ClassKit.CLSErrorCodeInvalidModification, 3)
        self.assertEqual(ClassKit.CLSErrorCodeAuthorizationDenied, 4)
        self.assertEqual(ClassKit.CLSErrorCodeDatabaseInaccessible, 5)
        self.assertEqual(ClassKit.CLSErrorCodeLimits, 6)
        self.assertEqual(ClassKit.CLSErrorCodeInvalidCreate, 7)
        self.assertEqual(ClassKit.CLSErrorCodeInvalidUpdate, 8)
        self.assertEqual(ClassKit.CLSErrorCodePartialFailure, 9)

    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(ClassKit.CLSErrorObjectKey, str)
        self.assertIsInstance(ClassKit.CLSErrorUnderlyingErrorsKey, str)

        self.assertIsInstance(ClassKit.CLSPredicateKeyPathDateCreated, str)
        self.assertIsInstance(ClassKit.CLSPredicateKeyPathIdentifier, str)
        self.assertIsInstance(ClassKit.CLSPredicateKeyPathTitle, str)
        self.assertIsInstance(ClassKit.CLSPredicateKeyPathUniversalLinkURL, str)
        self.assertIsInstance(ClassKit.CLSPredicateKeyPathTopic, str)
        self.assertIsInstance(ClassKit.CLSPredicateKeyPathParent, str)
