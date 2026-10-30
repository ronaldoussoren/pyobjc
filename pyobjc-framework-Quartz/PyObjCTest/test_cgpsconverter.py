from PyObjCTools.TestSupport import TestCase, NoObjCClass
import objc
import Quartz
import Foundation

PS_DATA = b"""\
%!PS-Adobe-3.0
%%Title: Multi-page Hand-Written Example
%%Pages: 2
%%BoundingBox: 0 0 612 792
%%EndComments

%%Page: i 1
%%BeginPageSetup
/Helvetica findfont 24 scalefont setfont
%%EndPageSetup
306 400 moveto
(This is Page 1) stringwidth pop 2 div neg 0 rmoveto
(This is Page 1) show
206 300 moveto
200 0 rlineto
0 -100 rlineto
-200 0 rlineto
closepath
stroke

showpage

%%Page: ii 2
%%BeginPageSetup
/Helvetica findfont 24 scalefont setfont
%%EndPageSetup
306 400 moveto
(This is Page 2) stringwidth pop 2 div neg 0 rmoveto
(This is Page 2) show
306 320 moveto
100 -100 lineto
206 220 lineto
closepath
stroke

showpage

%%EOF
"""


class TestCGPSConverter(TestCase):
    def test_constants(self):
        self.assertNotHasAttr(Quartz, "CGPSConverterCallbacks")

    def test_types(self):
        self.assertIsSubclass(Quartz.CGPSConverterRef, objc.objc_object)

    def test_functions(self):
        self.assertIsInstance(Quartz.CGPSConverterGetTypeID(), int)

        self.assertResultIsBOOL(Quartz.CGPSConverterAbort)
        self.assertResultIsBOOL(Quartz.CGPSConverterIsConverting)

        self.assertResultIsCFRetained(Quartz.CGPSConverterCreate)

        with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
            Quartz.CGPSConverterCreate()

        with self.assertRaisesRegex(TypeError, "callbacks must be tuple of length 7"):
            Quartz.CGPSConverterCreate(42, None, {})

        with self.assertRaisesRegex(TypeError, "beginDocument not callable or None"):
            Quartz.CGPSConverterCreate(
                42, (42, None, None, None, None, None, None), NoObjCClass()
            )

        with self.assertRaisesRegex(TypeError, "endDocument not callable or None"):
            Quartz.CGPSConverterCreate(
                42, (None, 42, None, None, None, None, None), NoObjCClass()
            )

        with self.assertRaisesRegex(TypeError, "beginPage not callable or None"):
            Quartz.CGPSConverterCreate(
                42, (None, None, 42, None, None, None, None), NoObjCClass()
            )

        with self.assertRaisesRegex(TypeError, "endPage not callable or None"):
            Quartz.CGPSConverterCreate(
                42, (None, None, None, 42, None, None, None), NoObjCClass()
            )

        with self.assertRaisesRegex(TypeError, "noteProgress not callable or None"):
            Quartz.CGPSConverterCreate(
                42, (None, None, None, None, 42, None, None), NoObjCClass()
            )

        with self.assertRaisesRegex(TypeError, "noteMessage not callable or None"):
            Quartz.CGPSConverterCreate(
                42, (None, None, None, None, None, 42, None), NoObjCClass()
            )

        with self.assertRaisesRegex(TypeError, "releaseInfo not callable or None"):
            Quartz.CGPSConverterCreate(
                42, (None, None, None, None, None, None, 42), NoObjCClass()
            )

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            Quartz.CGPSConverterCreate(
                42, (None, None, None, None, None, None, None), NoObjCClass()
            )

        lst = []

        def beginDocument(info):
            lst.append(("begin-document", info))

        def endDocument(info, ok):
            lst.append(("end-document", info, ok))

        def beginPage(info, pageNumber, pageInfo):
            lst.append(("begin-page", info, pageNumber, pageInfo))

        def endPage(info, pageNumber, pageInfo):
            lst.append(("end-page", info, pageNumber, pageInfo))

        def noteProgress(info):
            lst.append(("progress", info))

        def noteMessage(info, message):
            lst.append(("message", info, message))

        def releaseInfo(info):
            lst.append(("release-info", info))

        context = object()
        conv = Quartz.CGPSConverterCreate(
            context,
            (
                beginDocument,
                endDocument,
                beginPage,
                endPage,
                noteProgress,
                noteMessage,
                releaseInfo,
            ),
            None,
        )
        self.assertIsInstance(conv, Quartz.CGPSConverterRef)

        inputData = Quartz.CGDataProviderCreateWithCFData(
            PS_DATA.replace(b"\n", b"\r\n")
        )
        buf = Foundation.NSMutableData.data()
        outputData = Quartz.CGDataConsumerCreateWithCFData(buf)

        ok = Quartz.CGPSConverterConvert(conv, inputData, outputData, None)
        self.assertIs(ok, True)

        del conv

        # XXX: For some reason the begin-page and end-page callbacks are never invoked (macOS 26)
        self.assertEqual(
            lst,
            [
                ("begin-document", context),
                ("end-document", context, True),
                ("release-info", context),
            ],
        )
