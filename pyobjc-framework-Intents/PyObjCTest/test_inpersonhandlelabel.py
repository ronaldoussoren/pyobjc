from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINPersonHandleLabel(TestCase):
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
