import AddressBook
from PyObjCTools.TestSupport import TestCase, min_os_level, max_os_level


class TestABPersonView(TestCase):
    @min_os_level("10.7")
    def testMethods(self):
        v = AddressBook.ABPersonView.alloc().init()
        self.assertResultIsBOOL(v.editing)
        self.assertArgIsBOOL(v.setEditing_, 0)

    @min_os_level("10.8")
    @max_os_level("10.11")
    def testMethods10_8(self):
        v = AddressBook.ABPersonView.alloc().init()
        self.assertResultIsBOOL(v.shouldShowLinkedPeople)
        self.assertArgIsBOOL(v.setShouldShowLinkedPeople_, 0)
