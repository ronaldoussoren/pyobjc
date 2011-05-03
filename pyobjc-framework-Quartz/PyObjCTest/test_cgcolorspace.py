
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
import array
import sys

if sys.version_info[0] != 2:
    def buffer(value):
        if isinstance(value, bytes):
            return value
        return value.encode('latin1')

class TestCGColorSpace (TestCase):
    def testConstants(self):
        self.assertEqual(kCGRenderingIntentDefault, 0)
        self.assertEqual(kCGRenderingIntentAbsoluteColorimetric, 1)
        self.assertEqual(kCGRenderingIntentRelativeColorimetric, 2)
        self.assertEqual(kCGRenderingIntentPerceptual, 3)
        self.assertEqual(kCGRenderingIntentSaturation, 4)

        self.assertEqual(kCGColorSpaceModelUnknown, -1)
        self.assertEqual(kCGColorSpaceModelMonochrome, 0)
        self.assertEqual(kCGColorSpaceModelRGB, 1)
        self.assertEqual(kCGColorSpaceModelCMYK, 2)
        self.assertEqual(kCGColorSpaceModelLab, 3)
        self.assertEqual(kCGColorSpaceModelDeviceN, 4)
        self.assertEqual(kCGColorSpaceModelIndexed, 5)
        self.assertEqual(kCGColorSpaceModelPattern, 6)

        self.assertIsInstance(kCGColorSpaceGenericGray, unicode)
        self.assertIsInstance(kCGColorSpaceGenericRGB, unicode)
        self.assertIsInstance(kCGColorSpaceGenericCMYK, unicode)

        self.assertIsInstance(kCGColorSpaceUserGray, basestring)
        self.assertIsInstance(kCGColorSpaceUserRGB, basestring)
        self.assertIsInstance(kCGColorSpaceUserCMYK, basestring)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCGColorSpaceGenericRGBLinear, unicode)
        self.assertIsInstance(kCGColorSpaceAdobeRGB1998, unicode)
        self.assertIsInstance(kCGColorSpaceSRGB, unicode)


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCGColorSpaceGenericGrayGamma2_2, unicode)


    def testFunctions(self):
        self.assertResultIsCFRetained(CGColorSpaceCreateDeviceGray)
        self.assertIsInstance(CGColorSpaceCreateDeviceGray(), CGColorSpaceRef)

        self.assertResultIsCFRetained(CGColorSpaceCreateDeviceRGB)
        self.assertIsInstance(CGColorSpaceCreateDeviceRGB(), CGColorSpaceRef)

        self.assertResultIsCFRetained(CGColorSpaceCreateDeviceCMYK)
        self.assertIsInstance(CGColorSpaceCreateDeviceCMYK(), CGColorSpaceRef)

        self.assertResultIsCFRetained(CGColorSpaceCreateCalibratedGray)
        csp = CGColorSpaceCreateCalibratedGray((0, 0, 0), (1, 1, 1), 0.8)
        self.assertIsInstance(csp, CGColorSpaceRef)

        self.assertResultIsCFRetained(CGColorSpaceCreateCalibratedRGB)
        csp = CGColorSpaceCreateCalibratedRGB((0.5, 0.5, 0.2), (0.9, 0.95, 1.0), (0.7, 0.8, 0.9), (0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99))
        self.assertIsInstance(csp, CGColorSpaceRef)

        self.assertResultIsCFRetained(CGColorSpaceCreateLab)
        csp = CGColorSpaceCreateLab((0.1, 0.1, 0.1), (0.99, 0.99, 0.99), (0.1, 0.79, 0.5, 0.99))
        self.assertIsInstance(csp, CGColorSpaceRef)

        self.assertResultIsCFRetained(CGColorSpaceCreatePattern)
        csp = CGColorSpaceCreatePattern(csp)
        self.assertIsInstance(csp, CGColorSpaceRef)

        self.assertResultIsCFRetained(CGColorSpaceCreateWithName)
        csp = CGColorSpaceCreateWithName(kCGColorSpaceGenericRGB)
        self.assertIsInstance(csp, CGColorSpaceRef)

        v = CGColorSpaceRetain(csp)
        self.assertTrue(v is csp)
        CGColorSpaceRelease(csp)

        self.assertIsInstance(CGColorSpaceGetTypeID(), (int, long))
        self.assertIsInstance(CGColorSpaceGetNumberOfComponents(csp), (int, long))

    @min_os_level('10.5')
    def testFunctions10_5(self):
        csp = CGColorSpaceCreateWithName(kCGColorSpaceGenericRGB)
        self.assertIsInstance(CGColorSpaceGetModel(csp), (int, long))

        v = CGColorSpaceGetBaseColorSpace(csp)
        self.assertTrue(v is None)

        v = CGColorSpaceCreatePattern(csp)
        v = CGColorSpaceGetBaseColorSpace(v)
        self.assertTrue(v is csp)

        v = CGColorSpaceGetColorTableCount(csp)
        self.assertEqual(v, 0)

        v = CGColorSpaceCopyICCProfile(csp)
        self.assertIsInstance(v, CFDataRef)

        data = open('/Library/ColorSync/Profiles/WebSafeColors.icc', 'rb').read()
        provider = CGDataProviderCreateWithCFData(buffer(data))
        spc = CGColorSpaceCreateICCBased(3, [0.0, 255.0, 0.0, 255.0, 0.0, 255.0],
                provider, CGColorSpaceCreateDeviceRGB())
        self.assertIsInstance(spc, CGColorSpaceRef)
        
        dta= CGColorSpaceCopyICCProfile(spc)
        self.assertIsInstance(dta, CFDataRef)

        spc = CGColorSpaceCreateIndexed(CGColorSpaceCreateDeviceRGB(), 10,
                (0, 1, 2)*11)
        self.assertIsInstance(spc, CGColorSpaceRef) 

        self.assertEqual(CGColorSpaceGetModel(spc), kCGColorSpaceModelIndexed)

        v = CGColorSpaceGetColorTableCount(spc)
        self.assertEqual(v, 11)

        buf = array.array('B', [99] * (3*11))
        v = CGColorSpaceGetColorTable(spc, buf)
        self.assertTrue(buf is v)
        self.assertTrue(buf[0] == 0)
        self.assertTrue(buf[1] == 1)
        self.assertTrue(buf[2] == 2)
        self.assertTrue(buf[3] == 0)
        self.assertTrue(buf[4] == 1)
        self.assertTrue(buf[5] == 2)

        spc = CGColorSpaceCreateWithName(kCGColorSpaceGenericRGB)
        self.assertIsInstance(spc, CGColorSpaceRef)

        dta= CGColorSpaceCopyICCProfile(spc)
        self.assertIsInstance(dta, CFDataRef)

        self.assertResultIsCFRetained(CGColorSpaceCreateWithICCProfile)
        v = CGColorSpaceCreateWithICCProfile(dta)
        self.assertIsInstance(v, CGColorSpaceRef)

    @min_os_level('10.6')
    def testFunctions10_6(self):
        csp = CGColorSpaceCreateWithName(kCGColorSpaceGenericRGB)
        self.assertIsInstance(csp, CGColorSpaceRef)

        v = CGColorSpaceCopyName(csp)
        self.assertIsInstance(v, unicode)
        

if __name__ == "__main__":
    main()
