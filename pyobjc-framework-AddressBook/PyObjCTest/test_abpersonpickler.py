import AddressBook
from PyObjCTools.TestSupport import TestCase, min_os_level, onlyOn64Bit


class TestABPersonPicker(TestCase):
    @min_os_level("10.9")
    @onlyOn64Bit
    def testMethods_10_9(self):
        m = AddressBook.ABPersonPicker.showRelativeToRect_ofView_preferredEdge_
        self.assertArgHasType(m, 0, AddressBook.NSRect.__typestr__)
