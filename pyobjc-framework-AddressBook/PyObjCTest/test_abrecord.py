import AddressBook
from PyObjCTools.TestSupport import TestCase


class TestABRecord(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AddressBook.ABRecord.setValue_forProperty_)
        self.assertResultIsBOOL(AddressBook.ABRecord.removeValueForProperty_)
        self.assertResultIsBOOL(AddressBook.ABRecord.isReadOnly)

        self.assertResultIsBOOL(AddressBook.ABRecord.setValue_forProperty_error_)
        self.assertArgIsOut(AddressBook.ABRecord.setValue_forProperty_error_, 2)
