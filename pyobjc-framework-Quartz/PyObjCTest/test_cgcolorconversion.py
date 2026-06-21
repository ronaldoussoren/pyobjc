from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import Quartz


class TestCGColorConversion(TestCase):
    @min_os_level("10.12")
    def test_types(self):
        self.assertIsCFType(Quartz.CGColorConversionInfoRef)

    @min_os_level("10.12")
    def test_constants(self):
        self.assertIsEnumType(Quartz.CGColorConversionInfoTransformType)
        self.assertEqual(Quartz.kCGColorConversionTransformFromSpace, 0)
        self.assertEqual(Quartz.kCGColorConversionTransformToSpace, 1)
        self.assertEqual(Quartz.kCGColorConversionTransformApplySpace, 2)

        self.assertIsInstance(Quartz.kCGColorConversionBlackPointCompensation, str)

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(Quartz.kCGColorConversionTRCSize, str)

    @min_os_level("10.12")
    def test_functions(self):
        self.assertResultIsCFRetained(Quartz.CGColorConversionInfoCreate)

    @min_os_level("10.14.6")
    def test_functions10_14_6(self):
        self.assertResultIsCFRetained(Quartz.CGColorConversionInfoCreateWithOptions)

    @expectedFailure
    @min_os_level("10.12")
    def test_functions_manual(self):
        self.fail(
            "Quartz.CGColorConversionInfoCreateFromList"
        )  # Varargs with annoying signature

    @min_os_level("10.13")
    def test_functions10_13(self):
        try:
            Quartz.CGColorConversionInfoCreateFromListWithArguments
        except AttributeError:
            pass
        else:
            self.fail("CGColorConversionInfoCreateFromList is wrapped")

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsCFRetained(Quartz.CGColorConversionInfoCreateForToneMapping)
        self.assertArgIsOut(Quartz.CGColorConversionInfoCreateForToneMapping, 6)

        self.assertArgIsIn(Quartz.CGColorConversionInfoConvertData, 3)
        self.assertArgIsVariableSize(Quartz.CGColorConversionInfoConvertData, 3)
