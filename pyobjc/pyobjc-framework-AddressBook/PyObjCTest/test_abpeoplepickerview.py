
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABPeoplePickerView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(ABNoValueSelection, 0)
        self.failUnlessEqual(ABSingleValueSelection, 1)
        self.failUnlessEqual(ABMultipleValueSelection, 2)

        self.failUnlessIsInstance(ABPeoplePickerGroupSelectionDidChangeNotification, unicode)
        self.failUnlessIsInstance(ABPeoplePickerNameSelectionDidChangeNotification, unicode)
        self.failUnlessIsInstance(ABPeoplePickerValueSelectionDidChangeNotification, unicode)
        self.failUnlessIsInstance(ABPeoplePickerDisplayedPropertyDidChangeNotification, unicode)

    def testMethods(self):
        self.failUnlessArgIsBOOL(ABPeoplePickerView.selectGroup_byExtendingSelection_, 1)
        self.failUnlessArgIsBOOL(ABPeoplePickerView.selectRecord_byExtendingSelection_, 1)
        self.failUnlessArgIsBOOL(ABPeoplePickerView.selectIdentifier_forPerson_byExtendingSelection_, 2)

if __name__ == "__main__":
    main()
