
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABPeoplePickerC (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kABPickerSingleValueSelection, 1 << 0)
        self.failUnlessEqual(kABPickerMultipleValueSelection, 1 << 1)
        self.failUnlessEqual(kABPickerAllowGroupSelection, 1 << 2)
        self.failUnlessEqual(kABPickerAllowMultipleSelection, 1 << 3)
        self.failUnlessEqual(kEventClassABPeoplePicker, fourcc('abpp'))
        self.failUnlessEqual(kEventParamABPickerRef,  fourcc('abpp'))
        self.failUnlessEqual(kEventABPeoplePickerGroupSelectionChanged, 1)
        self.failUnlessEqual(kEventABPeoplePickerNameSelectionChanged, 2)
        self.failUnlessEqual(kEventABPeoplePickerValueSelectionChanged, 3)
        self.failUnlessEqual(kEventABPeoplePickerDisplayedPropertyChanged, 4)
        self.failUnlessEqual(kEventABPeoplePickerGroupDoubleClicked, 5)
        self.failUnlessEqual(kEventABPeoplePickerNameDoubleClicked, 6)


    def testType(self):
        self.failUnlessIsInstance(ABPickerRef, objc.objc_class)

    def testFunctions(self):
        self.failUnlessResultIsCFRetained(ABPickerCreate)
        ref = ABPickerCreate()
        self.failUnlessIsInstance(ref, ABPickerRef)

        ABPickerSetFrame(ref, ((90, 100), (200, 400)))
        r = ABPickerGetFrame(ref, None)
        self.failUnlessIsInstance(r, tuple)
        self.failUnlessEqual(r, ((90, 100), (200, 400)))

        self.failUnlessResultHasType(ABPickerIsVisible, objc._C_BOOL)
        r = ABPickerIsVisible(ref)
        self.failUnlessIsInstance(r, bool)
        self.failUnless(r is False)

        self.failUnlessArgHasType(ABPickerSetVisibility, 1, objc._C_BOOL)
        ABPickerSetVisibility(ref, True)

        r = ABPickerIsVisible(ref)
        self.failUnless(r is True)

        ABPickerSetVisibility(ref, False)

        r = ABPickerIsVisible(ref)
        self.failUnless(r is False)

        r = ABPickerGetAttributes(ref)
        self.failUnlessIsInstance(r, (int, long))

        r = ABPickerChangeAttributes(ref, kABPickerAllowMultipleSelection, 0)
        self.failUnless(r is None)

        ABPickerAddProperty(ref, kABFirstNameProperty)
        ABPickerAddProperty(ref, kABLastNameProperty)
        ABPickerRemoveProperty(ref, kABFirstNameProperty)

        v = ABPickerCopyProperties(ref)
        self.failUnlessIsInstance(v, CFArrayRef)
        self.failUnlessEqual(tuple(v), (kABLastNameProperty,))

        ABPickerSetColumnTitle(ref, u"Achternaam", kABLastNameProperty)
        v = ABPickerCopyColumnTitle(ref, kABLastNameProperty)
        self.failUnlessResultIsCFRetained(ABPickerCopyColumnTitle)
        self.failUnlessEqual(v, u"Achternaam")

        ABPickerSetDisplayedProperty(ref, kABLastNameProperty)
        v = ABPickerCopyDisplayedProperty(ref)
        self.failUnlessResultIsCFRetained(ABPickerCopyDisplayedProperty)
        self.failUnlessIsInstance(v, unicode)

        v = ABPickerCopySelectedGroups(ref)
        self.failUnlessIsInstance(v, CFArrayRef)

        v = ABPickerCopySelectedRecords(ref)
        self.failUnlessIsInstance(v, CFArrayRef)

        v = ABPickerCopySelectedIdentifiers(ref, ABGetMe(ABGetSharedAddressBook()))
        if v is not None:
            self.failUnlessIsInstance(v, CFArrayRef)

        v = ABPickerCopySelectedValues(ref)
        self.failUnlessIsInstance(v, CFArrayRef)

        grp = ABCopyArrayOfAllGroups(ABGetSharedAddressBook())[0]
        usr = ABGetMe(ABGetSharedAddressBook())

        ABPickerSelectGroup(ref, grp, True)
        self.failUnlessArgHasType(ABPickerSelectGroup, 2, objc._C_BOOL)

        ABPickerSelectRecord(ref, usr, False)
        self.failUnlessArgHasType(ABPickerSelectRecord, 2, objc._C_BOOL)

        ABPickerSelectIdentifier(ref, usr, "Last", False) #ABRecordCopyUniqueId(usr), False)
        self.failUnlessArgHasType(ABPickerSelectIdentifier, 3, objc._C_BOOL)

        ABPickerDeselectIdentifier(ref, usr, u"Last")

        ABPickerDeselectGroup(ref, grp)
        ABPickerDeselectRecord(ref, usr)

        ABPickerDeselectAll(ref)

        ABPickerClearSearchField(ref)

        if 0:
            # These are annoying, don't actually call
            ABPickerEditInAddressBook(ref)
            ABPickerSelectInAddressBook(ref)
        else:
            self.failUnlessResultHasType(ABPickerEditInAddressBook, objc._C_VOID)
            self.failUnlessResultHasType(ABPickerSelectInAddressBook, objc._C_VOID)

        r = ABPickerGetDelegate(ref)

        ABPickerSetDelegate









        


if __name__ == "__main__":
    main()
