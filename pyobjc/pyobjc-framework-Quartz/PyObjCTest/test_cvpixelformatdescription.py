
from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVPixelFormatDescription (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCVPixelFormatName, unicode)
        self.assertIsInstance(kCVPixelFormatConstant, unicode)
        self.assertIsInstance(kCVPixelFormatCodecType, unicode)
        self.assertIsInstance(kCVPixelFormatFourCC, unicode)
        self.assertIsInstance(kCVPixelFormatPlanes, unicode)

        self.assertIsInstance(kCVPixelFormatBlockWidth, unicode)
        self.assertIsInstance(kCVPixelFormatBlockHeight, unicode)
        self.assertIsInstance(kCVPixelFormatBitsPerBlock, unicode)
        self.assertIsInstance(kCVPixelFormatBlockHorizontalAlignment, unicode)
        self.assertIsInstance(kCVPixelFormatBlockVerticalAlignment, unicode)
        self.assertIsInstance(kCVPixelFormatHorizontalSubsampling, unicode)
        self.assertIsInstance(kCVPixelFormatVerticalSubsampling, unicode)
        self.assertIsInstance(kCVPixelFormatOpenGLFormat, unicode)
        self.assertIsInstance(kCVPixelFormatOpenGLType, unicode)
        self.assertIsInstance(kCVPixelFormatOpenGLInternalFormat, unicode)
        self.assertIsInstance(kCVPixelFormatCGBitmapInfo, unicode)
        self.assertIsInstance(kCVPixelFormatQDCompatibility, unicode)
        self.assertIsInstance(kCVPixelFormatCGBitmapContextCompatibility, unicode)
        self.assertIsInstance(kCVPixelFormatCGImageCompatibility, unicode)
        self.assertIsInstance(kCVPixelFormatOpenGLCompatibility, unicode)
        self.assertIsInstance(kCVPixelFormatFillExtendedPixelsCallback, unicode)


    def testFunctions(self):
        self.assertResultIsCFRetained(CVPixelFormatDescriptionCreateWithPixelFormatType)
        v = CVPixelFormatDescriptionCreateWithPixelFormatType(None, kCVPixelFormatType_32ARGB)
        self.assertIsInstance(v, CFDictionaryRef)

        self.assertResultIsCFRetained(CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes)
        v = CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(None)
        self.assertIsInstance(v, CFArrayRef)
        self.assertNotEqual(len(v), 0)
        self.assertIsInstance(v[0], (int, long))

        tp = 42
        while tp in v:
            tp += 1

        CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType({}, tp)


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCVPixelFormatBlackBlock, unicode)



if __name__ == "__main__":
    main()
