import array
import objc

from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


def buffer(value):
    if isinstance(value, bytes):
        return value
    return value.encode("latin1")


class TestCGColorSpace(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kCGRenderingIntentDefault, 0)
        self.assertEqual(Quartz.kCGRenderingIntentAbsoluteColorimetric, 1)
        self.assertEqual(Quartz.kCGRenderingIntentRelativeColorimetric, 2)
        self.assertEqual(Quartz.kCGRenderingIntentPerceptual, 3)
        self.assertEqual(Quartz.kCGRenderingIntentSaturation, 4)

        self.assertEqual(Quartz.kCGColorSpaceModelUnknown, -1)
        self.assertEqual(Quartz.kCGColorSpaceModelMonochrome, 0)
        self.assertEqual(Quartz.kCGColorSpaceModelRGB, 1)
        self.assertEqual(Quartz.kCGColorSpaceModelCMYK, 2)
        self.assertEqual(Quartz.kCGColorSpaceModelLab, 3)
        self.assertEqual(Quartz.kCGColorSpaceModelDeviceN, 4)
        self.assertEqual(Quartz.kCGColorSpaceModelIndexed, 5)
        self.assertEqual(Quartz.kCGColorSpaceModelPattern, 6)
        self.assertEqual(Quartz.kCGColorSpaceModelXYZ, 7)

        self.assertIsInstance(Quartz.kCGColorSpaceGenericGray, str)
        self.assertIsInstance(Quartz.kCGColorSpaceGenericRGB, str)
        self.assertIsInstance(Quartz.kCGColorSpaceGenericCMYK, str)

        self.assertIsInstance(Quartz.kCGColorSpaceUserGray, (str, str))
        self.assertIsInstance(Quartz.kCGColorSpaceUserRGB, (str, str))
        self.assertIsInstance(Quartz.kCGColorSpaceUserCMYK, (str, str))

        self.assertEqual(Quartz.CG_HDR_BT_2100, 1)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(Quartz.kCGColorSpaceGenericRGBLinear, str)
        self.assertIsInstance(Quartz.kCGColorSpaceAdobeRGB1998, str)
        self.assertIsInstance(Quartz.kCGColorSpaceSRGB, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.kCGColorSpaceGenericGrayGamma2_2, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(Quartz.kCGColorSpaceDisplayP3, str)

        self.assertIsInstance(Quartz.kCGColorSpaceGenericXYZ, str)
        self.assertIsInstance(Quartz.kCGColorSpaceACESCGLinear, str)
        self.assertIsInstance(Quartz.kCGColorSpaceITUR_709, str)
        self.assertIsInstance(Quartz.kCGColorSpaceITUR_2020, str)
        self.assertIsInstance(Quartz.kCGColorSpaceROMMRGB, str)
        self.assertIsInstance(Quartz.kCGColorSpaceDCIP3, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Quartz.kCGColorSpaceExtendedSRGB, str)
        self.assertIsInstance(Quartz.kCGColorSpaceLinearSRGB, str)
        self.assertIsInstance(Quartz.kCGColorSpaceExtendedLinearSRGB, str)
        self.assertIsInstance(Quartz.kCGColorSpaceExtendedGray, str)
        self.assertIsInstance(Quartz.kCGColorSpaceLinearGray, str)
        self.assertIsInstance(Quartz.kCGColorSpaceExtendedLinearGray, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Quartz.kCGColorSpaceGenericLab, str)

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(Quartz.kCGColorSpaceITUR_2020_PQ_EOTF, str)

    @min_os_level("10.14.3")
    def testConstants10_14_3(self):
        self.assertIsInstance(Quartz.kCGColorSpaceExtendedLinearITUR_2020, str)
        self.assertIsInstance(Quartz.kCGColorSpaceExtendedLinearDisplayP3, str)

    @min_os_level("10.15")
    def testConstants10_14_6(self):
        self.assertIsInstance(Quartz.kCGColorSpaceDisplayP3_PQ_EOTF, str)
        self.assertIsInstance(Quartz.kCGColorSpaceDisplayP3_HLG, str)
        self.assertIsInstance(Quartz.kCGColorSpaceITUR_2020_HLG, str)

    @min_os_level("10.15.5")
    def testConstants10_15_4(self):
        self.assertIsInstance(Quartz.kCGColorSpaceITUR_2020_PQ, str)
        self.assertIsInstance(Quartz.kCGColorSpaceDisplayP3_PQ, str)

    @min_os_level("10.16")
    def testConstants10_16(self):
        self.assertIsInstance(Quartz.kCGColorSpaceITUR_2100_PQ, str)
        self.assertIsInstance(Quartz.kCGColorSpaceITUR_2100_HLG, str)

        self.assertIsInstance(Quartz.kCGColorSpaceExtendedITUR_2020, str)
        self.assertIsInstance(Quartz.kCGColorSpaceExtendedDisplayP3, str)

    def testFunctions(self):
        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreateDeviceGray)
        self.assertIsInstance(
            Quartz.CGColorSpaceCreateDeviceGray(), Quartz.CGColorSpaceRef
        )

        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreateDeviceRGB)
        self.assertIsInstance(
            Quartz.CGColorSpaceCreateDeviceRGB(), Quartz.CGColorSpaceRef
        )

        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreateDeviceCMYK)
        self.assertIsInstance(
            Quartz.CGColorSpaceCreateDeviceCMYK(), Quartz.CGColorSpaceRef
        )

        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreateCalibratedGray)
        csp = Quartz.CGColorSpaceCreateCalibratedGray((0, 0, 0), (1, 1, 1), 0.8)
        self.assertIsInstance(csp, Quartz.CGColorSpaceRef)

        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreateCalibratedRGB)
        csp = Quartz.CGColorSpaceCreateCalibratedRGB(
            (0.5, 0.5, 0.2),
            (0.9, 0.95, 1.0),
            (0.7, 0.8, 0.9),
            (0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99),
        )
        self.assertIsInstance(csp, Quartz.CGColorSpaceRef)

        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreateLab)
        csp = Quartz.CGColorSpaceCreateLab(
            (0.1, 0.1, 0.1), (0.99, 0.99, 0.99), (0.1, 0.79, 0.5, 0.99)
        )
        self.assertIsInstance(csp, Quartz.CGColorSpaceRef)

        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreatePattern)
        csp = Quartz.CGColorSpaceCreatePattern(csp)
        self.assertIsInstance(csp, Quartz.CGColorSpaceRef)

        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreateWithName)
        csp = Quartz.CGColorSpaceCreateWithName(Quartz.kCGColorSpaceGenericRGB)
        self.assertIsInstance(csp, Quartz.CGColorSpaceRef)

        v = Quartz.CGColorSpaceRetain(csp)
        self.assertTrue(v is csp)
        Quartz.CGColorSpaceRelease(csp)

        self.assertIsInstance(Quartz.CGColorSpaceGetTypeID(), int)
        self.assertIsInstance(Quartz.CGColorSpaceGetNumberOfComponents(csp), int)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        csp = Quartz.CGColorSpaceCreateWithName(Quartz.kCGColorSpaceGenericRGB)
        self.assertIsInstance(Quartz.CGColorSpaceGetModel(csp), int)

        v = Quartz.CGColorSpaceGetBaseColorSpace(csp)
        self.assertTrue(v is None)

        v = Quartz.CGColorSpaceCreatePattern(csp)
        v = Quartz.CGColorSpaceGetBaseColorSpace(v)
        self.assertTrue(v is csp)

        v = Quartz.CGColorSpaceGetColorTableCount(csp)
        self.assertEqual(v, 0)

        v = Quartz.CGColorSpaceCopyICCProfile(csp)
        self.assertIsInstance(v, Quartz.CFDataRef)

        with open("/Library/ColorSync/Profiles/WebSafeColors.icc", "rb") as fp:
            data = fp.read()
        provider = Quartz.CGDataProviderCreateWithCFData(buffer(data))
        spc = Quartz.CGColorSpaceCreateICCBased(
            3,
            [0.0, 255.0, 0.0, 255.0, 0.0, 255.0],
            provider,
            Quartz.CGColorSpaceCreateDeviceRGB(),
        )
        self.assertIsInstance(spc, Quartz.CGColorSpaceRef)

        dta = Quartz.CGColorSpaceCopyICCProfile(csp)
        self.assertIsInstance(dta, Quartz.CFDataRef)

        spc = Quartz.CGColorSpaceCreateIndexed(
            Quartz.CGColorSpaceCreateDeviceRGB(), 10, (0, 1, 2) * 11
        )
        self.assertIsInstance(spc, Quartz.CGColorSpaceRef)

        self.assertEqual(
            Quartz.CGColorSpaceGetModel(spc), Quartz.kCGColorSpaceModelIndexed
        )

        v = Quartz.CGColorSpaceGetColorTableCount(spc)
        self.assertEqual(v, 11)

        buf = array.array("B", [99] * (3 * 11))
        v = Quartz.CGColorSpaceGetColorTable(spc, buf)
        self.assertTrue(buf is v)
        self.assertTrue(buf[0] == 0)
        self.assertTrue(buf[1] == 1)
        self.assertTrue(buf[2] == 2)
        self.assertTrue(buf[3] == 0)
        self.assertTrue(buf[4] == 1)
        self.assertTrue(buf[5] == 2)

        spc = Quartz.CGColorSpaceCreateWithName(Quartz.kCGColorSpaceGenericRGB)
        self.assertIsInstance(spc, Quartz.CGColorSpaceRef)

        dta = Quartz.CGColorSpaceCopyICCProfile(spc)
        self.assertIsInstance(dta, Quartz.CFDataRef)

        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreateWithICCProfile)
        v = Quartz.CGColorSpaceCreateWithICCProfile(dta)
        self.assertIsInstance(v, Quartz.CGColorSpaceRef)

    @min_os_level("10.6")
    def testFunctions10_6(self):
        csp = Quartz.CGColorSpaceCreateWithName(Quartz.kCGColorSpaceGenericRGB)
        self.assertIsInstance(csp, Quartz.CGColorSpaceRef)

        v = Quartz.CGColorSpaceCopyName(csp)
        self.assertIsInstance(v, str)

    @min_os_level("10.12")
    def testFunctions10_12(self):
        self.assertResultIsCFRetained(Quartz.CGColorSpaceCopyICCData)
        self.assertResultHasType(Quartz.CGColorSpaceIsWideGamutRGB, objc._C_BOOL)
        self.assertResultHasType(Quartz.CGColorSpaceSupportsOutput, objc._C_BOOL)
        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreateWithICCData)

        self.assertResultHasType(Quartz.CGColorSpaceUsesExtendedRange, objc._C_BOOL)

    @min_os_level("10.13")
    def testFunctions10_13(self):
        Quartz.CGColorSpaceGetName

    @min_os_level("10.15")
    def testFunctions10_15(self):
        Quartz.CGColorSpaceIsHDR

    @min_os_level("10.16")
    def testFunctions10_16(self):
        Quartz.CGColorSpaceUsesITUR_2100TF

        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreateLinearized)
        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreateExtended)
        self.assertResultIsCFRetained(Quartz.CGColorSpaceCreateExtendedLinearized)
