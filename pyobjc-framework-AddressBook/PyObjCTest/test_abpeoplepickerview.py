
from PyObjCTools.TestSupport import *
from AddressBook import *

try:
    unicode
except NameError:
    unicode = str

class TestABPeoplePickerView (TestCase):
    def testConstants(self):
        self.assertEqual(ABNoValueSelection, 0)
        self.assertEqual(ABSingleValueSelection, 1)
        self.assertEqual(ABMultipleValueSelection, 2)

        self.assertIsInstance(ABPeoplePickerGroupSelectionDidChangeNotification, unicode)
        self.assertIsInstance(ABPeoplePickerNameSelectionDidChangeNotification, unicode)
        self.assertIsInstance(ABPeoplePickerValueSelectionDidChangeNotification, unicode)
        self.assertIsInstance(ABPeoplePickerDisplayedPropertyDidChangeNotification, unicode)

    def testMethods(self):
        self.assertArgIsBOOL(ABPeoplePickerView.selectGroup_byExtendingSelection_, 1)
        self.assertArgIsBOOL(ABPeoplePickerView.selectRecord_byExtendingSelection_, 1)
        self.assertArgIsBOOL(ABPeoplePickerView.selectIdentifier_forPerson_byExtendingSelection_, 2)

        self.assertResultIsBOOL(ABPeoplePickerView.allowsGroupSelection)
        self.assertArgIsBOOL(ABPeoplePickerView.setAllowsGroupSelection_, 0)
        self.assertResultIsBOOL(ABPeoplePickerView.allowsMultipleSelection)
        self.assertArgIsBOOL(ABPeoplePickerView.setAllowsMultipleSelection_, 0)

        self.assertArgIsSEL(ABPeoplePickerView.setGroupDoubleAction_, 0, b'v@:@')
        self.assertArgIsSEL(ABPeoplePickerView.setNameDoubleAction_, 0, b'v@:@')



if __name__ == "__main__":
    main()
