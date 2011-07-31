from PyObjCTools.TestSupport import *
import AddressBook

class TestABMutableMultiValue (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AddressBook.ABMutableMultiValue.removeValueAndLabelAtIndex_)
        self.assertResultIsBOOL(AddressBook.ABMutableMultiValue.replaceValueAtIndex_withValue_)
        self.assertResultIsBOOL(AddressBook.ABMutableMultiValue.replaceLabelAtIndex_withLabel_)
        self.assertResultIsBOOL(AddressBook.ABMutableMultiValue.setPrimaryIdentifier_)

if __name__ == "__main__":
    main()
