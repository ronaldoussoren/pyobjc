from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNPostalAddressFormatter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Contacts.CNPostalAddressFormatterStyle)

    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(Contacts.CNPostalAddressFormatterStyleMailingAddress, 0)
        self.assertIsInstance(Contacts.CNPostalAddressPropertyAttribute, str)
        self.assertIsInstance(
            Contacts.CNPostalAddressLocalizedPropertyNameAttribute, str
        )
