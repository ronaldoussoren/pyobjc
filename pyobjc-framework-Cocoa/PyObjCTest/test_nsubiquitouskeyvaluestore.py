from PyObjCTools.TestSupport import *
from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSUbiquitousKeyValueStore (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(NSUbiquitousKeyValueStore.boolForKey_)
        self.assertArgIsBOOL(NSUbiquitousKeyValueStore.setBool_forKey_, 0)
        self.assertResultIsBOOL(NSUbiquitousKeyValueStore.synchronize)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(NSUbiquitousKeyValueStoreDidChangeExternallyNotification, unicode)
        self.assertIsInstance(NSUbiquitousKeyValueStoreChangeReasonKey, unicode)
        self.assertIsInstance(NSUbiquitousKeyValueStoreChangedKeysKey, unicode)

        self.assertEqual(NSUbiquitousKeyValueStoreServerChange, 0)
        self.assertEqual(NSUbiquitousKeyValueStoreInitialSyncChange, 1)
        self.assertEqual(NSUbiquitousKeyValueStoreQuotaViolationChange, 2)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(NSUbiquitousKeyValueStoreAccountChange, 3)

if __name__ ==  "__main__":
    main()
