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
        # pdfFile = pathlib.Path("/System/Library/ProductDocuments/ProductGuides/ENERGY STAR.pdf")

        self.assertTrue(pdfFile.is_file())

        pdf = Quartz.CGPDFDocumentCreateWithURL(pdfFile)
        self.assertIsNot(pdf, None)

        catalog = Quartz.CGPDFDocumentGetCatalog(pdf)
        self.assertIsNot(catalog, None)

        def save(key, value, context):
            context.append((key, value))

        saved_values = []
        Quartz.CGPDFDictionaryApplyFunction(catalog, save, saved_values)
        self.assertGreater(len(saved_values), 0)

        Quartz.CGPDFDictionaryApplyFunction(
            Quartz.CGPDFDocumentGetInfo(pdf), save, saved_values
        )

        pages = []
        infos = []
        for pnum in range(1, Quartz.CGPDFDocumentGetNumberOfPages(pdf) + 1):
            page = Quartz.CGPDFDocumentGetPage(pdf, pnum)
            pages.append(page)
            info = Quartz.CGPDFPageGetDictionary(page)
            infos.append(info)
            Quartz.CGPDFDictionaryApplyFunction(info, save, saved_values)

            # XXX: CGPDFContentStreamGetStreams can get at more information,
            #      but returns a CFArrayRef with embedded CGPDF* values,
            #      which aren't instances of a CF type-> needs manual binding.

        with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
            Quartz.CGPDFObjectGetValue()

        with self.assertRaisesRegex(
            TypeError, "Need instance of objc.CGPDFObject, got instance of int"
        ):
            Quartz.CGPDFObjectGetValue(42, 42, None)

        self.assertIsNot(pdf, None)
        test_value = None
        for _key, value in saved_values:
            if value is None:
                continue
            test_value = value
            tp = Quartz.CGPDFObjectGetType(value)
            self.assertIsInstance(tp, int)

            ok, v = Quartz.CGPDFObjectGetValue(value, tp, None)
            match tp:
                case Quartz.kCGPDFObjectTypeNull:
                    self.assertFalse(ok)
                    self.assertIs(v, None)
                case Quartz.kCGPDFObjectTypeBoolean:
                    self.assertTrue(ok)
                    self.assertIsInstance(v, bool)
                case Quartz.kCGPDFObjectTypeString:
                    self.assertTrue(ok)
                    self.assertIsInstance(v, Quartz.CGPDFStringRef)
                    o = Quartz.CGPDFStringCopyTextString(v)
                    self.assertIsInstance(o, str)
                case Quartz.kCGPDFObjectTypeName:
                    self.assertTrue(ok)
                    self.assertIsInstance(v, str)
                case Quartz.kCGPDFObjectTypeArray:
                    self.assertTrue(ok)
                    self.assertIsInstance(v, Quartz.CGPDFArrayRef)
                case Quartz.kCGPDFObjectTypeDictionary:
                    self.assertTrue(ok)
                    self.assertIsInstance(v, Quartz.CGPDFDictionaryRef)
                case Quartz.kCGPDFObjectTypeStream:
                    self.assertTrue(ok)
                    self.assertIsInstance(v, Quartz.CGPDFStreamRef)
            # print(_key, tp, ok, v)

        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            Quartz.CGPDFObjectGetValue(test_value, "1", None)

        with self.assertRaisesRegex(ValueError, "Invalid object type"):
            Quartz.CGPDFObjectGetValue(test_value, 300, None)

        with self.assertRaisesRegex(ValueError, "value must be None"):
            Quartz.CGPDFObjectGetValue(
                test_value, Quartz.CGPDFObjectGetType(saved_values[0][1]), 42
            )
