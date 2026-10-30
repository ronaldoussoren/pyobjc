import os

import Quartz
from PyObjCTools.TestSupport import TestCase
import objc


class TestCGFunction(TestCase):
    def test_functions(self):
        values = []

        def evaluate(info, input_value, output_value):
            values.append(input_value)
            return input_value * 4

        self.assertIsInstance(Quartz.CGFunctionGetTypeID(), int)

        with self.assertRaisesRegex(TypeError, "expected 6 arguments, got 0"):
            Quartz.CGFunctionCreate()
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            Quartz.CGFunctionCreate(None, "1", (0, 1), 2, (0, 1, 0, 1), evaluate)
        with self.assertRaisesRegex(
            ValueError, r"too few values \(2\) expecting at least 4"
        ):
            Quartz.CGFunctionCreate(None, 2, (0, 1), 2, (0, 1, 0, 1), evaluate)
        with self.assertRaisesRegex(TypeError, "converting to a C array"):
            Quartz.CGFunctionCreate(None, 1, 42, 2, (0, 1, 0, 1), evaluate)
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            Quartz.CGFunctionCreate(None, 1, (0, 1), "2", (0, 1, 0, 1), evaluate)
        with self.assertRaisesRegex(
            ValueError, r"too few values \(4\) expecting at least 6"
        ):
            Quartz.CGFunctionCreate(None, 1, (0, 1), 3, (0, 1, 0, 1), evaluate)
        with self.assertRaisesRegex(TypeError, "converting to a C array"):
            Quartz.CGFunctionCreate(None, 1, (0, 1), 2, 42, evaluate)
        with self.assertRaisesRegex(
            TypeError, "evaluate not callable, but of type int"
        ):
            func = Quartz.CGFunctionCreate(None, 1, (0, 1), 2, (0, 1, 0, 1), 42)

        func = Quartz.CGFunctionCreate(None, 0, None, 0, None, evaluate)
        self.assertIs(func, None)

        func_no_domain = Quartz.CGFunctionCreate(None, 1, None, 2, None, evaluate)
        self.assertIsInstance(func_no_domain, Quartz.CGFunctionRef)

        def evaluate_raises(info, input_value, output_value):
            raise RuntimeError("evaluate error")

        func_raises = Quartz.CGFunctionCreate(None, 1, None, 2, None, evaluate_raises)
        self.assertIsInstance(func_raises, Quartz.CGFunctionRef)

        def evaluate_invalid(info, input_value, output_value):
            return 42

        func_invalid = Quartz.CGFunctionCreate(None, 1, None, 2, None, evaluate_invalid)
        self.assertIsInstance(func_raises, Quartz.CGFunctionRef)

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

        shading_no_domain = Quartz.CGShadingCreateAxial(
            Quartz.CGColorSpaceCreateDeviceGray(),
            (0, 0),
            (30, 90),
            func_no_domain,
            False,
            False,
        )
        self.assertIsInstance(shading_no_domain, Quartz.CGShadingRef)

        shading_raises = Quartz.CGShadingCreateAxial(
            Quartz.CGColorSpaceCreateDeviceGray(),
            (0, 0),
            (30, 90),
            func_raises,
            False,
            False,
        )
        self.assertIsInstance(shading_raises, Quartz.CGShadingRef)
        shading_invalid = Quartz.CGShadingCreateAxial(
            Quartz.CGColorSpaceCreateDeviceGray(),
            (0, 0),
            (30, 90),
            func_invalid,
            False,
            False,
        )
        self.assertIsInstance(shading_invalid, Quartz.CGShadingRef)

        url = Quartz.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", Quartz.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, Quartz.CFURLRef)
        context = Quartz.CGPDFContextCreateWithURL(url, ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, Quartz.CGContextRef)
        try:
            Quartz.CGContextBeginPage(context, objc.NULL)

            Quartz.CGContextDrawShading(context, shading)
            Quartz.CGContextDrawShading(context, shading_no_domain)
            Quartz.CGContextEndPage(context)
            with self.assertRaisesRegex(RuntimeError, "evaluate error"):
                Quartz.CGContextBeginPage(context, objc.NULL)
                Quartz.CGContextDrawShading(context, shading_raises)
                Quartz.CGContextEndPage(context)
            with self.assertRaisesRegex(
                TypeError, "depythonifying array, got no sequence"
            ):
                Quartz.CGContextBeginPage(context, objc.NULL)
                Quartz.CGContextDrawShading(context, shading_invalid)
                Quartz.CGContextEndPage(context)
            Quartz.CGContextBeginPage(context, objc.NULL)
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
