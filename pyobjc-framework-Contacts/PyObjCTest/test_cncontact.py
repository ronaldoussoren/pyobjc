import objc

import Contacts
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCNContact(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Contacts.CNContactSortOrder)
        self.assertIsEnumType(Contacts.CNContactType)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Contacts.CNContactPhoneticOrganizationNameKey, str)
        self.assertIsInstance(Contacts.CNContactImageDataAvailableKey, str)

    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(Contacts.CNContactTypePerson, 0)
        self.assertEqual(Contacts.CNContactTypeOrganization, 1)

        self.assertEqual(Contacts.CNContactSortOrderNone, 0)
        self.assertEqual(Contacts.CNContactSortOrderUserDefault, 1)
        self.assertEqual(Contacts.CNContactSortOrderGivenName, 2)
        self.assertEqual(Contacts.CNContactSortOrderFamilyName, 3)

        self.assertIsInstance(Contacts.CNContactPropertyNotFetchedExceptionName, str)
        self.assertIsInstance(Contacts.CNContactIdentifierKey, str)
        self.assertIsInstance(Contacts.CNContactNamePrefixKey, str)
        self.assertIsInstance(Contacts.CNContactGivenNameKey, str)
        self.assertIsInstance(Contacts.CNContactMiddleNameKey, str)
        self.assertIsInstance(Contacts.CNContactFamilyNameKey, str)
        self.assertIsInstance(Contacts.CNContactPreviousFamilyNameKey, str)
        self.assertIsInstance(Contacts.CNContactNameSuffixKey, str)
        self.assertIsInstance(Contacts.CNContactNicknameKey, str)
        self.assertIsInstance(Contacts.CNContactPhoneticGivenNameKey, str)
        self.assertIsInstance(Contacts.CNContactPhoneticMiddleNameKey, str)
        self.assertIsInstance(Contacts.CNContactPhoneticFamilyNameKey, str)
        self.assertIsInstance(Contacts.CNContactOrganizationNameKey, str)
        self.assertIsInstance(Contacts.CNContactDepartmentNameKey, str)
        self.assertIsInstance(Contacts.CNContactJobTitleKey, str)
        self.assertIsInstance(Contacts.CNContactBirthdayKey, str)
        self.assertIsInstance(Contacts.CNContactNonGregorianBirthdayKey, str)
        self.assertIsInstance(Contacts.CNContactNoteKey, str)
        self.assertIsInstance(Contacts.CNContactImageDataKey, str)
        self.assertIsInstance(Contacts.CNContactThumbnailImageDataKey, str)
        self.assertIsInstance(Contacts.CNContactTypeKey, str)
        self.assertIsInstance(Contacts.CNContactPhoneNumbersKey, str)
        self.assertIsInstance(Contacts.CNContactEmailAddressesKey, str)
        self.assertIsInstance(Contacts.CNContactPostalAddressesKey, str)
        self.assertIsInstance(Contacts.CNContactDatesKey, str)
        self.assertIsInstance(Contacts.CNContactUrlAddressesKey, str)
        self.assertIsInstance(Contacts.CNContactRelationsKey, str)
        self.assertIsInstance(Contacts.CNContactSocialProfilesKey, str)
        self.assertIsInstance(Contacts.CNContactInstantMessageAddressesKey, str)

    @min_os_level("10.11")
    def testProtocols(self):
        objc.protocolNamed("CNKeyDescriptor")

    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(Contacts.CNContact.isKeyAvailable_)
        self.assertResultIsBOOL(Contacts.CNContact.areKeysAvailable_)
        self.assertResultIsBOOL(Contacts.CNContact.isUnifiedWithContactWithIdentifier_)
