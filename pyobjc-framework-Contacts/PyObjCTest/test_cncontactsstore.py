from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import Contacts


class TestCNContactStore(TestCase):
    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(Contacts.CNEntityTypeContacts, 0)

        self.assertEqual(Contacts.CNAuthorizationStatusNotDetermined, 0)
        self.assertEqual(Contacts.CNAuthorizationStatusRestricted, 1)
        self.assertEqual(Contacts.CNAuthorizationStatusDenied, 2)
        self.assertEqual(Contacts.CNAuthorizationStatusAuthorized, 3)

    @min_os_level("10.11")
    def testMethods(self):
        self.assertArgIsBlock(
            Contacts.CNContactStore.requestAccessForEntityType_completionHandler_,
            1,
            b"v" + objc._C_NSBOOL + b"@",
        )
        self.assertArgIsOut(
            Contacts.CNContactStore.unifiedContactsMatchingPredicate_keysToFetch_error_,
            2,
        )
        self.assertArgIsOut(
            Contacts.CNContactStore.unifiedContactWithIdentifier_keysToFetch_error_, 2
        )
        self.assertArgIsOut(
            Contacts.CNContactStore.unifiedMeContactWithKeysToFetch_error_, 1
        )

        self.assertResultIsBOOL(
            Contacts.CNContactStore.enumerateContactsWithFetchRequest_error_usingBlock_
        )
        self.assertArgIsOut(
            Contacts.CNContactStore.enumerateContactsWithFetchRequest_error_usingBlock_,
            1,
        )
        self.assertArgIsBlock(
            Contacts.CNContactStore.enumerateContactsWithFetchRequest_error_usingBlock_,
            2,
            b"v@o^Z",
        )

        self.assertArgIsOut(Contacts.CNContactStore.groupsMatchingPredicate_error_, 1)
        self.assertArgIsOut(
            Contacts.CNContactStore.containersMatchingPredicate_error_, 1
        )

        self.assertResultIsBOOL(Contacts.CNContactStore.executeSaveRequest_error_)
        self.assertArgIsOut(Contacts.CNContactStore.executeSaveRequest_error_, 1)
