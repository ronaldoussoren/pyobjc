import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSURLCredential(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSURLCredentialPersistence)

    def testConstants(self):
        self.assertEqual(Foundation.NSURLCredentialPersistenceNone, 0)
        self.assertEqual(Foundation.NSURLCredentialPersistenceForSession, 1)
        self.assertEqual(Foundation.NSURLCredentialPersistencePermanent, 2)
        self.assertEqual(Foundation.NSURLCredentialPersistenceSynchronizable, 3)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSURLCredential.hasPassword)
