import AddressBook
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestABPersonPicker(TestCase):
    @min_os_level("10.9")
    def testMethods_10_9(self):
        m = AddressBook.ABPersonPicker.showRelativeToRect_ofView_preferredEdge_
        self.assertArgHasType(m, 0, AddressBook.NSRect.__typestr__)
