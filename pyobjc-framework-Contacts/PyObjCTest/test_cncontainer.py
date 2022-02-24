from PyObjCTools.TestSupport import TestCase, min_os_level
import Contacts


class TestCNContainer(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Contacts.CNContainerType)

    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(Contacts.CNContainerTypeUnassigned, 0)
        self.assertEqual(Contacts.CNContainerTypeLocal, 1)
        self.assertEqual(Contacts.CNContainerTypeExchange, 2)
        self.assertEqual(Contacts.CNContainerTypeCardDAV, 3)

        self.assertIsInstance(Contacts.CNContainerIdentifierKey, str)
        self.assertIsInstance(Contacts.CNContainerNameKey, str)
        self.assertIsInstance(Contacts.CNContainerTypeKey, str)
