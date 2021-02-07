from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNContactVCardSerialization(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertArgIsOut(
            Contacts.CNContactVCardSerialization.dataWithContacts_error_, 1
        )
        self.assertArgIsOut(
            Contacts.CNContactVCardSerialization.contactsWithData_error_, 1
        )
