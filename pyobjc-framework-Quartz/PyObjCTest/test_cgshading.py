from PyObjCTools.TestSupport import TestCase
import Quartz
import objc


class TestCGShading(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CGShadingRef)

    def testFunctions(self):
        self.assertIsInstance(Quartz.CGShadingGetTypeID(), int)

        values = []

        def evaluate(info, input_value, output_value):
            values.append(input_value)
            return input_value * 4

        self.assertIsInstance(Quartz.CGFunctionGetTypeID(), int)

        myInfo = object()
        func = Quartz.CGFunctionCreate(
            myInfo, 1, [0, 1], 4, [0, 1, 0, 1, 0, 1, 0, 1], evaluate
        )
        self.assertIsInstance(func, Quartz.CGFunctionRef)

        self.assertResultIsCFRetained(Quartz.CGShadingCreateAxial)
        self.assertArgHasType(Quartz.CGShadingCreateAxial, 4, objc._C_BOOL)
        self.assertArgHasType(Quartz.CGShadingCreateAxial, 5, objc._C_BOOL)
        shading = Quartz.CGShadingCreateAxial(
            Quartz.CGColorSpaceCreateDeviceRGB(),
            Quartz.CGPoint(0, 0),
            Quartz.CGPoint(50, 200),
            func,
            False,
            False,
        )
        self.assertIsInstance(shading, Quartz.CGShadingRef)

        self.assertResultIsCFRetained(Quartz.CGShadingCreateRadial)
        self.assertArgHasType(Quartz.CGShadingCreateRadial, 6, objc._C_BOOL)
        self.assertArgHasType(Quartz.CGShadingCreateRadial, 7, objc._C_BOOL)
        shading = Quartz.CGShadingCreateRadial(
            Quartz.CGColorSpaceCreateDeviceRGB(),
            Quartz.CGPoint(0, 0),
            5.0,
            Quartz.CGPoint(50, 200),
            10.5,
            func,
            False,
            False,
        )
        self.assertIsInstance(shading, Quartz.CGShadingRef)

        v = Quartz.CGShadingRetain(shading)
        self.assertTrue(v is shading)

        Quartz.CGShadingRelease(shading)
