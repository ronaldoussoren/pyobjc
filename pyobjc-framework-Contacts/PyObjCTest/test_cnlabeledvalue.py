from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2**32:
    import Contacts

    class TestCNLabeledValue (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertIsInstance(Contacts.CNLabelHome, unicode)
            self.assertIsInstance(Contacts.CNLabelWork, unicode)
            self.assertIsInstance(Contacts.CNLabelOther, unicode)
            self.assertIsInstance(Contacts.CNLabelEmailiCloud, unicode)
            self.assertIsInstance(Contacts.CNLabelURLAddressHomePage, unicode)
            self.assertIsInstance(Contacts.CNLabelDateAnniversary, unicode)

if __name__ == "__main__":
    main()
