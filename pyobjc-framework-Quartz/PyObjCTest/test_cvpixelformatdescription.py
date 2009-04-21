
from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *

class TestCVPixelFormatDescription (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kCVPixelFormatName, unicode)
        self.failUnlessIsInstance(kCVPixelFormatConstant, unicode)
        self.failUnlessIsInstance(kCVPixelFormatCodecType, unicode)
        self.failUnlessIsInstance(kCVPixelFormatFourCC, unicode)
        self.failUnlessIsInstance(kCVPixelFormatPlanes, unicode)

        self.failUnlessIsInstance(kCVPixelFormatBlockWidth, unicode)
        self.failUnlessIsInstance(kCVPixelFormatBlockHeight, unicode)
        self.failUnlessIsInstance(kCVPixelFormatBitsPerBlock, unicode)
        self.failUnlessIsInstance(kCVPixelFormatBlockHorizontalAlignment, unicode)
        self.failUnlessIsInstance(kCVPixelFormatBlockVerticalAlignment, unicode)
        self.failUnlessIsInstance(kCVPixelFormatHorizontalSubsampling, unicode)
        self.failUnlessIsInstance(kCVPixelFormatVerticalSubsampling, unicode)
        self.failUnlessIsInstance(kCVPixelFormatOpenGLFormat, unicode)
        self.failUnlessIsInstance(kCVPixelFormatOpenGLType, unicode)
        self.failUnlessIsInstance(kCVPixelFormatOpenGLInternalFormat, unicode)
        self.failUnlessIsInstance(kCVPixelFormatCGBitmapInfo, unicode)
        self.failUnlessIsInstance(kCVPixelFormatQDCompatibility, unicode)
        self.failUnlessIsInstance(kCVPixelFormatCGBitmapContextCompatibility, unicode)
        self.failUnlessIsInstance(kCVPixelFormatCGImageCompatibility, unicode)
        self.failUnlessIsInstance(kCVPixelFormatOpenGLCompatibility, unicode)
        self.failUnlessIsInstance(kCVPixelFormatFillExtendedPixelsCallback, unicode)


    def testFunctions(self):
        self.failUnlessResultIsCFRetained(CVPixelFormatDescriptionCreateWithPixelFormatType)
        v = CVPixelFormatDescriptionCreateWithPixelFormatType(None, kCVPixelFormatType_32ARGB)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        self.failUnlessResultIsCFRetained(CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes)
        v = CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(None)
        self.failUnlessIsInstance(v, CFArrayRef)
        self.failIfEqual(len(v), 0)
        self.failUnlessIsInstance(v[0], (int, long))

        tp = 42
        while tp in v:
            tp += 1

        CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType({}, tp)






if __name__ == "__main__":
    main()
