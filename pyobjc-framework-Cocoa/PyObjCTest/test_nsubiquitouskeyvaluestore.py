import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSUbiquitousKeyValueStore(TestCase):
    def test_enums(self):
        # Unnamed enum
        self.assertEqual(Foundation.NSUbiquitousKeyValueStoreServerChange, 0)
        self.assertEqual(Foundation.NSUbiquitousKeyValueStoreInitialSyncChange, 1)
        self.assertEqual(Foundation.NSUbiquitousKeyValueStoreQuotaViolationChange, 2)
        self.assertEqual(Foundation.NSUbiquitousKeyValueStoreAccountChange, 3)

    def test_constants(self):
        self.assertIsInstance(
            Foundation.NSUbiquitousKeyValueStoreDidChangeExternallyNotification, str
        )
        self.assertIsInstance(Foundation.NSUbiquitousKeyValueStoreChangeReasonKey, str)
        self.assertIsInstance(Foundation.NSUbiquitousKeyValueStoreChangedKeysKey, str)

    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSUbiquitousKeyValueStore.boolForKey_)
        self.assertArgIsBOOL(Foundation.NSUbiquitousKeyValueStore.setBool_forKey_, 0)
        self.assertResultIsBOOL(Foundation.NSUbiquitousKeyValueStore.synchronize)
