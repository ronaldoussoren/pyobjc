from PyObjCTools.TestSupport import TestCase
import QTKit


class TestQTFormatDescription(TestCase):
    def testConstants(self):
        self.assertIsInstance(
            QTKit.QTFormatDescriptionAudioStreamBasicDescriptionAttribute, str
        )
        self.assertIsInstance(QTKit.QTFormatDescriptionAudioMagicCookieAttribute, str)
        self.assertIsInstance(QTKit.QTFormatDescriptionAudioChannelLayoutAttribute, str)
        self.assertIsInstance(
            QTKit.QTFormatDescriptionVideoCleanApertureDisplaySizeAttribute, str
        )
        self.assertIsInstance(
            QTKit.QTFormatDescriptionVideoProductionApertureDisplaySizeAttribute, str
        )
        self.assertIsInstance(
            QTKit.QTFormatDescriptionVideoEncodedPixelsSizeAttribute, str
        )

    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTFormatDescription.isEqualToFormatDescription_)
