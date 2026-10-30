from PyObjCTools.TestSupport import TestCase
import Intents


class TestINPersonHandle(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INPersonHandleType)
        self.assertEqual(Intents.INPersonHandleTypeUnknown, 0)
        self.assertEqual(Intents.INPersonHandleTypeEmailAddress, 1)
        self.assertEqual(Intents.INPersonHandleTypePhoneNumber, 2)
