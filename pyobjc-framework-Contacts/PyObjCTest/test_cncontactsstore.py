from PyObjCTools.TestSupport import *
import objc
import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2**32:
    import Contacts

    class TestCNContactStore (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertEqual(Contacts.CNEntityTypeContacts, 0)

            self.assertEqual(Contacts.CNAuthorizationStatusNotDetermined, 0)
            self.assertEqual(Contacts.CNAuthorizationStatusRestricted, 1)
            self.assertEqual(Contacts.CNAuthorizationStatusDenied, 2)
            self.assertEqual(Contacts.CNAuthorizationStatusAuthorized, 3)

        @min_os_level('10.11')
        def testMethods(self):
            self.assertArgIsBlock(Contacts.CNContactStore.requestAccessForEntityType_completionHandler_, 1, b'v' + objc._C_BOOL + b'@')
            self.assertArgIsOut(Contacts.CNContactStore.unifiedContactsMatchingPredicate_keysToFetch_error_, 2)
            self.assertArgIsOut(Contacts.CNContactStore.unifiedContactWithIdentifier_keysToFetch_error_, 2)
            self.assertArgIsOut(Contacts.CNContactStore.unifiedMeContactWithKeysToFetch_error_, 1)

            self.fail()

if __name__ == "__main__":
    main()
