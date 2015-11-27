from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import Contacts

    class TestCNPhoneNumber (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertIsInstance(Contacts.CNLabelPhoneNumberiPhone, unicode)
            self.assertIsInstance(Contacts.CNLabelPhoneNumberMobile, unicode)
            self.assertIsInstance(Contacts.CNLabelPhoneNumberMain, unicode)
            self.assertIsInstance(Contacts.CNLabelPhoneNumberHomeFax, unicode)
            self.assertIsInstance(Contacts.CNLabelPhoneNumberWorkFax, unicode)
            self.assertIsInstance(Contacts.CNLabelPhoneNumberOtherFax, unicode)
            self.assertIsInstance(Contacts.CNLabelPhoneNumberPager, unicode)

if __name__ == "__main__":
    main()
