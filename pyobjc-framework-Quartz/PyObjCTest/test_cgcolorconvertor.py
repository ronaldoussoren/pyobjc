from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGColorConvertor (TestCase):
    @min_os_level('10.12')
    def testTypes(self):
        self.assertIs(CGColorConversionInfoRef, CGColorConverterRef)

    @min_os_level('10.12')
    def testConstants(self):
        self.assertEqual(kCGColorConverterTransformFromSpace, kCGColorConversionTransformFromSpace)
        self.assertEqual(kCGColorConverterTransformToSpace, kCGColorConversionTransformToSpace)
        self.assertEqual(kCGColorConverterTransformApplySpace, kCGColorConversionTransformApplySpace)

    @min_os_level('10.12')
    def testFunctions(self):
        self.assertResultIsCFRetained(CGColorConverterCreateSimple)

    @expectedFailure
    @min_os_level('10.12')
    def testFunctionHard(self):
        self.fail("CGColorConverterCreate") # Varargs with annoying signature


if __name__ == "__main__":
    main()
