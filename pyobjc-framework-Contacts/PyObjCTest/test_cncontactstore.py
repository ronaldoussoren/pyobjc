from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNContactStore(TestCase):
    def test_methods(self):
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

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsOut(
            Contacts.CNContactStore.enumeratorForContactFetchRequest_error_, 1
        )
        self.assertArgIsOut(
            Contacts.CNContactStore.enumeratorForChangeHistoryFetchRequest_error_, 1
        )
