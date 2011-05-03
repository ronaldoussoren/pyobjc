
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABAddressBook (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(ABAddressBook.save)
        self.assertResultIsBOOL(ABAddressBook.hasUnsavedChanges)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(ABAddressBook.saveAndReturnError_)
        self.assertArgIsOut(ABAddressBook.saveAndReturnError_, 0)

if __name__ == "__main__":
    main()
