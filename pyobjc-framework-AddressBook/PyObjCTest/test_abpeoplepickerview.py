import AddressBook
from PyObjCTools.TestSupport import TestCase


class TestABPeoplePickerView(TestCase):
    def testConstants(self):
        self.assertEqual(AddressBook.ABNoValueSelection, 0)
        self.assertEqual(AddressBook.ABSingleValueSelection, 1)
        self.assertEqual(AddressBook.ABMultipleValueSelection, 2)

        self.assertIsInstance(
            AddressBook.ABPeoplePickerGroupSelectionDidChangeNotification, str
        )
        self.assertIsInstance(
            AddressBook.ABPeoplePickerNameSelectionDidChangeNotification, str
        )
        self.assertIsInstance(
            AddressBook.ABPeoplePickerValueSelectionDidChangeNotification, str
        )
        self.assertIsInstance(
            AddressBook.ABPeoplePickerDisplayedPropertyDidChangeNotification, str
        )

    def testMethods(self):
        self.assertArgIsBOOL(
            AddressBook.ABPeoplePickerView.selectGroup_byExtendingSelection_, 1
        )
        self.assertArgIsBOOL(
            AddressBook.ABPeoplePickerView.selectRecord_byExtendingSelection_, 1
        )
        self.assertArgIsBOOL(
            AddressBook.ABPeoplePickerView.selectIdentifier_forPerson_byExtendingSelection_,
            2,
        )

        self.assertResultIsBOOL(AddressBook.ABPeoplePickerView.allowsGroupSelection)
        self.assertArgIsBOOL(AddressBook.ABPeoplePickerView.setAllowsGroupSelection_, 0)
        self.assertResultIsBOOL(AddressBook.ABPeoplePickerView.allowsMultipleSelection)
        self.assertArgIsBOOL(
            AddressBook.ABPeoplePickerView.setAllowsMultipleSelection_, 0
        )

        self.assertArgIsSEL(
            AddressBook.ABPeoplePickerView.setGroupDoubleAction_, 0, b"v@:@"
        )
        self.assertArgIsSEL(
            AddressBook.ABPeoplePickerView.setNameDoubleAction_, 0, b"v@:@"
        )
