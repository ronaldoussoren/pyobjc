from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNGroup(TestCase):
    @min_os_level("10.11")
    def testConstants(self):
        self.assertIsInstance(Contacts.CNGroupIdentifierKey, str)
        self.assertIsInstance(Contacts.CNGroupNameKey, str)
