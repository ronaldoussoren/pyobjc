from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNLabeledValue(TestCase):
    @min_os_level("10.11")
    def test_constants(self):
        self.assertIsInstance(Contacts.CNLabelHome, str)
        self.assertIsInstance(Contacts.CNLabelWork, str)
        self.assertIsInstance(Contacts.CNLabelOther, str)
        self.assertIsInstance(Contacts.CNLabelEmailiCloud, str)
        self.assertIsInstance(Contacts.CNLabelURLAddressHomePage, str)
        self.assertIsInstance(Contacts.CNLabelDateAnniversary, str)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(Contacts.CNLabelSchool, str)
