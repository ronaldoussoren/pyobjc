from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNPostalAddressFormatter(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Contacts.CNPostalAddressFormatterStyle)
        self.assertEqual(Contacts.CNPostalAddressFormatterStyleMailingAddress, 0)

    @min_os_level("10.11")
    def test_constants(self):
        self.assertIsInstance(Contacts.CNPostalAddressPropertyAttribute, str)
        self.assertIsInstance(
            Contacts.CNPostalAddressLocalizedPropertyNameAttribute, str
        )
