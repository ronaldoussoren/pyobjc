from PyObjCTools.TestSupport import *
import AddressBook

class TestABImageLoading (TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AddressBook.ABPerson.setImageData_)

if __name__ == "__main__":
    main()
