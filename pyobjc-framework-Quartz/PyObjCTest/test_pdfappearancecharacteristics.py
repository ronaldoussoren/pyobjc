from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFAppearanceCharacteristic(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Quartz.PDFAppearanceCharacteristicsKey, str)

    @min_os_level("10.13")
    def testConstants(self):
        self.assertIsInstance(
            Quartz.PDFAppearanceCharacteristicsKeyBackgroundColor, str
        )
        self.assertIsInstance(Quartz.PDFAppearanceCharacteristicsKeyBorderColor, str)
        self.assertIsInstance(Quartz.PDFAppearanceCharacteristicsKeyRotation, str)
        self.assertIsInstance(Quartz.PDFAppearanceCharacteristicsKeyCaption, str)
        self.assertIsInstance(
            Quartz.PDFAppearanceCharacteristicsKeyRolloverCaption, str
        )
        self.assertIsInstance(Quartz.PDFAppearanceCharacteristicsKeyDownCaption, str)
