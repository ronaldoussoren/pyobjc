
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTFormatDescription (TestCase):
    def testConstants(self):
        self.assertIsInstance(QTFormatDescriptionAudioStreamBasicDescriptionAttribute, unicode)
        self.assertIsInstance(QTFormatDescriptionAudioMagicCookieAttribute, unicode)
        self.assertIsInstance(QTFormatDescriptionAudioChannelLayoutAttribute, unicode)
        self.assertIsInstance(QTFormatDescriptionVideoCleanApertureDisplaySizeAttribute, unicode)
        self.assertIsInstance(QTFormatDescriptionVideoProductionApertureDisplaySizeAttribute, unicode)
        self.assertIsInstance(QTFormatDescriptionVideoEncodedPixelsSizeAttribute, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(QTFormatDescription.isEqualToFormatDescription_)


if __name__ == "__main__":
    main()
