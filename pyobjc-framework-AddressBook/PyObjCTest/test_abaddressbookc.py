
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

_C_ABAddressBookRef = b'^{__ABAddressBookRef=}'
_C_ABMultiValueRef = b'^{__ABMultiValue=}'
_C_ABPersonRef = b'^{__ABPerson=}'
_C_ABGroupRef = b'^{__ABGroup=}'
_C_ABSearchElementRef = b'^{__ABSearchElementRef=}'
_C_CFStringRef = b'^{__CFString=}'
_C_CFStringRefPtr = b'^^{__CFString}'
_C_CFDictionaryRef = b'^{__CFDictionary=}'
_C_CFArrayRef = b'^{__CFArray=}'
_C_CFDataRef = b'^{__CFData=}'

class TestABAddressBookC (TestCase):
    def testTypes(self):
        self.assertTrue(ABAddressBookRef is ABAddressBook)
        self.assertTrue(ABPersonRef is ABPerson)
        self.assertTrue(ABSearchElementRef is ABSearchElement)
        self.assertTrue(ABGroupRef is ABGroup)

    def testFunctions(self):
        ref = ABGetSharedAddressBook()
        self.assertIsInstance(ref, ABAddressBookRef)

        r = ABSave(ref)
        self.assertResultHasType(ABSave, objc._C_BOOL)
        self.assertIsInstance(r, bool)

        r = ABHasUnsavedChanges(ref)
        self.assertResultHasType(ABHasUnsavedChanges, objc._C_BOOL)
        self.assertIsInstance(r, bool)

        r = me = ABGetMe(ref)
        self.assertIsInstance(r, ABPersonRef)

        # There's only one addressbook per user account, therefore
        # testing functions that modify the adressbook isn't safe
        # because we'd update the AddressBook of the user running
        # the test which is a bad thing.
        # Therefore we only test if the function signature is
        # correct. That's not ideal, but because mutation functions
        # have a simple interface it should be sufficient.
        self.assertResultHasType(ABSetMe, objc._C_VOID)
        self.assertArgHasType(ABSetMe, 0, _C_ABAddressBookRef)
        self.assertArgHasType(ABSetMe, 1, _C_ABPersonRef)

        name = ABCopyRecordTypeFromUniqueId(ref, ABRecordCopyUniqueId(me))
        self.assertEqual(name, 'ABPerson')

        self.assertResultHasType(ABAddPropertiesAndTypes, objc._C_CFIndex)
        self.assertArgHasType(ABAddPropertiesAndTypes, 0, _C_ABAddressBookRef)
        self.assertArgHasType(ABAddPropertiesAndTypes, 1, _C_CFStringRef)
        self.assertArgHasType(ABAddPropertiesAndTypes, 2, _C_CFDictionaryRef)

        self.assertResultHasType(ABRemoveProperties, objc._C_CFIndex)
        self.assertArgHasType(ABRemoveProperties, 0, _C_ABAddressBookRef)
        self.assertArgHasType(ABRemoveProperties, 1, _C_CFStringRef)
        self.assertArgHasType(ABRemoveProperties, 2, _C_CFArrayRef)

        v = ABCopyArrayOfPropertiesForRecordType(ref, 'ABPerson')
        self.assertResultIsCFRetained(ABCopyArrayOfPropertiesForRecordType)
        self.assertIsInstance(v, NSArray)
        self.assertTrue(len(v))
        self.assertIsInstance(v[0], unicode)

        v = ABTypeOfProperty(ref, "ABPersion", v[0])
        self.assertIsInstance(v, (int, long))

        v = ABCopyRecordForUniqueId(ref, ABRecordCopyUniqueId(me))
        self.assertResultIsCFRetained(ABCopyRecordForUniqueId)
        self.assertIsInstance(v, ABPersonRef)


        self.assertResultHasType(ABAddRecord, objc._C_BOOL)
        self.assertArgHasType(ABAddRecord, 0, _C_ABAddressBookRef)
        self.assertArgHasType(ABAddRecord, 1, objc._C_ID)

        self.assertResultHasType(ABRemoveRecord, objc._C_BOOL)
        self.assertArgHasType(ABRemoveRecord, 0, _C_ABAddressBookRef)
        self.assertArgHasType(ABRemoveRecord, 1, objc._C_ID)

        v = ABCopyArrayOfAllPeople(ref)
        self.assertResultIsCFRetained(ABCopyArrayOfAllPeople)
        self.assertIsInstance(v, NSArray)

        v = ABCopyArrayOfAllGroups(ref)
        self.assertResultIsCFRetained(ABCopyArrayOfAllGroups)
        self.assertIsInstance(v, NSArray)

        self.assertResultHasType(ABRecordCreateCopy, objc._C_ID)
        self.assertResultIsCFRetained(ABRecordCreateCopy)
        self.assertArgHasType(ABRecordCreateCopy, 0, objc._C_ID)

        v = ABRecordCopyRecordType(me)
        self.assertResultIsCFRetained(ABRecordCopyRecordType)
        self.assertIsInstance(v, unicode)

        self.assertResultHasType(ABRecordCopyValue, objc._C_ID)
        self.assertArgHasType(ABRecordCopyValue, 0, objc._C_ID)
        self.assertArgHasType(ABRecordCopyValue, 1, _C_CFStringRef)

        self.assertResultHasType(ABRecordSetValue, objc._C_BOOL)
        self.assertArgHasType(ABRecordSetValue, 0, objc._C_ID)
        self.assertArgHasType(ABRecordSetValue, 1, _C_CFStringRef)
        self.assertArgHasType(ABRecordSetValue, 2, objc._C_ID)

        self.assertResultHasType(ABRecordRemoveValue, objc._C_BOOL)
        self.assertArgHasType(ABRecordRemoveValue, 0, objc._C_ID)
        self.assertArgHasType(ABRecordRemoveValue, 1, _C_CFStringRef)

        self.assertResultHasType(ABRecordIsReadOnly, objc._C_BOOL)
        self.assertArgHasType(ABRecordIsReadOnly, 0, objc._C_ID)

        self.assertResultHasType(ABRecordCopyUniqueId, _C_CFStringRef)
        self.assertArgHasType(ABRecordCopyUniqueId, 0, objc._C_ID)

        self.assertResultHasType(ABPersonCreate, _C_ABPersonRef)

        self.assertResultHasType(ABPersonCreateWithVCardRepresentation, _C_ABPersonRef)
        self.assertArgHasType(ABPersonCreateWithVCardRepresentation, 0, _C_CFDataRef)

        self.assertResultHasType(ABPersonCopyParentGroups, _C_CFArrayRef)
        self.assertArgHasType(ABPersonCopyParentGroups, 0, _C_ABPersonRef)

        self.assertResultHasType(ABPersonCreateSearchElement, _C_ABSearchElementRef)
        self.assertArgHasType(ABPersonCreateSearchElement, 0, _C_CFStringRef)
        self.assertArgHasType(ABPersonCreateSearchElement, 1, _C_CFStringRef)
        self.assertArgHasType(ABPersonCreateSearchElement, 2, _C_CFStringRef)
        self.assertArgHasType(ABPersonCreateSearchElement, 3, objc._C_ID)
        self.assertArgHasType(ABPersonCreateSearchElement, 4, objc._C_CFIndex)

        self.assertResultHasType(ABGroupCreate, _C_ABGroupRef)

        self.assertResultHasType(ABGroupCopyArrayOfAllMembers, _C_CFArrayRef)
        self.assertArgHasType(ABGroupCopyArrayOfAllMembers, 0, _C_ABGroupRef)

        self.assertResultHasType(ABGroupAddMember, objc._C_BOOL)
        self.assertArgHasType(ABGroupAddMember, 0, _C_ABGroupRef)
        self.assertArgHasType(ABGroupAddMember, 1, _C_ABPersonRef)

        self.assertResultHasType(ABGroupRemoveMember, objc._C_BOOL)
        self.assertArgHasType(ABGroupRemoveMember, 0, _C_ABGroupRef)
        self.assertArgHasType(ABGroupRemoveMember, 1, _C_ABPersonRef)

        self.assertResultHasType(ABGroupCopyArrayOfAllSubgroups, _C_CFArrayRef)
        self.assertArgHasType(ABGroupCopyArrayOfAllSubgroups, 0, _C_ABGroupRef)

        self.assertResultHasType(ABGroupAddGroup, objc._C_BOOL)
        self.assertArgHasType(ABGroupAddGroup, 0, _C_ABGroupRef)
        self.assertArgHasType(ABGroupAddGroup, 1, _C_ABGroupRef)

        self.assertResultHasType(ABGroupRemoveGroup, objc._C_BOOL)
        self.assertArgHasType(ABGroupRemoveGroup, 0, _C_ABGroupRef)
        self.assertArgHasType(ABGroupRemoveGroup, 1, _C_ABGroupRef)

        self.assertResultHasType(ABGroupCopyParentGroups, _C_CFArrayRef)
        self.assertArgHasType(ABGroupCopyParentGroups, 0, _C_ABGroupRef)

        self.assertResultHasType(ABGroupSetDistributionIdentifier, objc._C_BOOL)
        self.assertArgHasType(ABGroupSetDistributionIdentifier, 0, _C_ABGroupRef)
        self.assertArgHasType(ABGroupSetDistributionIdentifier, 1, _C_ABPersonRef)
        self.assertArgHasType(ABGroupSetDistributionIdentifier, 2, _C_CFStringRef)
        self.assertArgHasType(ABGroupSetDistributionIdentifier, 3, _C_CFStringRef)

        self.assertResultHasType(ABGroupCopyDistributionIdentifier, _C_CFStringRef)
        self.assertArgHasType(ABGroupCopyDistributionIdentifier, 0, _C_ABGroupRef)
        self.assertArgHasType(ABGroupCopyDistributionIdentifier, 1, _C_ABPersonRef)
        self.assertArgHasType(ABGroupCopyDistributionIdentifier, 2, _C_CFStringRef)

        self.assertResultHasType(ABGroupCreateSearchElement, _C_ABSearchElementRef)
        self.assertArgHasType(ABGroupCreateSearchElement, 0, _C_CFStringRef)
        self.assertArgHasType(ABGroupCreateSearchElement, 1, _C_CFStringRef)
        self.assertArgHasType(ABGroupCreateSearchElement, 2, _C_CFStringRef)
        self.assertArgHasType(ABGroupCreateSearchElement, 3, objc._C_ID)
        self.assertArgHasType(ABGroupCreateSearchElement, 4, objc._C_CFIndex)

        self.assertResultHasType(ABSearchElementCreateWithConjunction, _C_ABSearchElementRef)
        self.assertArgHasType(ABSearchElementCreateWithConjunction, 0, objc._C_CFIndex)
        self.assertArgHasType(ABSearchElementCreateWithConjunction, 1, _C_CFArrayRef)

        self.assertResultHasType(ABSearchElementMatchesRecord, objc._C_BOOL)
        self.assertArgHasType(ABSearchElementMatchesRecord, 0, _C_ABSearchElementRef)
        self.assertArgHasType(ABSearchElementMatchesRecord, 1, objc._C_ID)

        self.assertResultHasType(ABMultiValueCreate, _C_ABMultiValueRef)

        self.assertResultHasType(ABMultiValueCount, objc._C_CFIndex)
        self.assertArgHasType(ABMultiValueCount, 0, _C_ABMultiValueRef)

        self.assertResultHasType(ABMultiValueCopyValueAtIndex, objc._C_ID)
        self.assertArgHasType(ABMultiValueCopyValueAtIndex, 0, _C_ABMultiValueRef)
        self.assertArgHasType(ABMultiValueCopyValueAtIndex, 1, objc._C_CFIndex)

        self.assertResultHasType(ABMultiValueCopyLabelAtIndex, _C_CFStringRef)
        self.assertArgHasType(ABMultiValueCopyLabelAtIndex, 0, _C_ABMultiValueRef)
        self.assertArgHasType(ABMultiValueCopyLabelAtIndex, 1, objc._C_CFIndex)

        self.assertResultHasType(ABMultiValueCopyPrimaryIdentifier, _C_CFStringRef)
        self.assertArgHasType(ABMultiValueCopyPrimaryIdentifier, 0, _C_ABMultiValueRef)

        self.assertResultHasType(ABMultiValueIndexForIdentifier, objc._C_CFIndex)
        self.assertArgHasType(ABMultiValueIndexForIdentifier, 0, _C_ABMultiValueRef)
        self.assertArgHasType(ABMultiValueIndexForIdentifier, 1, _C_CFStringRef)

        self.assertResultHasType(ABMultiValueCopyIdentifierAtIndex, _C_CFStringRef)
        self.assertArgHasType(ABMultiValueCopyIdentifierAtIndex, 0, _C_ABMultiValueRef)
        self.assertArgHasType(ABMultiValueCopyIdentifierAtIndex, 1, objc._C_CFIndex)

        self.assertResultHasType(ABMultiValuePropertyType, objc._C_CFIndex)
        self.assertArgHasType(ABMultiValuePropertyType, 0, _C_ABMultiValueRef)

        self.assertResultHasType(ABMultiValueCreateCopy, _C_ABMultiValueRef)
        self.assertArgHasType(ABMultiValueCreateCopy, 0, _C_ABMultiValueRef)

        self.assertResultHasType(ABMultiValueCreateMutable, _C_ABMultiValueRef)


        self.assertResultHasType(ABMultiValueAdd, objc._C_BOOL)
        self.assertArgHasType(ABMultiValueAdd, 0, _C_ABMultiValueRef)
        self.assertArgHasType(ABMultiValueAdd, 1, objc._C_ID)
        self.assertArgHasType(ABMultiValueAdd, 2, _C_CFStringRef)
        self.assertArgHasType(ABMultiValueAdd, 3, objc._C_OUT + _C_CFStringRefPtr)

        self.assertResultHasType(ABMultiValueInsert, objc._C_BOOL)
        self.assertArgHasType(ABMultiValueInsert, 0, _C_ABMultiValueRef)
        self.assertArgHasType(ABMultiValueInsert, 1, objc._C_ID)
        self.assertArgHasType(ABMultiValueInsert, 2, _C_CFStringRef)
        self.assertArgHasType(ABMultiValueInsert, 3, objc._C_CFIndex)
        self.assertArgHasType(ABMultiValueInsert, 4, objc._C_OUT + _C_CFStringRefPtr)

        self.assertResultHasType(ABMultiValueRemove, objc._C_BOOL)
        self.assertArgHasType(ABMultiValueRemove, 0, _C_ABMultiValueRef)
        self.assertArgHasType(ABMultiValueRemove, 1, objc._C_CFIndex)

        self.assertResultHasType(ABMultiValueReplaceValue, objc._C_BOOL)
        self.assertArgHasType(ABMultiValueReplaceValue, 0, _C_ABMultiValueRef)
        self.assertArgHasType(ABMultiValueReplaceValue, 1, objc._C_ID)
        self.assertArgHasType(ABMultiValueReplaceValue, 2, objc._C_CFIndex)

        self.assertResultHasType(ABMultiValueReplaceLabel, objc._C_BOOL)
        self.assertArgHasType(ABMultiValueReplaceLabel, 0, _C_ABMultiValueRef)
        self.assertArgHasType(ABMultiValueReplaceLabel, 1, _C_CFStringRef)
        self.assertArgHasType(ABMultiValueReplaceLabel, 2, objc._C_CFIndex)

        self.assertResultHasType(ABMultiValueSetPrimaryIdentifier, objc._C_BOOL)
        self.assertArgHasType(ABMultiValueSetPrimaryIdentifier, 0, _C_ABMultiValueRef)
        self.assertArgHasType(ABMultiValueSetPrimaryIdentifier, 1, _C_CFStringRef)

        self.assertResultHasType(ABMultiValueCreateMutableCopy, _C_ABMultiValueRef)
        self.assertArgHasType(ABMultiValueCreateMutableCopy, 0, _C_ABMultiValueRef)

        self.assertResultHasType(ABCopyLocalizedPropertyOrLabel, _C_CFStringRef)
        self.assertArgHasType(ABCopyLocalizedPropertyOrLabel, 0, _C_CFStringRef)

        self.assertResultHasType(ABCreateFormattedAddressFromDictionary, _C_CFStringRef)
        self.assertArgHasType(ABCreateFormattedAddressFromDictionary, 0, _C_ABAddressBookRef)
        self.assertArgHasType(ABCreateFormattedAddressFromDictionary, 1, _C_CFDictionaryRef)

        self.assertResultHasType(ABCopyDefaultCountryCode, _C_CFStringRef)
        self.assertArgHasType(ABCopyDefaultCountryCode, 0, _C_ABAddressBookRef)

        self.assertResultHasType(ABPersonSetImageData, objc._C_BOOL)
        self.assertArgHasType(ABPersonSetImageData, 0, _C_ABPersonRef)
        self.assertArgHasType(ABPersonSetImageData, 1, _C_CFDataRef)

        self.assertResultHasType(ABPersonCopyImageData, _C_CFDataRef)
        self.assertArgHasType(ABPersonCopyImageData, 0, _C_ABPersonRef)

        r = []

        @objc.callbackFor(ABBeginLoadingImageDataForClient)
        def callback(imageData, tag, refcon):
            r.append((imageData, tag, refcon))

        idx = ABBeginLoadingImageDataForClient(me, callback, 99)
        self.assertIsInstance(idx, (int, long))

        #CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, True)
        ABCancelLoadingImageDataForTag(idx)

if __name__ == "__main__":
    main()
