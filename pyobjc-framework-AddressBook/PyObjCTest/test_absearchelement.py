import AddressBook
from PyObjCTools.TestSupport import TestCase


class TestABSearchElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AddressBook.ABSearchElement.matchesRecord_)
