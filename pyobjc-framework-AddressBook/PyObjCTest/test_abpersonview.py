from PyObjCTools.TestSupport import *
import AddressBook

class TestABPersonView (TestCase):
    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(AddressBook.ABPersonView.editing)
        self.assertArgIsBOOL(AddressBook.ABPersonView.setEditing_, 0)

if __name__ == "__main__":
    main()
