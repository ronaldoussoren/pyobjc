from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNPostalAddress(TestCase):
    @min_os_level("10.11")
    def testConstants(self):
        self.assertIsInstance(Contacts.CNPostalAddressStreetKey, str)
        self.assertIsInstance(Contacts.CNPostalAddressCityKey, str)
        self.assertIsInstance(Contacts.CNPostalAddressStateKey, str)
        self.assertIsInstance(Contacts.CNPostalAddressPostalCodeKey, str)
        self.assertIsInstance(Contacts.CNPostalAddressCountryKey, str)
        self.assertIsInstance(Contacts.CNPostalAddressISOCountryCodeKey, str)

        self.assertIsInstance(Contacts.CNPostalAddressSubAdministrativeAreaKey, str)

    @min_os_level("10.12.4")
    def testConstants10_12_4(self):
        self.assertIsInstance(Contacts.CNPostalAddressSubLocalityKey, str)
