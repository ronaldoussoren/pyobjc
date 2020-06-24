import os

import Quartz
from PyObjCTools.TestSupport import TestCase
import objc


class TestCGFunction(TestCase):
    def testFunctions(self):
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

        v = Quartz.CGFunctionRetain(func)
        self.assertTrue(v is func)
        Quartz.CGFunctionRelease(func)

        # It is not possible to "call" a Quartz.CGFunction object directly, use a
        # shading object to check that the function is actually called.

        shading = Quartz.CGShadingCreateAxial(
            Quartz.CGColorSpaceCreateDeviceRGB(), (0, 0), (50, 50), func, True, True
        )
        self.assertIsInstance(shading, Quartz.CGShadingRef)

        url = Quartz.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", Quartz.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, Quartz.CFURLRef)
        context = Quartz.CGPDFContextCreateWithURL(url, ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, Quartz.CGContextRef)
        try:
            Quartz.CGContextBeginPage(context, objc.NULL)

            Quartz.CGContextDrawShading(context, shading)
        finally:
            Quartz.CGContextEndPage(context)
            if hasattr(Quartz, "CGPDFContextClose"):
                Quartz.CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

        # Drawing is done, check that the shading function is actually used
        self.assertNotEqual(len(values), 0)
        for item in values:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 1)
            self.assertIsInstance(item[0], float)

        del func
