import AddressBook
from PyObjCTools.TestSupport import TestCase


class TestABAddressBook(TestCase):
    def test_constants(self):
        self.assertEqual(AddressBook.ABAddRecordsError, 1001)
        self.assertEqual(AddressBook.ABRemoveRecordsError, 1002)
        self.assertEqual(AddressBook.ABPropertyValueValidationError, 1012)
        self.assertEqual(AddressBook.ABPropertyUnsupportedBySourceError, 1013)
        self.assertEqual(AddressBook.ABPropertyReadOnlyError, 1014)

        self.assertIsInstance(AddressBook.ABAddressBookErrorDomain, str)
        self.assertIsInstance(AddressBook.ABMultiValueIdentifiersErrorKey, str)

    def test_methods(self):
        self.assertResultIsBOOL(AddressBook.ABAddressBook.save)
        self.assertResultIsBOOL(AddressBook.ABAddressBook.hasUnsavedChanges)
        self.assertResultIsBOOL(AddressBook.ABAddressBook.addRecord_)
        self.assertResultIsBOOL(AddressBook.ABAddressBook.removeRecord_)

        self.assertResultIsBOOL(AddressBook.ABAddressBook.saveAndReturnError_)
        self.assertArgIsOut(AddressBook.ABAddressBook.saveAndReturnError_, 0)

        self.assertResultIsBOOL(AddressBook.ABAddressBook.addRecord_error_)
        self.assertArgIsOut(AddressBook.ABAddressBook.addRecord_error_, 1)
        self.assertResultIsBOOL(AddressBook.ABAddressBook.removeRecord_error_)
        self.assertArgIsOut(AddressBook.ABAddressBook.removeRecord_error_, 1)
