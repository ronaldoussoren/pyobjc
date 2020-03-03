import AddressBook
from PyObjCTools.TestSupport import TestCase


class TestABActionHelper(AddressBook.NSObject):
    def shouldEnableActionForPerson_identifier_(self, person, identifier):
        return True


class TestABActions(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(
            TestABActionHelper.shouldEnableActionForPerson_identifier_
        )
