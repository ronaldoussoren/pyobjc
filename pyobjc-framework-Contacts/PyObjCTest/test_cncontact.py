from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import Contacts

    class TestCNContact (TestCase):
        @min_os_level("10.12")
        def testConstants10_12(self):
            self.assertIsInstance(Contacts.CNContactPhoneticOrganizationNameKey, unicode)
            self.assertIsInstance(Contacts.CNContactImageDataAvailableKey, unicode)

        @min_os_level("10.11")
        def testConstants(self):
            self.assertEqual(Contacts.CNContactTypePerson, 0)
            self.assertEqual(Contacts.CNContactTypeOrganization, 1)

            self.assertEqual(Contacts.CNContactSortOrderNone, 0)
            self.assertEqual(Contacts.CNContactSortOrderUserDefault, 1)
            self.assertEqual(Contacts.CNContactSortOrderGivenName, 2)
            self.assertEqual(Contacts.CNContactSortOrderFamilyName, 3)

            self.assertIsInstance(Contacts.CNContactPropertyNotFetchedExceptionName, unicode)
            self.assertIsInstance(Contacts.CNContactIdentifierKey, unicode)
            self.assertIsInstance(Contacts.CNContactNamePrefixKey, unicode)
            self.assertIsInstance(Contacts.CNContactGivenNameKey, unicode)
            self.assertIsInstance(Contacts.CNContactMiddleNameKey, unicode)
            self.assertIsInstance(Contacts.CNContactFamilyNameKey, unicode)
            self.assertIsInstance(Contacts.CNContactPreviousFamilyNameKey, unicode)
            self.assertIsInstance(Contacts.CNContactNameSuffixKey, unicode)
            self.assertIsInstance(Contacts.CNContactNicknameKey, unicode)
            self.assertIsInstance(Contacts.CNContactPhoneticGivenNameKey, unicode)
            self.assertIsInstance(Contacts.CNContactPhoneticMiddleNameKey, unicode)
            self.assertIsInstance(Contacts.CNContactPhoneticFamilyNameKey, unicode)
            self.assertIsInstance(Contacts.CNContactOrganizationNameKey, unicode)
            self.assertIsInstance(Contacts.CNContactDepartmentNameKey, unicode)
            self.assertIsInstance(Contacts.CNContactJobTitleKey, unicode)
            self.assertIsInstance(Contacts.CNContactBirthdayKey, unicode)
            self.assertIsInstance(Contacts.CNContactNonGregorianBirthdayKey, unicode)
            self.assertIsInstance(Contacts.CNContactNoteKey, unicode)
            self.assertIsInstance(Contacts.CNContactImageDataKey, unicode)
            self.assertIsInstance(Contacts.CNContactThumbnailImageDataKey, unicode)
            self.assertIsInstance(Contacts.CNContactTypeKey, unicode)
            self.assertIsInstance(Contacts.CNContactPhoneNumbersKey, unicode)
            self.assertIsInstance(Contacts.CNContactEmailAddressesKey, unicode)
            self.assertIsInstance(Contacts.CNContactPostalAddressesKey, unicode)
            self.assertIsInstance(Contacts.CNContactDatesKey, unicode)
            self.assertIsInstance(Contacts.CNContactUrlAddressesKey, unicode)
            self.assertIsInstance(Contacts.CNContactRelationsKey, unicode)
            self.assertIsInstance(Contacts.CNContactSocialProfilesKey, unicode)
            self.assertIsInstance(Contacts.CNContactInstantMessageAddressesKey, unicode)

        @min_os_level('10.11')
        def testProtocols(self):
            objc.protocolNamed('CNKeyDescriptor')

        @min_os_level('10.11')
        def testMethods(self):
            self.assertResultIsBOOL(Contacts.CNContact.isKeyAvailable_)
            self.assertResultIsBOOL(Contacts.CNContact.areKeysAvailable_)
            self.assertResultIsBOOL(Contacts.CNContact.isUnifiedWithContactWithIdentifier_)

if __name__ == "__main__":
    main()
