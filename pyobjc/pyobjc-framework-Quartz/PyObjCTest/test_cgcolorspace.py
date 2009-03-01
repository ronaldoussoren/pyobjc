
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
import array

class TestCGColorSpace (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCGRenderingIntentDefault, 0)
        self.failUnlessEqual(kCGRenderingIntentAbsoluteColorimetric, 1)
        self.failUnlessEqual(kCGRenderingIntentRelativeColorimetric, 2)
        self.failUnlessEqual(kCGRenderingIntentPerceptual, 3)
        self.failUnlessEqual(kCGRenderingIntentSaturation, 4)

        self.failUnlessEqual(kCGColorSpaceModelUnknown, -1)
        self.failUnlessEqual(kCGColorSpaceModelMonochrome, 0)
        self.failUnlessEqual(kCGColorSpaceModelRGB, 1)
        self.failUnlessEqual(kCGColorSpaceModelCMYK, 2)
        self.failUnlessEqual(kCGColorSpaceModelLab, 3)
        self.failUnlessEqual(kCGColorSpaceModelDeviceN, 4)
        self.failUnlessEqual(kCGColorSpaceModelIndexed, 5)
        self.failUnlessEqual(kCGColorSpaceModelPattern, 6)

        self.failUnlessIsInstance(kCGColorSpaceGenericGray, unicode)
        self.failUnlessIsInstance(kCGColorSpaceGenericRGB, unicode)
        self.failUnlessIsInstance(kCGColorSpaceGenericCMYK, unicode)
        self.failUnlessIsInstance(kCGColorSpaceGenericRGBLinear, unicode)
        self.failUnlessIsInstance(kCGColorSpaceAdobeRGB1998, unicode)
        self.failUnlessIsInstance(kCGColorSpaceSRGB, unicode)

        self.failUnlessIsInstance(kCGColorSpaceUserGray, basestring)
        self.failUnlessIsInstance(kCGColorSpaceUserRGB, basestring)
        self.failUnlessIsInstance(kCGColorSpaceUserCMYK, basestring)

    def testFunctions(self):
        self.failUnlessResultIsCFRetained(CGColorSpaceCreateDeviceGray)
        self.failUnlessIsInstance(CGColorSpaceCreateDeviceGray(), CGColorSpaceRef)

        self.failUnlessResultIsCFRetained(CGColorSpaceCreateDeviceRGB)
        self.failUnlessIsInstance(CGColorSpaceCreateDeviceRGB(), CGColorSpaceRef)

        self.failUnlessResultIsCFRetained(CGColorSpaceCreateDeviceCMYK)
        self.failUnlessIsInstance(CGColorSpaceCreateDeviceCMYK(), CGColorSpaceRef)

        self.failUnlessResultIsCFRetained(CGColorSpaceCreateCalibratedGray)
        csp = CGColorSpaceCreateCalibratedGray((0, 0, 0), (1, 1, 1), 0.8)
        self.failUnlessIsInstance(csp, CGColorSpaceRef)

        self.failUnlessResultIsCFRetained(CGColorSpaceCreateCalibratedRGB)
        csp = CGColorSpaceCreateCalibratedRGB((0.5, 0.5, 0.2), (0.9, 0.95, 1.0), (0.7, 0.8, 0.9), (0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99))
        self.failUnlessIsInstance(csp, CGColorSpaceRef)

        self.failUnlessResultIsCFRetained(CGColorSpaceCreateLab)
        csp = CGColorSpaceCreateLab((0.1, 0.1, 0.1), (0.99, 0.99, 0.99), (0.1, 0.79, 0.5, 0.99))
        self.failUnlessIsInstance(csp, CGColorSpaceRef)

        self.failUnlessResultIsCFRetained(CGColorSpaceCreatePattern)
        csp = CGColorSpaceCreatePattern(csp)
        self.failUnlessIsInstance(csp, CGColorSpaceRef)

        self.failUnlessResultIsCFRetained(CGColorSpaceCreateWithName)
        csp = CGColorSpaceCreateWithName(kCGColorSpaceGenericRGB)
        self.failUnlessIsInstance(csp, CGColorSpaceRef)

        v = CGColorSpaceRetain(csp)
        self.failUnless(v is csp)
        CGColorSpaceRelease(csp)

        self.failUnlessIsInstance(CGColorSpaceGetTypeID(), (int, long))
        self.failUnlessIsInstance(CGColorSpaceGetNumberOfComponents(csp), (int, long))
        self.failUnlessIsInstance(CGColorSpaceGetModel(csp), (int, long))

        v = CGColorSpaceGetBaseColorSpace(csp)
        self.failUnless(v is None)

        v = CGColorSpaceCreatePattern(csp)
        v = CGColorSpaceGetBaseColorSpace(v)
        self.failUnless(v is csp)

        v = CGColorSpaceGetColorTableCount(csp)
        self.failUnlessEqual(v, 0)

        v = CGColorSpaceCopyICCProfile(csp)
        self.failUnlessIsInstance(v, CFDataRef)


        data = open('/Library/ColorSync/Profiles/WebSafeColors.icc', 'rb').read()
        provider = CGDataProviderCreateWithCFData(buffer(data))
        spc = CGColorSpaceCreateICCBased(3, [0.0, 255.0, 0.0, 255.0, 0.0, 255.0],
                provider, CGColorSpaceCreateDeviceRGB())
        self.failUnlessIsInstance(spc, CGColorSpaceRef)
        
        dta= CGColorSpaceCopyICCProfile(spc)
        self.failUnlessIsInstance(dta, CFDataRef)

        spc = CGColorSpaceCreateIndexed(CGColorSpaceCreateDeviceRGB(), 10,
                (0, 1, 2)*11)
        self.failUnlessIsInstance(spc, CGColorSpaceRef) 

        self.failUnlessEqual(CGColorSpaceGetModel(spc), kCGColorSpaceModelIndexed)

        v = CGColorSpaceGetColorTableCount(spc)
        self.failUnlessEqual(v, 11)

        buf = array.array('B', [99] * (3*11))
        v = CGColorSpaceGetColorTable(spc, buf)
        self.failUnless(buf is v)
        self.failUnless(buf[0] == 0)
        self.failUnless(buf[1] == 1)
        self.failUnless(buf[2] == 2)
        self.failUnless(buf[3] == 0)
        self.failUnless(buf[4] == 1)
        self.failUnless(buf[5] == 2)

if __name__ == "__main__":
    main()
