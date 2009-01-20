
from PyObjCTools.TestSupport import *
from AddressBook import *

_C_ABAddressBookRef = '^{__ABAddressBookRef=}'
_C_ABMultiValueRef = '^{__ABMultiValue=}'
_C_ABPersonRef = '^{__ABPerson=}'
_C_ABGroupRef = '^{__ABGroup=}'
_C_ABSearchElementRef = '^{__ABSearchElementRef=}'
_C_CFStringRef = '^{__CFString=}'
_C_CFStringRefPtr = '^^{__CFString}'
_C_CFDictionaryRef = '^{__CFDictionary=}'
_C_CFArrayRef = '^{__CFArray=}'
_C_CFDataRef = '^{__CFData=}'

class TestABAddressBookC (TestCase):
    def testTypes(self):
        self.failUnless(ABAddressBookRef is ABAddressBook)
        self.failUnless(ABPersonRef is ABPerson)
        self.failUnless(ABSearchElementRef is ABSearchElement)
        self.failUnless(ABGroupRef is ABGroup)

    def testFunctions(self):
        ref = ABGetSharedAddressBook()
        self.failUnlessIsInstance(ref, ABAddressBookRef)

        r = ABSave(ref)
        self.failUnlessResultHasType(ABSave, objc._C_BOOL)
        self.failUnlessIsInstance(r, bool)

        r = ABHasUnsavedChanges(ref)
        self.failUnlessResultHasType(ABHasUnsavedChanges, objc._C_BOOL)
        self.failUnlessIsInstance(r, bool)
        
        r = me = ABGetMe(ref)
        self.failUnlessIsInstance(r, ABPersonRef)

        # There's only one addressbook per user account, therefore
        # testing functions that modify the adressbook isn't safe 
        # because we'd update the AddressBook of the user running
        # the test which is a bad thing.
        # Therefore we only test if the function signature is 
        # correct. That's not ideal, but because mutation functions
        # have a simple interface it should be sufficient.
        self.failUnlessResultHasType(ABSetMe, objc._C_VOID)
        self.failUnlessArgHasType(ABSetMe, 0, _C_ABAddressBookRef)
        self.failUnlessArgHasType(ABSetMe, 1, _C_ABPersonRef)

        name = ABCopyRecordTypeFromUniqueId(ref, ABRecordCopyUniqueId(me))
        self.failUnlessEqual(name, u'ABPerson')

        self.failUnlessResultHasType(ABAddPropertiesAndTypes, objc._C_CFIndex)
        self.failUnlessArgHasType(ABAddPropertiesAndTypes, 0, _C_ABAddressBookRef)
        self.failUnlessArgHasType(ABAddPropertiesAndTypes, 1, _C_CFStringRef)
        self.failUnlessArgHasType(ABAddPropertiesAndTypes, 2, _C_CFDictionaryRef)

        self.failUnlessResultHasType(ABRemoveProperties, objc._C_CFIndex)
        self.failUnlessArgHasType(ABRemoveProperties, 0, _C_ABAddressBookRef)
        self.failUnlessArgHasType(ABRemoveProperties, 1, _C_CFStringRef)
        self.failUnlessArgHasType(ABRemoveProperties, 2, _C_CFArrayRef)

        v = ABCopyArrayOfPropertiesForRecordType(ref, 'ABPerson')
        self.failUnlessResultIsCFRetained(ABCopyArrayOfPropertiesForRecordType)
        self.failUnlessIsInstance(v, CFArrayRef)
        self.failUnless(len(v))
        self.failUnlessIsInstance(v[0], unicode)

        v = ABTypeOfProperty(ref, "ABPersion", v[0])
        self.failUnlessIsInstance(v, (int, long))

        v = ABCopyRecordForUniqueId(ref, ABRecordCopyUniqueId(me)) 
        self.failUnlessResultIsCFRetained(ABCopyRecordForUniqueId)
        self.failUnlessIsInstance(v, ABPersonRef)


        self.failUnlessResultHasType(ABAddRecord, objc._C_BOOL)
        self.failUnlessArgHasType(ABAddRecord, 0, _C_ABAddressBookRef)
        self.failUnlessArgHasType(ABAddRecord, 1, objc._C_ID)

        self.failUnlessResultHasType(ABRemoveRecord, objc._C_BOOL)
        self.failUnlessArgHasType(ABRemoveRecord, 0, _C_ABAddressBookRef)
        self.failUnlessArgHasType(ABRemoveRecord, 1, objc._C_ID)

        v = ABCopyArrayOfAllPeople(ref)
        self.failUnlessResultIsCFRetained(ABCopyArrayOfAllPeople)
        self.failUnlessIsInstance(v, CFArrayRef)

        v = ABCopyArrayOfAllGroups(ref)
        self.failUnlessResultIsCFRetained(ABCopyArrayOfAllGroups)
        self.failUnlessIsInstance(v, CFArrayRef)

        self.failUnlessResultHasType(ABRecordCreateCopy, objc._C_ID)
        self.failUnlessResultIsCFRetained(ABRecordCreateCopy)
        self.failUnlessArgHasType(ABRecordCreateCopy, 0, objc._C_ID)

        v = ABRecordCopyRecordType(me)
        self.failUnlessResultIsCFRetained(ABRecordCopyRecordType)
        self.failUnlessIsInstance(v, unicode)

        self.failUnlessResultHasType(ABRecordCopyValue, objc._C_ID)
        self.failUnlessArgHasType(ABRecordCopyValue, 0, objc._C_ID)
        self.failUnlessArgHasType(ABRecordCopyValue, 1, _C_CFStringRef)

        self.failUnlessResultHasType(ABRecordSetValue, objc._C_BOOL)
        self.failUnlessArgHasType(ABRecordSetValue, 0, objc._C_ID)
        self.failUnlessArgHasType(ABRecordSetValue, 1, _C_CFStringRef)
        self.failUnlessArgHasType(ABRecordSetValue, 2, objc._C_ID)

        self.failUnlessResultHasType(ABRecordRemoveValue, objc._C_BOOL)
        self.failUnlessArgHasType(ABRecordRemoveValue, 0, objc._C_ID)
        self.failUnlessArgHasType(ABRecordRemoveValue, 1, _C_CFStringRef)

        self.failUnlessResultHasType(ABRecordIsReadOnly, objc._C_BOOL)
        self.failUnlessArgHasType(ABRecordIsReadOnly, 0, objc._C_ID)

        self.failUnlessResultHasType(ABRecordCopyUniqueId, _C_CFStringRef)
        self.failUnlessArgHasType(ABRecordCopyUniqueId, 0, objc._C_ID)

        self.failUnlessResultHasType(ABPersonCreate, _C_ABPersonRef)

        self.failUnlessResultHasType(ABPersonCreateWithVCardRepresentation, _C_ABPersonRef)
        self.failUnlessArgHasType(ABPersonCreateWithVCardRepresentation, 0, _C_CFDataRef)

        self.failUnlessResultHasType(ABPersonCopyParentGroups, _C_CFArrayRef)
        self.failUnlessArgHasType(ABPersonCopyParentGroups, 0, _C_ABPersonRef)

        self.failUnlessResultHasType(ABPersonCreateSearchElement, _C_ABSearchElementRef)
        self.failUnlessArgHasType(ABPersonCreateSearchElement, 0, _C_CFStringRef)
        self.failUnlessArgHasType(ABPersonCreateSearchElement, 1, _C_CFStringRef)
        self.failUnlessArgHasType(ABPersonCreateSearchElement, 2, _C_CFStringRef)
        self.failUnlessArgHasType(ABPersonCreateSearchElement, 3, objc._C_ID)
        self.failUnlessArgHasType(ABPersonCreateSearchElement, 4, objc._C_CFIndex)

        self.failUnlessResultHasType(ABGroupCreate, _C_ABGroupRef)

        self.failUnlessResultHasType(ABGroupCopyArrayOfAllMembers, _C_CFArrayRef)
        self.failUnlessArgHasType(ABGroupCopyArrayOfAllMembers, 0, _C_ABGroupRef)

        self.failUnlessResultHasType(ABGroupAddMember, objc._C_BOOL)
        self.failUnlessArgHasType(ABGroupAddMember, 0, _C_ABGroupRef)
        self.failUnlessArgHasType(ABGroupAddMember, 1, _C_ABPersonRef)

        self.failUnlessResultHasType(ABGroupRemoveMember, objc._C_BOOL)
        self.failUnlessArgHasType(ABGroupRemoveMember, 0, _C_ABGroupRef)
        self.failUnlessArgHasType(ABGroupRemoveMember, 1, _C_ABPersonRef)

        self.failUnlessResultHasType(ABGroupCopyArrayOfAllSubgroups, _C_CFArrayRef)
        self.failUnlessArgHasType(ABGroupCopyArrayOfAllSubgroups, 0, _C_ABGroupRef)

        self.failUnlessResultHasType(ABGroupAddGroup, objc._C_BOOL)
        self.failUnlessArgHasType(ABGroupAddGroup, 0, _C_ABGroupRef)
        self.failUnlessArgHasType(ABGroupAddGroup, 1, _C_ABGroupRef)

        self.failUnlessResultHasType(ABGroupRemoveGroup, objc._C_BOOL)
        self.failUnlessArgHasType(ABGroupRemoveGroup, 0, _C_ABGroupRef)
        self.failUnlessArgHasType(ABGroupRemoveGroup, 1, _C_ABGroupRef)

        self.failUnlessResultHasType(ABGroupCopyParentGroups, _C_CFArrayRef)
        self.failUnlessArgHasType(ABGroupCopyParentGroups, 0, _C_ABGroupRef)

        self.failUnlessResultHasType(ABGroupSetDistributionIdentifier, objc._C_BOOL)
        self.failUnlessArgHasType(ABGroupSetDistributionIdentifier, 0, _C_ABGroupRef)
        self.failUnlessArgHasType(ABGroupSetDistributionIdentifier, 1, _C_ABPersonRef)
        self.failUnlessArgHasType(ABGroupSetDistributionIdentifier, 2, _C_CFStringRef)
        self.failUnlessArgHasType(ABGroupSetDistributionIdentifier, 3, _C_CFStringRef)

        self.failUnlessResultHasType(ABGroupCopyDistributionIdentifier, _C_CFStringRef)
        self.failUnlessArgHasType(ABGroupCopyDistributionIdentifier, 0, _C_ABGroupRef)
        self.failUnlessArgHasType(ABGroupCopyDistributionIdentifier, 1, _C_ABPersonRef)
        self.failUnlessArgHasType(ABGroupCopyDistributionIdentifier, 2, _C_CFStringRef)

        self.failUnlessResultHasType(ABGroupCreateSearchElement, _C_ABSearchElementRef)
        self.failUnlessArgHasType(ABGroupCreateSearchElement, 0, _C_CFStringRef)
        self.failUnlessArgHasType(ABGroupCreateSearchElement, 1, _C_CFStringRef)
        self.failUnlessArgHasType(ABGroupCreateSearchElement, 2, _C_CFStringRef)
        self.failUnlessArgHasType(ABGroupCreateSearchElement, 3, objc._C_ID)
        self.failUnlessArgHasType(ABGroupCreateSearchElement, 4, objc._C_CFIndex)

        self.failUnlessResultHasType(ABSearchElementCreateWithConjunction, _C_ABSearchElementRef)
        self.failUnlessArgHasType(ABSearchElementCreateWithConjunction, 0, objc._C_CFIndex)
        self.failUnlessArgHasType(ABSearchElementCreateWithConjunction, 1, _C_CFArrayRef)

        self.failUnlessResultHasType(ABSearchElementMatchesRecord, objc._C_BOOL)
        self.failUnlessArgHasType(ABSearchElementMatchesRecord, 0, _C_ABSearchElementRef)
        self.failUnlessArgHasType(ABSearchElementMatchesRecord, 1, objc._C_ID)

        self.failUnlessResultHasType(ABMultiValueCreate, _C_ABMultiValueRef)

        self.failUnlessResultHasType(ABMultiValueCount, objc._C_CFIndex)
        self.failUnlessArgHasType(ABMultiValueCount, 0, _C_ABMultiValueRef)

        self.failUnlessResultHasType(ABMultiValueCopyValueAtIndex, objc._C_ID)
        self.failUnlessArgHasType(ABMultiValueCopyValueAtIndex, 0, _C_ABMultiValueRef)
        self.failUnlessArgHasType(ABMultiValueCopyValueAtIndex, 1, objc._C_CFIndex)

        self.failUnlessResultHasType(ABMultiValueCopyLabelAtIndex, _C_CFStringRef)
        self.failUnlessArgHasType(ABMultiValueCopyLabelAtIndex, 0, _C_ABMultiValueRef)
        self.failUnlessArgHasType(ABMultiValueCopyLabelAtIndex, 1, objc._C_CFIndex)

        self.failUnlessResultHasType(ABMultiValueCopyPrimaryIdentifier, _C_CFStringRef)
        self.failUnlessArgHasType(ABMultiValueCopyPrimaryIdentifier, 0, _C_ABMultiValueRef)

        self.failUnlessResultHasType(ABMultiValueIndexForIdentifier, objc._C_CFIndex)
        self.failUnlessArgHasType(ABMultiValueIndexForIdentifier, 0, _C_ABMultiValueRef)
        self.failUnlessArgHasType(ABMultiValueIndexForIdentifier, 1, _C_CFStringRef)

        self.failUnlessResultHasType(ABMultiValueCopyIdentifierAtIndex, _C_CFStringRef)
        self.failUnlessArgHasType(ABMultiValueCopyIdentifierAtIndex, 0, _C_ABMultiValueRef)
        self.failUnlessArgHasType(ABMultiValueCopyIdentifierAtIndex, 1, objc._C_CFIndex)

        self.failUnlessResultHasType(ABMultiValuePropertyType, objc._C_CFIndex)
        self.failUnlessArgHasType(ABMultiValuePropertyType, 0, _C_ABMultiValueRef)

        self.failUnlessResultHasType(ABMultiValueCreateCopy, _C_ABMultiValueRef)
        self.failUnlessArgHasType(ABMultiValueCreateCopy, 0, _C_ABMultiValueRef)

        self.failUnlessResultHasType(ABMultiValueCreateMutable, _C_ABMultiValueRef)


        self.failUnlessResultHasType(ABMultiValueAdd, objc._C_BOOL)
        self.failUnlessArgHasType(ABMultiValueAdd, 0, _C_ABMultiValueRef)
        self.failUnlessArgHasType(ABMultiValueAdd, 1, objc._C_ID)
        self.failUnlessArgHasType(ABMultiValueAdd, 2, _C_CFStringRef)
        self.failUnlessArgHasType(ABMultiValueAdd, 3, objc._C_OUT + _C_CFStringRefPtr)

        self.failUnlessResultHasType(ABMultiValueInsert, objc._C_BOOL)
        self.failUnlessArgHasType(ABMultiValueInsert, 0, _C_ABMultiValueRef)
        self.failUnlessArgHasType(ABMultiValueInsert, 1, objc._C_ID)
        self.failUnlessArgHasType(ABMultiValueInsert, 2, _C_CFStringRef)
        self.failUnlessArgHasType(ABMultiValueInsert, 3, objc._C_CFIndex)
        self.failUnlessArgHasType(ABMultiValueInsert, 4, objc._C_OUT + _C_CFStringRefPtr)

        self.failUnlessResultHasType(ABMultiValueRemove, objc._C_BOOL)
        self.failUnlessArgHasType(ABMultiValueRemove, 0, _C_ABMultiValueRef)
        self.failUnlessArgHasType(ABMultiValueRemove, 1, objc._C_CFIndex)

        self.failUnlessResultHasType(ABMultiValueReplaceValue, objc._C_BOOL)
        self.failUnlessArgHasType(ABMultiValueReplaceValue, 0, _C_ABMultiValueRef)
        self.failUnlessArgHasType(ABMultiValueReplaceValue, 1, objc._C_ID)
        self.failUnlessArgHasType(ABMultiValueReplaceValue, 2, objc._C_CFIndex)

        self.failUnlessResultHasType(ABMultiValueReplaceLabel, objc._C_BOOL)
        self.failUnlessArgHasType(ABMultiValueReplaceLabel, 0, _C_ABMultiValueRef)
        self.failUnlessArgHasType(ABMultiValueReplaceLabel, 1, _C_CFStringRef)
        self.failUnlessArgHasType(ABMultiValueReplaceLabel, 2, objc._C_CFIndex)

        self.failUnlessResultHasType(ABMultiValueSetPrimaryIdentifier, objc._C_BOOL)
        self.failUnlessArgHasType(ABMultiValueSetPrimaryIdentifier, 0, _C_ABMultiValueRef)
        self.failUnlessArgHasType(ABMultiValueSetPrimaryIdentifier, 1, _C_CFStringRef)

        self.failUnlessResultHasType(ABMultiValueCreateMutableCopy, _C_ABMultiValueRef)
        self.failUnlessArgHasType(ABMultiValueCreateMutableCopy, 0, _C_ABMultiValueRef)

        self.failUnlessResultHasType(ABCopyLocalizedPropertyOrLabel, _C_CFStringRef)
        self.failUnlessArgHasType(ABCopyLocalizedPropertyOrLabel, 0, _C_CFStringRef)

        self.failUnlessResultHasType(ABCreateFormattedAddressFromDictionary, _C_CFStringRef)
        self.failUnlessArgHasType(ABCreateFormattedAddressFromDictionary, 0, _C_ABAddressBookRef)
        self.failUnlessArgHasType(ABCreateFormattedAddressFromDictionary, 1, _C_CFDictionaryRef)

        self.failUnlessResultHasType(ABCopyDefaultCountryCode, _C_CFStringRef)
        self.failUnlessArgHasType(ABCopyDefaultCountryCode, 0, _C_ABAddressBookRef)

        self.failUnlessResultHasType(ABPersonSetImageData, objc._C_BOOL)
        self.failUnlessArgHasType(ABPersonSetImageData, 0, _C_ABPersonRef)
        self.failUnlessArgHasType(ABPersonSetImageData, 1, _C_CFDataRef)

        self.failUnlessResultHasType(ABPersonCopyImageData, _C_CFDataRef)
        self.failUnlessArgHasType(ABPersonCopyImageData, 0, _C_ABPersonRef)

        r = []

        @objc.callbackFor(ABBeginLoadingImageDataForClient)
        def callback(imageData, tag, refcon):
            print "done"
            r.append((imageData, tag, refcon))

        idx = ABBeginLoadingImageDataForClient(me, callback, 99)
        self.failUnlessIsInstance(idx, (int, long))

        #CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, True)
        ABCancelLoadingImageDataForTag(idx)

if __name__ == "__main__":
    main()
