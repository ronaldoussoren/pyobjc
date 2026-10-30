import AddressBook
from PyObjCTools.TestSupport import TestCase


class TestABPersonPicker(TestCase):
    def test_methods(self):
        m = AddressBook.ABPersonPicker.showRelativeToRect_ofView_preferredEdge_
        self.assertArgHasType(m, 0, AddressBook.NSRect.__typestr__)
