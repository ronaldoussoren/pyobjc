from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import Quartz


class TestCGColorConvertor(TestCase):
    @min_os_level("10.12")
    def test_types(self):
        self.assertIs(Quartz.CGColorConversionInfoRef, Quartz.CGColorConverterRef)

    @min_os_level("10.12")
    def test_constants(self):
        self.assertEqual(
            Quartz.kCGColorConverterTransformFromSpace,
            Quartz.kCGColorConversionTransformFromSpace,
        )
        self.assertEqual(
            Quartz.kCGColorConverterTransformToSpace,
            Quartz.kCGColorConversionTransformToSpace,
        )
        self.assertEqual(
            Quartz.kCGColorConverterTransformApplySpace,
            Quartz.kCGColorConversionTransformApplySpace,
        )

    @min_os_level("10.12")
    def test_functions(self):
        self.assertResultIsCFRetained(Quartz.CGColorConverterCreateSimple)

    @expectedFailure
    @min_os_level("10.12")
    def testFunctionHard(self):
        self.fail("Quartz.CGColorConverterCreate")  # Varargs with annoying signature
