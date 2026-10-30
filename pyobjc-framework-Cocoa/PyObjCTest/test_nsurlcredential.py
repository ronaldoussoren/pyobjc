import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSURLCredential(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSURLCredentialPersistence)
        self.assertEqual(Foundation.NSURLCredentialPersistenceNone, 0)
        self.assertEqual(Foundation.NSURLCredentialPersistenceForSession, 1)
        self.assertEqual(Foundation.NSURLCredentialPersistencePermanent, 2)
        self.assertEqual(Foundation.NSURLCredentialPersistenceSynchronizable, 3)

    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSURLCredential.hasPassword)
