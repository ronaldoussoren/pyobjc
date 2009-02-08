
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTFormatDescription (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(QTFormatDescriptionAudioStreamBasicDescriptionAttribute, unicode)
        self.failUnlessIsInstance(QTFormatDescriptionAudioMagicCookieAttribute, unicode)
        self.failUnlessIsInstance(QTFormatDescriptionAudioChannelLayoutAttribute, unicode)
        self.failUnlessIsInstance(QTFormatDescriptionVideoCleanApertureDisplaySizeAttribute, unicode)
        self.failUnlessIsInstance(QTFormatDescriptionVideoProductionApertureDisplaySizeAttribute, unicode)
        self.failUnlessIsInstance(QTFormatDescriptionVideoEncodedPixelsSizeAttribute, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(QTFormatDescription.isEqualToFormatDescription_)


if __name__ == "__main__":
    main()
