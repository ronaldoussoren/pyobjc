
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABAddressBook (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(ABAddressBook.save)
        self.failUnlessResultIsBOOL(ABAddressBook.saveAndReturnError_)
        self.failUnlessArgIsOut(ABAddressBook.saveAndReturnError_, 0)
        self.failUnlessResultIsBOOL(ABAddressBook.hasUnsavedChanges)

if __name__ == "__main__":
    main()
