
from PyObjCTools.TestSupport import *
from AddressBook import *

try:
    long
except NameError:
    long = int

try:
    unicode
except NameError:
    unicode = str

class TestABPeoplePickerC (TestCase):
    def testConstants(self):
        self.assertEqual(kABPickerSingleValueSelection, 1 << 0)
        self.assertEqual(kABPickerMultipleValueSelection, 1 << 1)
        self.assertEqual(kABPickerAllowGroupSelection, 1 << 2)
        self.assertEqual(kABPickerAllowMultipleSelection, 1 << 3)
        self.assertEqual(kEventClassABPeoplePicker, fourcc(b'abpp'))
        self.assertEqual(kEventParamABPickerRef,  fourcc(b'abpp'))
        self.assertEqual(kEventABPeoplePickerGroupSelectionChanged, 1)
        self.assertEqual(kEventABPeoplePickerNameSelectionChanged, 2)
        self.assertEqual(kEventABPeoplePickerValueSelectionChanged, 3)
        self.assertEqual(kEventABPeoplePickerDisplayedPropertyChanged, 4)
        self.assertEqual(kEventABPeoplePickerGroupDoubleClicked, 5)
        self.assertEqual(kEventABPeoplePickerNameDoubleClicked, 6)


    def testType(self):
        self.assertIsInstance(ABPickerRef, objc.objc_class)

    def testFunctions(self):
        self.assertResultIsCFRetained(ABPickerCreate)
        ref = ABPickerCreate()
        try:
            self.assertIsInstance(ref, (ABPickerRef, objc.lookUpClass('ABPeoplePickerCAdapter')))

        except objc.error:
            self.assertIsInstance(ref, ABPickerRef)

        ABPickerSetFrame(ref, ((90, 100), (200, 400)))
        r = ABPickerGetFrame(ref, None)
        self.assertIsInstance(r, NSRect)
        self.assertEqual(r, ((90, 100), (200, 400)))

        self.assertResultHasType(ABPickerIsVisible, objc._C_BOOL)
        r = ABPickerIsVisible(ref)
        self.assertIsInstance(r, bool)
        self.assertTrue(r is False)

        self.assertArgHasType(ABPickerSetVisibility, 1, objc._C_BOOL)
        ABPickerSetVisibility(ref, True)

        r = ABPickerIsVisible(ref)
        self.assertTrue(r is True)

        ABPickerSetVisibility(ref, False)

        r = ABPickerIsVisible(ref)
        self.assertTrue(r is False)

        r = ABPickerGetAttributes(ref)
        self.assertIsInstance(r, (int, long))

        r = ABPickerChangeAttributes(ref, kABPickerAllowMultipleSelection, 0)
        self.assertTrue(r is None)

        ABPickerAddProperty(ref, kABFirstNameProperty)
        ABPickerAddProperty(ref, kABLastNameProperty)
        ABPickerRemoveProperty(ref, kABFirstNameProperty)

        v = ABPickerCopyProperties(ref)
        self.assertIsInstance(v, NSArray)

        # Disable detailed testing, the RemoveProperties function
        # doesn't actually remove. See radar #7999195.
        #self.assertEqual(tuple(v), (kABLastNameProperty,))

        ABPickerSetColumnTitle(ref, "Achternaam", kABLastNameProperty)
        v = ABPickerCopyColumnTitle(ref, kABLastNameProperty)
        self.assertResultIsCFRetained(ABPickerCopyColumnTitle)
        self.assertEqual(v, "Achternaam")

        ABPickerSetDisplayedProperty(ref, kABLastNameProperty)
        v = ABPickerCopyDisplayedProperty(ref)
        self.assertResultIsCFRetained(ABPickerCopyDisplayedProperty)
        self.assertIsInstance(v, unicode)

        v = ABPickerCopySelectedGroups(ref)
        self.assertIsInstance(v, NSArray)

        v = ABPickerCopySelectedRecords(ref)
        self.assertIsInstance(v, NSArray)

        v = ABPickerCopySelectedIdentifiers(ref, ABGetMe(ABGetSharedAddressBook()))
        if v is not None:
            self.assertIsInstance(v, NSArray)

        v = ABPickerCopySelectedValues(ref)
        self.assertIsInstance(v, NSArray)

        grp = ABCopyArrayOfAllGroups(ABGetSharedAddressBook())[0]
        usr = ABGetMe(ABGetSharedAddressBook())

        ABPickerSelectGroup(ref, grp, True)
        self.assertArgHasType(ABPickerSelectGroup, 2, objc._C_BOOL)

        ABPickerSelectRecord(ref, usr, False)
        self.assertArgHasType(ABPickerSelectRecord, 2, objc._C_BOOL)

        ABPickerSelectIdentifier(ref, usr, "Last", False) #ABRecordCopyUniqueId(usr), False)
        self.assertArgHasType(ABPickerSelectIdentifier, 3, objc._C_BOOL)

        ABPickerDeselectIdentifier(ref, usr, "Last")

        ABPickerDeselectGroup(ref, grp)
        ABPickerDeselectRecord(ref, usr)

        ABPickerDeselectAll(ref)

        ABPickerClearSearchField(ref)

        if 0:
            # These are annoying, don't actually call
            ABPickerEditInAddressBook(ref)
            ABPickerSelectInAddressBook(ref)
        else:
            self.assertResultHasType(ABPickerEditInAddressBook, objc._C_VOID)
            self.assertResultHasType(ABPickerSelectInAddressBook, objc._C_VOID)

        r = ABPickerGetDelegate(ref)

        ABPickerSetDelegate












if __name__ == "__main__":
    main()
