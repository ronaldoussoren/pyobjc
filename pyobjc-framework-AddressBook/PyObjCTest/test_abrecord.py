import AddressBook
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestABRecord(TestCase):
    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AddressBook.ABRecord.setValue_forProperty_error_)
        self.assertArgIsOut(AddressBook.ABRecord.setValue_forProperty_error_, 2)

    def testMethods(self):
        self.assertResultIsBOOL(AddressBook.ABRecord.setValue_forProperty_)
        self.assertResultIsBOOL(AddressBook.ABRecord.removeValueForProperty_)
        self.assertResultIsBOOL(AddressBook.ABRecord.isReadOnly)
