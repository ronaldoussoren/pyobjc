import CoreText
import Quartz
import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, NoObjCClass
import io
import sys


class TestCTRunDelegate(TestCase):
    def test_enums(self):
        # Unnamed enum:
        self.assertEqual(CoreText.kCTRunDelegateVersion1, 1)
        self.assertEqual(
            CoreText.kCTRunDelegateCurrentVersion, CoreText.kCTRunDelegateVersion1
        )

    def test_types(self):
        self.assertIsCFType(CoreText.CTRunDelegateRef)

    @min_os_level("10.9")
    def test_functions(self):
        self.assertIsInstance(CoreText.CTRunDelegateGetTypeID(), int)

        def getAscender(info):
            return info["ascender"]

        def getDescender(info):
            return info["descender"]

        def getWidth(info):
            return info["width"]

        rc = {"ascender": 1.0, "descender": 2.0, "width": 3.0}

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            CoreText.CTRunDelegateCreate()

        with self.assertRaisesRegex(ValueError, "arg0 must be a tuple of 3 callables"):
            CoreText.CTRunDelegateCreate(42, rc)

        with self.assertRaisesRegex(TypeError, "getAscender is not callable"):
            delegate = CoreText.CTRunDelegateCreate((42, getDescender, getWidth), rc)

        with self.assertRaisesRegex(TypeError, "getDescender is not callable"):
            delegate = CoreText.CTRunDelegateCreate((getAscender, 42, getWidth), rc)

        with self.assertRaisesRegex(TypeError, "getWidth is not callable"):
            delegate = CoreText.CTRunDelegateCreate((getAscender, getDescender, 42), rc)

        delegate = CoreText.CTRunDelegateCreate(
            (getAscender, getDescender, getWidth), rc
        )
        self.assertIsInstance(delegate, CoreText.CTRunDelegateRef)

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 0"):
            CoreText.CTRunDelegateGetRefCon()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreText.CTRunDelegateGetRefCon(NoObjCClass())

        v = CoreText.CTRunDelegateGetRefCon(delegate)
        self.assertIs(v, rc)

        buf = AppKit.NSMutableData()
        consumer = Quartz.CGDataConsumerCreateWithCFData(buf)
        attrString = AppKit.NSMutableAttributedString.alloc().initWithString_(
            "This is my delegate space"
        )

        AppKit.CFAttributedStringSetAttribute(
            attrString, (19, 1), CoreText.kCTRunDelegateAttributeName, delegate
        )

        for field in (None, "ascender", "descender", "width"):
            for missing in (True, False):
                with self.subTest(field=field):
                    path = Quartz.CGPathCreateMutable()
                    Quartz.CGPathAddRect(path, None, ((0, 0), (500, 400)))
                    context = Quartz.CGPDFContextCreate(consumer, None, None)
                    Quartz.CGPDFContextBeginPage(context, None)
                    Quartz.CGContextSetTextMatrix(
                        context, Quartz.CGAffineTransformIdentity
                    )
                    Quartz.CGContextSetTextPosition(context, 0, 0)

                    if field is not None:
                        cur = rc[field]
                        if missing:
                            del rc[field]
                        else:
                            rc[field] = None

                        v = CoreText.CTRunDelegateGetRefCon(delegate)

                        saved_stderr = sys.stderr
                        sys.stderr = str_io = io.StringIO()
                        try:
                            try:
                                frameSetter = (
                                    CoreText.CTFramesetterCreateWithAttributedString(
                                        attrString
                                    )
                                )
                                frame = CoreText.CTFramesetterCreateFrame(
                                    frameSetter, (0, len(attrString)), path, None
                                )
                                CoreText.CTFrameDraw(frame, context)
                                Quartz.CGPDFContextEndPage(context)
                            finally:
                                rc[field] = cur
                        finally:
                            sys.stderr = saved_stderr

                        stderr = str_io.getvalue()
                        self.assertIn(f"get{field[0].upper()}{field[1:]}", stderr)
                        if missing:
                            self.assertIn(f"KeyError: '{field}'", stderr)
                        else:
                            self.assertIn(
                                "ValueError: depythonifying 'double', got 'NoneType",
                                stderr,
                            )

                    else:
                        frameSetter = CoreText.CTFramesetterCreateWithAttributedString(
                            attrString
                        )
                        frame = CoreText.CTFramesetterCreateFrame(
                            frameSetter, (0, len(attrString)), path, None
                        )
                        CoreText.CTFrameDraw(frame, context)
                        Quartz.CGPDFContextEndPage(context)
