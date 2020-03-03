import AddressBook
import objc
from PyObjCTools.TestSupport import TestCase

_C_ABAddressBookRef = b"^{__ABAddressBookRef=}"
_C_ABMultiValueRef = b"^{__ABMultiValue=}"
_C_ABPersonRef = b"^{__ABPerson=}"
_C_ABGroupRef = b"^{__ABGroup=}"
_C_ABSearchElementRef = b"^{__ABSearchElementRef=}"
_C_CFStringRef = b"^{__CFString=}"
_C_CFStringRefPtr = b"^^{__CFString}"
_C_CFDictionaryRef = b"^{__CFDictionary=}"
_C_CFArrayRef = b"^{__CFArray=}"
_C_CFDataRef = b"^{__CFData=}"


class TestABAddressBookC(TestCase):
    def testTypes(self):
        self.assertTrue(AddressBook.ABAddressBookRef is AddressBook.ABAddressBook)
        self.assertTrue(AddressBook.ABPersonRef is AddressBook.ABPerson)
        self.assertTrue(AddressBook.ABSearchElementRef is AddressBook.ABSearchElement)
        self.assertTrue(AddressBook.ABGroupRef is AddressBook.ABGroup)

    def testFunctions(self):
        ref = AddressBook.ABGetSharedAddressBook()
        self.assertIsInstance(ref, AddressBook.ABAddressBookRef)

        r = AddressBook.ABSave(ref)
        self.assertResultHasType(AddressBook.ABSave, objc._C_BOOL)
        self.assertIsInstance(r, bool)

        r = AddressBook.ABHasUnsavedChanges(ref)
        self.assertResultHasType(AddressBook.ABHasUnsavedChanges, objc._C_BOOL)
        self.assertIsInstance(r, bool)

        r = me = AddressBook.ABGetMe(ref)
        self.assertIsInstance(r, AddressBook.ABPersonRef)

        # There's only one addressbook per user account, therefore
        # testing functions that modify the adressbook isn't safe
        # because we'd update the AddressBook of the user running
        # the test which is a bad thing.
        # Therefore we only test if the function signature is
        # correct. That's not ideal, but because mutation functions
        # have a simple interface it should be sufficient.
        self.assertResultHasType(AddressBook.ABSetMe, objc._C_VOID)
        self.assertArgHasType(AddressBook.ABSetMe, 0, _C_ABAddressBookRef)
        self.assertArgHasType(AddressBook.ABSetMe, 1, _C_ABPersonRef)

        name = AddressBook.ABCopyRecordTypeFromUniqueId(
            ref, AddressBook.ABRecordCopyUniqueId(me)
        )
        self.assertEqual(name, "ABPerson")

        self.assertResultHasType(AddressBook.ABAddPropertiesAndTypes, objc._C_CFIndex)
        self.assertArgHasType(
            AddressBook.ABAddPropertiesAndTypes, 0, _C_ABAddressBookRef
        )
        self.assertArgHasType(AddressBook.ABAddPropertiesAndTypes, 1, _C_CFStringRef)
        self.assertArgHasType(
            AddressBook.ABAddPropertiesAndTypes, 2, _C_CFDictionaryRef
        )

        self.assertResultHasType(AddressBook.ABRemoveProperties, objc._C_CFIndex)
        self.assertArgHasType(AddressBook.ABRemoveProperties, 0, _C_ABAddressBookRef)
        self.assertArgHasType(AddressBook.ABRemoveProperties, 1, _C_CFStringRef)
        self.assertArgHasType(AddressBook.ABRemoveProperties, 2, _C_CFArrayRef)

        v = AddressBook.ABCopyArrayOfPropertiesForRecordType(ref, "ABPerson")
        self.assertResultIsCFRetained(AddressBook.ABCopyArrayOfPropertiesForRecordType)
        self.assertIsInstance(v, AddressBook.NSArray)
        self.assertTrue(len(v))
        self.assertIsInstance(v[0], str)

        v = AddressBook.ABTypeOfProperty(ref, "ABPersion", v[0])
        self.assertIsInstance(v, int)

        v = AddressBook.ABCopyRecordForUniqueId(
            ref, AddressBook.ABRecordCopyUniqueId(me)
        )
        self.assertResultIsCFRetained(AddressBook.ABCopyRecordForUniqueId)
        self.assertIsInstance(v, AddressBook.ABPersonRef)

        self.assertResultHasType(AddressBook.ABAddRecord, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABAddRecord, 0, _C_ABAddressBookRef)
        self.assertArgHasType(AddressBook.ABAddRecord, 1, objc._C_ID)

        self.assertResultHasType(AddressBook.ABRemoveRecord, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABRemoveRecord, 0, _C_ABAddressBookRef)
        self.assertArgHasType(AddressBook.ABRemoveRecord, 1, objc._C_ID)

        v = AddressBook.ABCopyArrayOfAllPeople(ref)
        self.assertResultIsCFRetained(AddressBook.ABCopyArrayOfAllPeople)
        self.assertIsInstance(v, AddressBook.NSArray)

        v = AddressBook.ABCopyArrayOfAllGroups(ref)
        self.assertResultIsCFRetained(AddressBook.ABCopyArrayOfAllGroups)
        self.assertIsInstance(v, AddressBook.NSArray)

        self.assertResultHasType(AddressBook.ABRecordCreateCopy, objc._C_ID)
        self.assertResultIsCFRetained(AddressBook.ABRecordCreateCopy)
        self.assertArgHasType(AddressBook.ABRecordCreateCopy, 0, objc._C_ID)

        v = AddressBook.ABRecordCopyRecordType(me)
        self.assertResultIsCFRetained(AddressBook.ABRecordCopyRecordType)
        self.assertIsInstance(v, str)

        self.assertResultHasType(AddressBook.ABRecordCopyValue, objc._C_ID)
        self.assertArgHasType(AddressBook.ABRecordCopyValue, 0, objc._C_ID)
        self.assertArgHasType(AddressBook.ABRecordCopyValue, 1, _C_CFStringRef)

        self.assertResultHasType(AddressBook.ABRecordSetValue, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABRecordSetValue, 0, objc._C_ID)
        self.assertArgHasType(AddressBook.ABRecordSetValue, 1, _C_CFStringRef)
        self.assertArgHasType(AddressBook.ABRecordSetValue, 2, objc._C_ID)

        self.assertResultHasType(AddressBook.ABRecordRemoveValue, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABRecordRemoveValue, 0, objc._C_ID)
        self.assertArgHasType(AddressBook.ABRecordRemoveValue, 1, _C_CFStringRef)

        self.assertResultHasType(AddressBook.ABRecordIsReadOnly, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABRecordIsReadOnly, 0, objc._C_ID)

        self.assertResultHasType(AddressBook.ABRecordCopyUniqueId, _C_CFStringRef)
        self.assertArgHasType(AddressBook.ABRecordCopyUniqueId, 0, objc._C_ID)

        self.assertResultHasType(AddressBook.ABPersonCreate, _C_ABPersonRef)

        self.assertResultHasType(
            AddressBook.ABPersonCreateWithVCardRepresentation, _C_ABPersonRef
        )
        self.assertArgHasType(
            AddressBook.ABPersonCreateWithVCardRepresentation, 0, _C_CFDataRef
        )

        self.assertResultHasType(AddressBook.ABPersonCopyParentGroups, _C_CFArrayRef)
        self.assertArgHasType(AddressBook.ABPersonCopyParentGroups, 0, _C_ABPersonRef)

        self.assertResultHasType(
            AddressBook.ABPersonCreateSearchElement, _C_ABSearchElementRef
        )
        self.assertArgHasType(
            AddressBook.ABPersonCreateSearchElement, 0, _C_CFStringRef
        )
        self.assertArgHasType(
            AddressBook.ABPersonCreateSearchElement, 1, _C_CFStringRef
        )
        self.assertArgHasType(
            AddressBook.ABPersonCreateSearchElement, 2, _C_CFStringRef
        )
        self.assertArgHasType(AddressBook.ABPersonCreateSearchElement, 3, objc._C_ID)
        self.assertArgHasType(
            AddressBook.ABPersonCreateSearchElement, 4, objc._C_CFIndex
        )

        self.assertResultHasType(AddressBook.ABGroupCreate, _C_ABGroupRef)

        self.assertResultHasType(
            AddressBook.ABGroupCopyArrayOfAllMembers, _C_CFArrayRef
        )
        self.assertArgHasType(
            AddressBook.ABGroupCopyArrayOfAllMembers, 0, _C_ABGroupRef
        )

        self.assertResultHasType(AddressBook.ABGroupAddMember, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABGroupAddMember, 0, _C_ABGroupRef)
        self.assertArgHasType(AddressBook.ABGroupAddMember, 1, _C_ABPersonRef)

        self.assertResultHasType(AddressBook.ABGroupRemoveMember, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABGroupRemoveMember, 0, _C_ABGroupRef)
        self.assertArgHasType(AddressBook.ABGroupRemoveMember, 1, _C_ABPersonRef)

        self.assertResultHasType(
            AddressBook.ABGroupCopyArrayOfAllSubgroups, _C_CFArrayRef
        )
        self.assertArgHasType(
            AddressBook.ABGroupCopyArrayOfAllSubgroups, 0, _C_ABGroupRef
        )

        self.assertResultHasType(AddressBook.ABGroupAddGroup, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABGroupAddGroup, 0, _C_ABGroupRef)
        self.assertArgHasType(AddressBook.ABGroupAddGroup, 1, _C_ABGroupRef)

        self.assertResultHasType(AddressBook.ABGroupRemoveGroup, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABGroupRemoveGroup, 0, _C_ABGroupRef)
        self.assertArgHasType(AddressBook.ABGroupRemoveGroup, 1, _C_ABGroupRef)

        self.assertResultHasType(AddressBook.ABGroupCopyParentGroups, _C_CFArrayRef)
        self.assertArgHasType(AddressBook.ABGroupCopyParentGroups, 0, _C_ABGroupRef)

        self.assertResultHasType(
            AddressBook.ABGroupSetDistributionIdentifier, objc._C_BOOL
        )
        self.assertArgHasType(
            AddressBook.ABGroupSetDistributionIdentifier, 0, _C_ABGroupRef
        )
        self.assertArgHasType(
            AddressBook.ABGroupSetDistributionIdentifier, 1, _C_ABPersonRef
        )
        self.assertArgHasType(
            AddressBook.ABGroupSetDistributionIdentifier, 2, _C_CFStringRef
        )
        self.assertArgHasType(
            AddressBook.ABGroupSetDistributionIdentifier, 3, _C_CFStringRef
        )

        self.assertResultHasType(
            AddressBook.ABGroupCopyDistributionIdentifier, _C_CFStringRef
        )
        self.assertArgHasType(
            AddressBook.ABGroupCopyDistributionIdentifier, 0, _C_ABGroupRef
        )
        self.assertArgHasType(
            AddressBook.ABGroupCopyDistributionIdentifier, 1, _C_ABPersonRef
        )
        self.assertArgHasType(
            AddressBook.ABGroupCopyDistributionIdentifier, 2, _C_CFStringRef
        )

        self.assertResultHasType(
            AddressBook.ABGroupCreateSearchElement, _C_ABSearchElementRef
        )
        self.assertArgHasType(AddressBook.ABGroupCreateSearchElement, 0, _C_CFStringRef)
        self.assertArgHasType(AddressBook.ABGroupCreateSearchElement, 1, _C_CFStringRef)
        self.assertArgHasType(AddressBook.ABGroupCreateSearchElement, 2, _C_CFStringRef)
        self.assertArgHasType(AddressBook.ABGroupCreateSearchElement, 3, objc._C_ID)
        self.assertArgHasType(
            AddressBook.ABGroupCreateSearchElement, 4, objc._C_CFIndex
        )

        self.assertResultHasType(
            AddressBook.ABSearchElementCreateWithConjunction, _C_ABSearchElementRef
        )
        self.assertArgHasType(
            AddressBook.ABSearchElementCreateWithConjunction, 0, objc._C_CFIndex
        )
        self.assertArgHasType(
            AddressBook.ABSearchElementCreateWithConjunction, 1, _C_CFArrayRef
        )

        self.assertResultHasType(AddressBook.ABSearchElementMatchesRecord, objc._C_BOOL)
        self.assertArgHasType(
            AddressBook.ABSearchElementMatchesRecord, 0, _C_ABSearchElementRef
        )
        self.assertArgHasType(AddressBook.ABSearchElementMatchesRecord, 1, objc._C_ID)

        self.assertResultHasType(AddressBook.ABMultiValueCreate, _C_ABMultiValueRef)

        self.assertResultHasType(AddressBook.ABMultiValueCount, objc._C_CFIndex)
        self.assertArgHasType(AddressBook.ABMultiValueCount, 0, _C_ABMultiValueRef)

        self.assertResultHasType(AddressBook.ABMultiValueCopyValueAtIndex, objc._C_ID)
        self.assertArgHasType(
            AddressBook.ABMultiValueCopyValueAtIndex, 0, _C_ABMultiValueRef
        )
        self.assertArgHasType(
            AddressBook.ABMultiValueCopyValueAtIndex, 1, objc._C_CFIndex
        )

        self.assertResultHasType(
            AddressBook.ABMultiValueCopyLabelAtIndex, _C_CFStringRef
        )
        self.assertArgHasType(
            AddressBook.ABMultiValueCopyLabelAtIndex, 0, _C_ABMultiValueRef
        )
        self.assertArgHasType(
            AddressBook.ABMultiValueCopyLabelAtIndex, 1, objc._C_CFIndex
        )

        self.assertResultHasType(
            AddressBook.ABMultiValueCopyPrimaryIdentifier, _C_CFStringRef
        )
        self.assertArgHasType(
            AddressBook.ABMultiValueCopyPrimaryIdentifier, 0, _C_ABMultiValueRef
        )

        self.assertResultHasType(
            AddressBook.ABMultiValueIndexForIdentifier, objc._C_CFIndex
        )
        self.assertArgHasType(
            AddressBook.ABMultiValueIndexForIdentifier, 0, _C_ABMultiValueRef
        )
        self.assertArgHasType(
            AddressBook.ABMultiValueIndexForIdentifier, 1, _C_CFStringRef
        )

        self.assertResultHasType(
            AddressBook.ABMultiValueCopyIdentifierAtIndex, _C_CFStringRef
        )
        self.assertArgHasType(
            AddressBook.ABMultiValueCopyIdentifierAtIndex, 0, _C_ABMultiValueRef
        )
        self.assertArgHasType(
            AddressBook.ABMultiValueCopyIdentifierAtIndex, 1, objc._C_CFIndex
        )

        self.assertResultHasType(AddressBook.ABMultiValuePropertyType, objc._C_CFIndex)
        self.assertArgHasType(
            AddressBook.ABMultiValuePropertyType, 0, _C_ABMultiValueRef
        )

        self.assertResultHasType(AddressBook.ABMultiValueCreateCopy, _C_ABMultiValueRef)
        self.assertArgHasType(AddressBook.ABMultiValueCreateCopy, 0, _C_ABMultiValueRef)

        self.assertResultHasType(
            AddressBook.ABMultiValueCreateMutable, _C_ABMultiValueRef
        )

        self.assertResultHasType(AddressBook.ABMultiValueAdd, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABMultiValueAdd, 0, _C_ABMultiValueRef)
        self.assertArgHasType(AddressBook.ABMultiValueAdd, 1, objc._C_ID)
        self.assertArgHasType(AddressBook.ABMultiValueAdd, 2, _C_CFStringRef)
        self.assertArgHasType(
            AddressBook.ABMultiValueAdd, 3, objc._C_OUT + _C_CFStringRefPtr
        )

        self.assertResultHasType(AddressBook.ABMultiValueInsert, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABMultiValueInsert, 0, _C_ABMultiValueRef)
        self.assertArgHasType(AddressBook.ABMultiValueInsert, 1, objc._C_ID)
        self.assertArgHasType(AddressBook.ABMultiValueInsert, 2, _C_CFStringRef)
        self.assertArgHasType(AddressBook.ABMultiValueInsert, 3, objc._C_CFIndex)
        self.assertArgHasType(
            AddressBook.ABMultiValueInsert, 4, objc._C_OUT + _C_CFStringRefPtr
        )

        self.assertResultHasType(AddressBook.ABMultiValueRemove, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABMultiValueRemove, 0, _C_ABMultiValueRef)
        self.assertArgHasType(AddressBook.ABMultiValueRemove, 1, objc._C_CFIndex)

        self.assertResultHasType(AddressBook.ABMultiValueReplaceValue, objc._C_BOOL)
        self.assertArgHasType(
            AddressBook.ABMultiValueReplaceValue, 0, _C_ABMultiValueRef
        )
        self.assertArgHasType(AddressBook.ABMultiValueReplaceValue, 1, objc._C_ID)
        self.assertArgHasType(AddressBook.ABMultiValueReplaceValue, 2, objc._C_CFIndex)

        self.assertResultHasType(AddressBook.ABMultiValueReplaceLabel, objc._C_BOOL)
        self.assertArgHasType(
            AddressBook.ABMultiValueReplaceLabel, 0, _C_ABMultiValueRef
        )
        self.assertArgHasType(AddressBook.ABMultiValueReplaceLabel, 1, _C_CFStringRef)
        self.assertArgHasType(AddressBook.ABMultiValueReplaceLabel, 2, objc._C_CFIndex)

        self.assertResultHasType(
            AddressBook.ABMultiValueSetPrimaryIdentifier, objc._C_BOOL
        )
        self.assertArgHasType(
            AddressBook.ABMultiValueSetPrimaryIdentifier, 0, _C_ABMultiValueRef
        )
        self.assertArgHasType(
            AddressBook.ABMultiValueSetPrimaryIdentifier, 1, _C_CFStringRef
        )

        self.assertResultHasType(
            AddressBook.ABMultiValueCreateMutableCopy, _C_ABMultiValueRef
        )
        self.assertArgHasType(
            AddressBook.ABMultiValueCreateMutableCopy, 0, _C_ABMultiValueRef
        )

        self.assertResultHasType(
            AddressBook.ABCopyLocalizedPropertyOrLabel, _C_CFStringRef
        )
        self.assertArgHasType(
            AddressBook.ABCopyLocalizedPropertyOrLabel, 0, _C_CFStringRef
        )

        self.assertResultHasType(
            AddressBook.ABCreateFormattedAddressFromDictionary, _C_CFStringRef
        )
        self.assertArgHasType(
            AddressBook.ABCreateFormattedAddressFromDictionary, 0, _C_ABAddressBookRef
        )
        self.assertArgHasType(
            AddressBook.ABCreateFormattedAddressFromDictionary, 1, _C_CFDictionaryRef
        )

        self.assertResultHasType(AddressBook.ABCopyDefaultCountryCode, _C_CFStringRef)
        self.assertArgHasType(
            AddressBook.ABCopyDefaultCountryCode, 0, _C_ABAddressBookRef
        )

        self.assertResultHasType(AddressBook.ABPersonSetImageData, objc._C_BOOL)
        self.assertArgHasType(AddressBook.ABPersonSetImageData, 0, _C_ABPersonRef)
        self.assertArgHasType(AddressBook.ABPersonSetImageData, 1, _C_CFDataRef)

        self.assertResultHasType(AddressBook.ABPersonCopyImageData, _C_CFDataRef)
        self.assertArgHasType(AddressBook.ABPersonCopyImageData, 0, _C_ABPersonRef)

        r = []

        @objc.callbackFor(AddressBook.ABBeginLoadingImageDataForClient)
        def callback(imageData, tag, refcon):
            r.append((imageData, tag, refcon))

        idx = AddressBook.ABBeginLoadingImageDataForClient(me, callback, 99)
        self.assertIsInstance(idx, int)

        # AddressBook.CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, True)
        AddressBook.ABCancelLoadingImageDataForTag(idx)
