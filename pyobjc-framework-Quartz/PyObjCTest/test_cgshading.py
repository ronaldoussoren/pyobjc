
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGShading (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGShadingRef)

    def testFunctions(self):
        self.failUnlessIsInstance(CGShadingGetTypeID(), (int, long))

        values = []
        def evaluate(info, input, output):
            values.append(input)
            return input * 4
        
        self.failUnlessIsInstance(CGFunctionGetTypeID(), (int, long))

        myInfo = object()
        func = CGFunctionCreate(myInfo, 1, [0, 1], 4, [0, 1, 0, 1, 0, 1, 0, 1], evaluate)
        self.failUnlessIsInstance(func, CGFunctionRef)


        self.failUnlessResultIsCFRetained(CGShadingCreateAxial)
        self.failUnlessArgHasType(CGShadingCreateAxial, 4, objc._C_BOOL)
        self.failUnlessArgHasType(CGShadingCreateAxial, 5, objc._C_BOOL)
        shading = CGShadingCreateAxial(
                CGColorSpaceCreateDeviceRGB(), CGPoint(0, 0), CGPoint(50, 200),
                func, False, False)
        self.failUnlessIsInstance(shading, CGShadingRef)

        self.failUnlessResultIsCFRetained(CGShadingCreateRadial)
        self.failUnlessArgHasType(CGShadingCreateRadial, 6, objc._C_BOOL)
        self.failUnlessArgHasType(CGShadingCreateRadial, 7, objc._C_BOOL)
        shading = CGShadingCreateRadial(
                CGColorSpaceCreateDeviceRGB(), CGPoint(0, 0), 5.0, 
                CGPoint(50, 200), 10.5, func, False, False)
        self.failUnlessIsInstance(shading, CGShadingRef)

        v = CGShadingRetain(shading)
        self.failUnless(v is shading)

        CGShadingRelease(shading)




if __name__ == "__main__":
    main()
