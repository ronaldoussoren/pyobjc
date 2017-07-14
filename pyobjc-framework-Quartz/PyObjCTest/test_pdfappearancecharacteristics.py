from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAppearanceCharacteristic (TestCase):
    @min_os_level('10.13')
    def testConstants(self):
        self.assertIsInstance(PDFAppearanceCharacteristicsKeyBackgroundColor, unicode)
        self.assertIsInstance(PDFAppearanceCharacteristicsKeyBorderColor, unicode)
        self.assertIsInstance(PDFAppearanceCharacteristicsKeyRotation, unicode)
        self.assertIsInstance(PDFAppearanceCharacteristicsKeyCaption, unicode)
        self.assertIsInstance(PDFAppearanceCharacteristicsKeyRolloverCaption, unicode)
        self.assertIsInstance(PDFAppearanceCharacteristicsKeyDownCaption, unicode)


if __name__ == "__main__":
    main()
