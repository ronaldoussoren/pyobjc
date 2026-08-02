from PyObjCTools.TestSupport import TestCase, expectedFailure
import Quartz
import pathlib


class TestCGPDFObject(TestCase):
    @expectedFailure
    def test_incomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPDFObject.h>")

    def test_constants(self):
        self.assertEqual(Quartz.kCGPDFObjectTypeNull, 1)
        self.assertEqual(Quartz.kCGPDFObjectTypeBoolean, 2)
        self.assertEqual(Quartz.kCGPDFObjectTypeInteger, 3)
        self.assertEqual(Quartz.kCGPDFObjectTypeReal, 4)
        self.assertEqual(Quartz.kCGPDFObjectTypeName, 5)
        self.assertEqual(Quartz.kCGPDFObjectTypeString, 6)
        self.assertEqual(Quartz.kCGPDFObjectTypeArray, 7)
        self.assertEqual(Quartz.kCGPDFObjectTypeDictionary, 8)
        self.assertEqual(Quartz.kCGPDFObjectTypeStream, 9)

    def test_functions(self):
        pdfFile = pathlib.Path(__file__).parent / "testdoc.pdf"
        self.assertTrue(pdfFile.is_file())

        pdf = Quartz.CGPDFDocumentCreateWithURL(pdfFile)
        self.assertIsNot(pdf, None)

        catalog = Quartz.CGPDFDocumentGetCatalog(pdf)
        self.assertIsNot(catalog, None)

        def save(key, value, context):
            context.append(value)

        saved_values = []
        Quartz.CGPDFDictionaryApplyFunction(catalog, save, saved_values)
        self.assertGreater(len(saved_values), 0)

        Quartz.CGPDFDictionaryApplyFunction(
            Quartz.CGPDFDocumentGetInfo(pdf), save, saved_values
        )

        for pnum in range(Quartz.CGPDFDocumentGetNumberOfPages(pdf)):
            page = Quartz.CGPDFDocumentGetPage(pdf, pnum)
            info = Quartz.CGPDFPageGetDictionary(page)
            Quartz.CGPDFDictionaryApplyFunction(info, save, saved_values)

        with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
            Quartz.CGPDFObjectGetValue()

        with self.assertRaisesRegex(
            TypeError, "Need instance of objc.CGPDFObject, got instance of int"
        ):
            Quartz.CGPDFObjectGetValue(42, 42, None)

        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            Quartz.CGPDFObjectGetValue(saved_values[0], "1", None)

        with self.assertRaisesRegex(ValueError, "Invalid object type"):
            Quartz.CGPDFObjectGetValue(saved_values[0], 300, None)

        with self.assertRaisesRegex(ValueError, "value must be None"):
            Quartz.CGPDFObjectGetValue(
                saved_values[0], Quartz.CGPDFObjectGetType(saved_values[0]), 42
            )

        for value in saved_values:
            tp = Quartz.CGPDFObjectGetType(value)
            self.assertIsInstance(tp, int)

            ok, value = Quartz.CGPDFObjectGetValue(value, tp, None)
            match tp:
                case Quartz.kCGPDFObjectTypeNull:
                    self.assertFalse(ok)
                    self.assertIs(value, None)
                case Quartz.kCGPDFObjectTypeBoolean:
                    self.assertTrue(ok)
                    self.assertIsInstance(value, bool)
                case Quartz.kCGPDFObjectTypeString:
                    self.assertTrue(ok)
                    self.assertIsInstance(value, str)
                case Quartz.kCGPDFObjectTypeName:
                    self.assertTrue(ok)
                    self.assertIsInstance(value, str)
                case Quartz.kCGPDFObjectTypeArray:
                    self.assertTrue(ok)
                    self.assertIsInstance(value, Quartz.CGPDFArrayRef)
                case Quartz.kCGPDFObjectTypeDictionary:
                    self.assertTrue(ok)
                    self.assertIsInstance(value, Quartz.CGPDFDictionaryRef)
                case Quartz.kCGPDFObjectTypeStream:
                    self.assertTrue(ok)
                    self.assertIsInstance(value, Quartz.CGPDFStreamRef)
