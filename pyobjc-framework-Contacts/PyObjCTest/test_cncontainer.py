from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNContainer(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Contacts.CNContainerType)
        self.assertEqual(Contacts.CNContainerTypeUnassigned, 0)
        self.assertEqual(Contacts.CNContainerTypeLocal, 1)
        self.assertEqual(Contacts.CNContainerTypeExchange, 2)
        self.assertEqual(Contacts.CNContainerTypeCardDAV, 3)

    @min_os_level("10.11")
    def test_constants(self):

        self.assertIsInstance(Contacts.CNContainerIdentifierKey, str)
        self.assertIsInstance(Contacts.CNContainerNameKey, str)
        self.assertIsInstance(Contacts.CNContainerTypeKey, str)
