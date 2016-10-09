from PyObjCTools.TestSupport import *
import AddressBook
import Cocoa

class TestABPersonView (TestCase):
    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(AddressBook.ABPersonView.editing)
        self.assertArgIsBOOL(AddressBook.ABPersonView.setEditing_, 0)

    @min_os_level('10.8')
    @max_os_level('10.11')
    def testMethods(self):
        v = AddressBook.ABPersonView.alloc().init()
        self.assertResultIsBOOL(v.shouldShowLinkedPeople)
        self.assertArgIsBOOL(v.setShouldShowLinkedPeople_, 0)

if __name__ == "__main__":
    main()
