
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABAddressBook (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(ABAddressBook.save)
        self.failUnlessResultIsBOOL(ABAddressBook.hasUnsavedChanges)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(ABAddressBook.saveAndReturnError_)
        self.failUnlessArgIsOut(ABAddressBook.saveAndReturnError_, 0)

if __name__ == "__main__":
    main()
