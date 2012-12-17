
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

try:
    long
except NameError:
    long = int

class TestCGShading (TestCase):
    def testTypes(self):
        self.assertIsCFType(CGShadingRef)

    def testFunctions(self):
        self.assertIsInstance(CGShadingGetTypeID(), (int, long))

        values = []
        def evaluate(info, input, output):
            values.append(input)
            return input * 4

        self.assertIsInstance(CGFunctionGetTypeID(), (int, long))

        myInfo = object()
        func = CGFunctionCreate(myInfo, 1, [0, 1], 4, [0, 1, 0, 1, 0, 1, 0, 1], evaluate)
        self.assertIsInstance(func, CGFunctionRef)


        self.assertResultIsCFRetained(CGShadingCreateAxial)
        self.assertArgHasType(CGShadingCreateAxial, 4, objc._C_BOOL)
        self.assertArgHasType(CGShadingCreateAxial, 5, objc._C_BOOL)
        shading = CGShadingCreateAxial(
                CGColorSpaceCreateDeviceRGB(), CGPoint(0, 0), CGPoint(50, 200),
                func, False, False)
        self.assertIsInstance(shading, CGShadingRef)

        self.assertResultIsCFRetained(CGShadingCreateRadial)
        self.assertArgHasType(CGShadingCreateRadial, 6, objc._C_BOOL)
        self.assertArgHasType(CGShadingCreateRadial, 7, objc._C_BOOL)
        shading = CGShadingCreateRadial(
                CGColorSpaceCreateDeviceRGB(), CGPoint(0, 0), 5.0,
                CGPoint(50, 200), 10.5, func, False, False)
        self.assertIsInstance(shading, CGShadingRef)

        v = CGShadingRetain(shading)
        self.assertTrue(v is shading)

        CGShadingRelease(shading)




if __name__ == "__main__":
    main()
