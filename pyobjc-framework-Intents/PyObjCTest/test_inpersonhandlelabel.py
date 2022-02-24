from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINPersonHandleLabel(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Intents.INPersonHandleLabel, str)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertIsInstance(Intents.INPersonHandleLabelHome, str)
        self.assertIsInstance(Intents.INPersonHandleLabelWork, str)
        self.assertIsInstance(Intents.INPersonHandleLabeliPhone, str)
        self.assertIsInstance(Intents.INPersonHandleLabelMobile, str)
        self.assertIsInstance(Intents.INPersonHandleLabelMain, str)
        self.assertIsInstance(Intents.INPersonHandleLabelHomeFax, str)
        self.assertIsInstance(Intents.INPersonHandleLabelWorkFax, str)
        self.assertIsInstance(Intents.INPersonHandleLabelPager, str)
        self.assertIsInstance(Intents.INPersonHandleLabelOther, str)

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(Intents.INPersonHandleLabelSchool, str)
