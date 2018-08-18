from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGColorConversion (TestCase):
    @min_os_level('10.12')
    def testTypes(self):
        self.assertIsCFType(CGColorConversionInfoRef)

    @min_os_level('10.12')
    def testConstants(self):
        self.assertEqual(kCGColorConversionTransformFromSpace, 0)
        self.assertEqual(kCGColorConversionTransformToSpace, 1)
        self.assertEqual(kCGColorConversionTransformApplySpace, 2)

        self.assertIsInstance(kCGColorConversionBlackPointCompensation, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(kCGColorConversionTRCSize, unicode)

    @min_os_level('10.12')
    def testFunctions(self):
        self.assertResultIsCFRetained(CGColorConversionInfoCreate)

    @expectedFailure
    @min_os_level('10.12')
    def testFunctionHard(self):
        self.fail("CGColorConversionInfoCreateFromList") # Varargs with annoying signature

    @min_os_level('10.13')
    def testFunctions(self):
        try:
            CGColorConversionInfoCreateFromList
        except NameError:
            pass
        else:
            self.fail("CGColorConversionInfoCreateFromList is wrapped")

if __name__ == "__main__":
    main()
