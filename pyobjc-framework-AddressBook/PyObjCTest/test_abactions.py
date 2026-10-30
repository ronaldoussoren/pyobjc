import AddressBook
from PyObjCTools.TestSupport import TestCase


class TestABActionHelper(AddressBook.NSObject):
    def shouldEnableActionForPerson_identifier_(self, person, identifier):
        return True


class TestABActions(TestCase):
    def test_protocol_methods(self):
        # Informal protocol
        self.assertResultIsBOOL(
            TestABActionHelper.shouldEnableActionForPerson_identifier_
        )
