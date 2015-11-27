from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import Contacts

    class TestCNPostalAddressFormatter (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertEqual(Contacts.CNPostalAddressFormatterStyleMailingAddress, 0)
            self.assertIsInstance(Contacts.CNPostalAddressPropertyAttribute, unicode)
            self.assertIsInstance(Contacts.CNPostalAddressLocalizedPropertyNameAttribute, unicode)

if __name__ == "__main__":
    main()
