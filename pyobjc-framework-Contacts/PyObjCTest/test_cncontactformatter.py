from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import Contacts

    class TestCNContactFormatter (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertEqual(Contacts.CNContactFormatterStyleFullName, 0)
            self.assertEqual(Contacts.CNContactFormatterStylePhoneticFullName, 1)

            self.assertEqual(Contacts.CNContactDisplayNameOrderUserDefault, 0)
            self.assertEqual(Contacts.CNContactDisplayNameOrderGivenNameFirst, 1)
            self.assertEqual(Contacts.CNContactDisplayNameOrderFamilyNameFirst, 2)

            self.assertIsInstance(Contacts.CNContactPropertyAttribute, unicode)

if __name__ == "__main__":
    main()
