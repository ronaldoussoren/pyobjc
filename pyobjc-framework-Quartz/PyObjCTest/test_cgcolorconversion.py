from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import Quartz


class TestCGColorConversion(TestCase):
    @min_os_level("10.12")
    def testTypes(self):
        self.assertIsCFType(Quartz.CGColorConversionInfoRef)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Quartz.kCGColorConversionTransformFromSpace, 0)
        self.assertEqual(Quartz.kCGColorConversionTransformToSpace, 1)
        self.assertEqual(Quartz.kCGColorConversionTransformApplySpace, 2)

        self.assertIsInstance(Quartz.kCGColorConversionBlackPointCompensation, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Quartz.kCGColorConversionTRCSize, str)

    @min_os_level("10.12")
    def testFunctions(self):
        self.assertResultIsCFRetained(Quartz.CGColorConversionInfoCreate)

    @min_os_level("10.14.6")
    def testFunctions10_14_6(self):
        self.assertResultIsCFRetained(Quartz.CGColorConversionInfoCreateWithOptions)

    @expectedFailure
    @min_os_level("10.12")
    def testFunctionHard(self):
        self.fail(
            "Quartz.CGColorConversionInfoCreateFromList"
        )  # Varargs with annoying signature

    @min_os_level("10.13")
    def testFunctions10_13(self):
        try:
            Quartz.CGColorConversionInfoCreateFromList
        except AttributeError:
            pass
        else:
            self.fail("CGColorConversionInfoCreateFromList is wrapped")
