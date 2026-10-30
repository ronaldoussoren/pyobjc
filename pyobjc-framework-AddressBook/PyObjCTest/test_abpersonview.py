import AddressBook
from PyObjCTools.TestSupport import TestCase, max_os_level


class TestABPersonView(TestCase):
    def test_methods(self):
        v = AddressBook.ABPersonView.alloc().init()
        self.assertResultIsBOOL(v.editing)
        self.assertArgIsBOOL(v.setEditing_, 0)

    @max_os_level("10.11")
    def test_methods_dropped_10_11(self):
        v = AddressBook.ABPersonView.alloc().init()
        self.assertResultIsBOOL(v.shouldShowLinkedPeople)
        self.assertArgIsBOOL(v.setShouldShowLinkedPeople_, 0)
