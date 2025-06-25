from PyObjCTools.TestSupport import TestCase, min_os_level
import sys
import Quartz


class TestPDFPage(TestCase):
    def testConstants(self):
        self.assertIsEnumType(Quartz.PDFDisplayBox)
        self.assertEqual(Quartz.kPDFDisplayBoxMediaBox, 0)
        self.assertEqual(Quartz.kPDFDisplayBoxCropBox, 1)
        self.assertEqual(Quartz.kPDFDisplayBoxBleedBox, 2)
        self.assertEqual(Quartz.kPDFDisplayBoxTrimBox, 3)
        self.assertEqual(Quartz.kPDFDisplayBoxArtBox, 4)

        self.assertIsEnumType(Quartz.PDFAreaOfInterest)
        self.assertEqual(Quartz.kPDFNoArea, 0)
        self.assertEqual(Quartz.kPDFPageArea, 1 << 0)
        self.assertEqual(Quartz.kPDFTextArea, 1 << 1)
        self.assertEqual(Quartz.kPDFAnnotationArea, 1 << 2)
        self.assertEqual(Quartz.kPDFLinkArea, 1 << 3)
        self.assertEqual(Quartz.kPDFControlArea, 1 << 4)
        self.assertEqual(Quartz.kPDFTextFieldArea, 1 << 5)
        self.assertEqual(Quartz.kPDFIconArea, 1 << 6)
        self.assertEqual(Quartz.kPDFPopupArea, 1 << 7)
        self.assertEqual(Quartz.kPDFImageArea, 1 << 8)
        self.assertEqual(Quartz.kPDFAnyArea, sys.maxsize)

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
