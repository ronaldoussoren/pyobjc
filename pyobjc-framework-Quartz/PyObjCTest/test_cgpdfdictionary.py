from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import os
import pathlib


class TestCGPDFDictionary(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(Quartz.CGPDFDictionaryRef)

    def assertIsPDFGetter(self, function):
        self.assertArgIsIn(function, 1)
        self.assertArgIsNullTerminated(function, 1)
        self.assertArgIsOut(function, 2)

    def test_incomplete(self):
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetObject)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetBoolean)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetInteger)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetNumber)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetName)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetString)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetArray)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetDictionary)
        self.assertIsPDFGetter(Quartz.CGPDFDictionaryGetStream)

        pdfFile = "/System/Library/ProductDocuments/ProductGuides/ENERGY STAR.pdf"
        self.assertTrue(os.path.isfile(pdfFile))

        pdf = Quartz.CGPDFDocumentCreateWithURL(pathlib.Path(pdfFile))
        self.assertIsNot(pdf, None)

        catalog = Quartz.CGPDFDocumentGetCatalog(pdf)
        self.assertIsNot(catalog, None)

        context = {}

        def applier(key, value, context):
            context[key] = value

        def applier_raises(key, value, context):
            raise RuntimeError("callback error")

        with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
            Quartz.CGPDFDictionaryApplyFunction()

        with self.assertRaisesRegex(
            TypeError, "Need instance of objc.CGPDFDictionaryRef, got instance of int"
        ):
            Quartz.CGPDFDictionaryApplyFunction(42, applier, context)

        with self.assertRaisesRegex(TypeError, "callback not callable"):
            Quartz.CGPDFDictionaryApplyFunction(catalog, 42, context)

        Quartz.CGPDFDictionaryApplyFunction(catalog, applier, context)

        self.assertGreater(len(context), 0)
        for key, _value in context.items():
            self.assertIsInstance(key, bytes)

        with self.assertRaisesRegex(RuntimeError, "callback error"):
            Quartz.CGPDFDictionaryApplyFunction(catalog, applier_raises, context)

    def test_functions(self):
        Quartz.CGPDFDictionaryGetCount

    @min_os_level("10.14")
    def test_functions10_14(self):
        self.assertArgIsBlock(
            Quartz.CGPDFDictionaryApplyBlock, 1, b"vn^t^{CGPDFObject=}^v"
        )
