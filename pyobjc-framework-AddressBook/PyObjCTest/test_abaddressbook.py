
from PyObjCTools.TestSupport import *
from AddressBook import *

try:
    unicode
except NameError:
    unicode = str

class TestABAddressBook (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(ABAddressBook.save)
        self.assertResultIsBOOL(ABAddressBook.hasUnsavedChanges)
        self.assertResultIsBOOL(ABAddressBook.addRecord_)
        self.assertResultIsBOOL(ABAddressBook.removeRecord_)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(ABAddressBook.saveAndReturnError_)
        self.assertArgIsOut(ABAddressBook.saveAndReturnError_, 0)

    @min_os_level('10.7')
    def testMethods10_5(self):
        self.assertResultIsBOOL(ABAddressBook.addRecord_error_)
        self.assertArgIsOut(ABAddressBook.addRecord_error_, 1)
        self.assertResultIsBOOL(ABAddressBook.removeRecord_error_)
        self.assertArgIsOut(ABAddressBook.removeRecord_error_, 1)

    def testConstants(self):
        self.assertEqual(ABAddRecordsError, 1001)
        self.assertEqual(ABRemoveRecordsError, 1002)
        self.assertEqual(ABPropertyValueValidationError, 1012)
        self.assertEqual(ABPropertyUnsupportedBySourceError, 1013)
        self.assertEqual(ABPropertyReadOnlyError, 1014)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(ABAddressBookErrorDomain, unicode)
        self.assertIsInstance(ABMultiValueIdentifiersErrorKey, unicode)



if __name__ == "__main__":
    main()
