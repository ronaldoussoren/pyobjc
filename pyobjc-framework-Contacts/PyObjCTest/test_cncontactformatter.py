from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNContactFormatter(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Contacts.CNContactDisplayNameOrder)
        self.assertEqual(Contacts.CNContactDisplayNameOrderUserDefault, 0)
        self.assertEqual(Contacts.CNContactDisplayNameOrderGivenNameFirst, 1)
        self.assertEqual(Contacts.CNContactDisplayNameOrderFamilyNameFirst, 2)

        self.assertIsEnumType(Contacts.CNContactFormatterStyle)
        self.assertEqual(Contacts.CNContactFormatterStyleFullName, 0)
        self.assertEqual(Contacts.CNContactFormatterStylePhoneticFullName, 1)

    @min_os_level("10.11")
    def test_constants(self):
        self.assertIsInstance(Contacts.CNContactPropertyAttribute, str)
