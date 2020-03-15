import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSUbiquitousKeyValueStore(TestCase):
    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(Foundation.NSUbiquitousKeyValueStore.boolForKey_)
        self.assertArgIsBOOL(Foundation.NSUbiquitousKeyValueStore.setBool_forKey_, 0)
        self.assertResultIsBOOL(Foundation.NSUbiquitousKeyValueStore.synchronize)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(
            Foundation.NSUbiquitousKeyValueStoreDidChangeExternallyNotification, str
        )
        self.assertIsInstance(Foundation.NSUbiquitousKeyValueStoreChangeReasonKey, str)
        self.assertIsInstance(Foundation.NSUbiquitousKeyValueStoreChangedKeysKey, str)

        self.assertEqual(Foundation.NSUbiquitousKeyValueStoreServerChange, 0)
        self.assertEqual(Foundation.NSUbiquitousKeyValueStoreInitialSyncChange, 1)
        self.assertEqual(Foundation.NSUbiquitousKeyValueStoreQuotaViolationChange, 2)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(Foundation.NSUbiquitousKeyValueStoreAccountChange, 3)
