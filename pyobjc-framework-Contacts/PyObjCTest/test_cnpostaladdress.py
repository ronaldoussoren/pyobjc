from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import Contacts

    class TestCNPostalAddress (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertIsInstance(Contacts.CNPostalAddressStreetKey, unicode)
            self.assertIsInstance(Contacts.CNPostalAddressCityKey, unicode)
            self.assertIsInstance(Contacts.CNPostalAddressStateKey, unicode)
            self.assertIsInstance(Contacts.CNPostalAddressPostalCodeKey, unicode)
            self.assertIsInstance(Contacts.CNPostalAddressCountryKey, unicode)
            self.assertIsInstance(Contacts.CNPostalAddressISOCountryCodeKey, unicode)

            self.assertIsInstance(Contacts.CNPostalAddressSubLocalityKey, unicode)
            self.assertIsInstance(Contacts.CNPostalAddressSubAdministrativeAreaKey, unicode)

if __name__ == "__main__":
    main()
