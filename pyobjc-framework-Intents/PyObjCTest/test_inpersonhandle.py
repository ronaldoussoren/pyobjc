from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINPersonHandle(TestCase):
    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INPersonHandleTypeUnknown, 0)
        self.assertEqual(Intents.INPersonHandleTypeEmailAddress, 1)
        self.assertEqual(Intents.INPersonHandleTypePhoneNumber, 2)
