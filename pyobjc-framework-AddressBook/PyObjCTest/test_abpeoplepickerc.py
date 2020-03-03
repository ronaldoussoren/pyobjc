import AddressBook
import objc
from PyObjCTools.TestSupport import TestCase, expectedFailure, fourcc


class TestABPeoplePickerC(TestCase):
    def testConstants(self):
        self.assertEqual(AddressBook.kABPickerSingleValueSelection, 1 << 0)
        self.assertEqual(AddressBook.kABPickerMultipleValueSelection, 1 << 1)
        self.assertEqual(AddressBook.kABPickerAllowGroupSelection, 1 << 2)
        self.assertEqual(AddressBook.kABPickerAllowMultipleSelection, 1 << 3)
        self.assertEqual(AddressBook.kEventClassABPeoplePicker, fourcc(b"abpp"))
        self.assertEqual(AddressBook.kEventParamABPickerRef, fourcc(b"abpp"))
        self.assertEqual(AddressBook.kEventABPeoplePickerGroupSelectionChanged, 1)
        self.assertEqual(AddressBook.kEventABPeoplePickerNameSelectionChanged, 2)
        self.assertEqual(AddressBook.kEventABPeoplePickerValueSelectionChanged, 3)
        self.assertEqual(AddressBook.kEventABPeoplePickerDisplayedPropertyChanged, 4)
        self.assertEqual(AddressBook.kEventABPeoplePickerGroupDoubleClicked, 5)
        self.assertEqual(AddressBook.kEventABPeoplePickerNameDoubleClicked, 6)

    def testType(self):
        self.assertIsInstance(AddressBook.ABPickerRef, objc.objc_class)

    @expectedFailure
    def testFunctions(self):
        self.assertResultIsCFRetained(AddressBook.ABPickerCreate)

        ref = AddressBook.ABPickerCreate()

        try:
            self.assertIsInstance(
                ref,
                (AddressBook.ABPickerRef, objc.lookUpClass("ABPeoplePickerCAdapter")),
            )

        except objc.error:
            self.assertIsInstance(ref, AddressBook.ABPickerRef)

        AddressBook.ABPickerSetFrame(ref, ((90, 100), (200, 400)))
        r = AddressBook.ABPickerGetFrame(ref, None)
        self.assertIsInstance(r, AddressBook.NSRect)
        self.assertEqual(r, ((90, 100), (200, 400)))

        self.assertResultHasType(AddressBook.ABPickerIsVisible, objc._C_BOOL)
        r = AddressBook.ABPickerIsVisible(ref)
        self.assertIsInstance(r, bool)
        self.assertTrue(r is False)

        self.assertArgHasType(AddressBook.ABPickerSetVisibility, 1, objc._C_BOOL)
        AddressBook.ABPickerSetVisibility(ref, True)

        r = AddressBook.ABPickerIsVisible(ref)
        self.assertTrue(r is True)

        AddressBook.ABPickerSetVisibility(ref, False)

        r = AddressBook.ABPickerIsVisible(ref)
        self.assertTrue(r is False)

        r = AddressBook.ABPickerGetAttributes(ref)
        self.assertIsInstance(r, int)

        r = AddressBook.ABPickerChangeAttributes(
            ref, AddressBook.kABPickerAllowMultipleSelection, 0
        )
        self.assertTrue(r is None)

        AddressBook.ABPickerAddProperty(ref, AddressBook.kABFirstNameProperty)
        AddressBook.ABPickerAddProperty(ref, AddressBook.kABLastNameProperty)
        AddressBook.ABPickerRemoveProperty(ref, AddressBook.kABFirstNameProperty)

        v = AddressBook.ABPickerCopyProperties(ref)
        self.assertIsInstance(v, AddressBook.NSArray)

        # Disable detailed testing, the RemoveProperties function
        # doesn't actually remove. See radar #7999195.
        # self.assertEqual(tuple(v), (AddressBook.kABLastNameProperty,))

        AddressBook.ABPickerSetColumnTitle(
            ref, "Achternaam", AddressBook.kABLastNameProperty
        )
        v = AddressBook.ABPickerCopyColumnTitle(ref, AddressBook.kABLastNameProperty)
        self.assertResultIsCFRetained(AddressBook.ABPickerCopyColumnTitle)
        self.assertEqual(v, "Achternaam")

        AddressBook.ABPickerSetDisplayedProperty(ref, AddressBook.kABLastNameProperty)
        v = AddressBook.ABPickerCopyDisplayedProperty(ref)
        self.assertResultIsCFRetained(AddressBook.ABPickerCopyDisplayedProperty)
        self.assertIsInstance(v, str)

        v = AddressBook.ABPickerCopySelectedGroups(ref)
        self.assertIsInstance(v, AddressBook.NSArray)

        v = AddressBook.ABPickerCopySelectedRecords(ref)
        self.assertIsInstance(v, AddressBook.NSArray)

        v = AddressBook.ABPickerCopySelectedIdentifiers(
            ref, AddressBook.ABGetMe(AddressBook.ABGetSharedAddressBook())
        )
        if v is not None:
            self.assertIsInstance(v, AddressBook.NSArray)

        v = AddressBook.ABPickerCopySelectedValues(ref)
        self.assertIsInstance(v, AddressBook.NSArray)

        grp = AddressBook.ABCopyArrayOfAllGroups(AddressBook.ABGetSharedAddressBook())[
            0
        ]
        usr = AddressBook.ABGetMe(AddressBook.ABGetSharedAddressBook())

        AddressBook.ABPickerSelectGroup(ref, grp, True)
        self.assertArgHasType(AddressBook.ABPickerSelectGroup, 2, objc._C_BOOL)

        AddressBook.ABPickerSelectRecord(ref, usr, False)
        self.assertArgHasType(AddressBook.ABPickerSelectRecord, 2, objc._C_BOOL)

        AddressBook.ABPickerSelectIdentifier(
            ref, usr, "Last", False
        )  # AddressBook.ABRecordCopyUniqueId(usr), False)
        self.assertArgHasType(AddressBook.ABPickerSelectIdentifier, 3, objc._C_BOOL)

        AddressBook.ABPickerDeselectIdentifier(ref, usr, "Last")

        AddressBook.ABPickerDeselectGroup(ref, grp)
        AddressBook.ABPickerDeselectRecord(ref, usr)

        AddressBook.ABPickerDeselectAll(ref)

        AddressBook.ABPickerClearSearchField(ref)

        if 0:
            # These are annoying, don't actually call
            AddressBook.ABPickerEditInAddressBook(ref)
            AddressBook.ABPickerSelectInAddressBook(ref)
        else:
            AddressBook.self.assertResultHasType(
                AddressBook.ABPickerEditInAddressBook, objc._C_VOID
            )
            AddressBook.self.assertResultHasType(
                AddressBook.ABPickerSelectInAddressBook, objc._C_VOID
            )

        r = AddressBook.ABPickerGetDelegate(ref)

        AddressBook.ABPickerSetDelegate
