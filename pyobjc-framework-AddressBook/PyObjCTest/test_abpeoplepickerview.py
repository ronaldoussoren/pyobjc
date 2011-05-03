
from PyObjCTools.TestSupport import *
from AddressBook import *

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

if __name__ == "__main__":
    main()
