from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFPage(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Quartz.PDFDisplayBox)

    def testConstants(self):
        self.assertEqual(Quartz.kPDFDisplayBoxMediaBox, 0)
        self.assertEqual(Quartz.kPDFDisplayBoxCropBox, 1)
        self.assertEqual(Quartz.kPDFDisplayBoxBleedBox, 2)
        self.assertEqual(Quartz.kPDFDisplayBoxTrimBox, 3)
        self.assertEqual(Quartz.kPDFDisplayBoxArtBox, 4)

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsTypedEnum(Quartz.PDFPageImageInitializationOption, str)

        self.assertIsInstance(Quartz.PDFPageImageInitializationOptionMediaBox, str)
        self.assertIsInstance(Quartz.PDFPageImageInitializationOptionRotation, str)
        self.assertIsInstance(
            Quartz.PDFPageImageInitializationOptionUpscaleIfSmaller, str
        )
        self.assertIsInstance(
            Quartz.PDFPageImageInitializationOptionCompressionQuality, str
        )

    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFPage.displaysAnnotations)
        self.assertArgIsBOOL(Quartz.PDFPage.setDisplaysAnnotations_, 0)
