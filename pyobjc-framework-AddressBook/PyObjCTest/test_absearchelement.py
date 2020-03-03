import AddressBook
from PyObjCTools.TestSupport import TestCase


class TestABSearchElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AddressBook.ABSearchElement.matchesRecord_)
