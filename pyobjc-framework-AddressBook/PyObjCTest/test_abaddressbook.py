import AddressBook
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestABAddressBook(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AddressBook.ABAddressBook.save)
        self.assertResultIsBOOL(AddressBook.ABAddressBook.hasUnsavedChanges)
        self.assertResultIsBOOL(AddressBook.ABAddressBook.addRecord_)
        self.assertResultIsBOOL(AddressBook.ABAddressBook.removeRecord_)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(AddressBook.ABAddressBook.saveAndReturnError_)
        self.assertArgIsOut(AddressBook.ABAddressBook.saveAndReturnError_, 0)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AddressBook.ABAddressBook.addRecord_error_)
        self.assertArgIsOut(AddressBook.ABAddressBook.addRecord_error_, 1)
        self.assertResultIsBOOL(AddressBook.ABAddressBook.removeRecord_error_)
        self.assertArgIsOut(AddressBook.ABAddressBook.removeRecord_error_, 1)

    def testConstants(self):
        self.assertEqual(AddressBook.ABAddRecordsError, 1001)
        self.assertEqual(AddressBook.ABRemoveRecordsError, 1002)
        self.assertEqual(AddressBook.ABPropertyValueValidationError, 1012)
        self.assertEqual(AddressBook.ABPropertyUnsupportedBySourceError, 1013)
        self.assertEqual(AddressBook.ABPropertyReadOnlyError, 1014)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AddressBook.ABAddressBookErrorDomain, str)
        self.assertIsInstance(AddressBook.ABMultiValueIdentifiersErrorKey, str)
