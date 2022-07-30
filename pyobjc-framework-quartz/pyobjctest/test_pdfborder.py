from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFBorder(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Quartz.PDFBorderKey, str)

    def test_enum_types(self):
        self.assertIsEnumType(Quartz.PDFBorderStyle)

    def testConstants(self):
        self.assertEqual(Quartz.kPDFBorderStyleSolid, 0)
        self.assertEqual(Quartz.kPDFBorderStyleDashed, 1)
        self.assertEqual(Quartz.kPDFBorderStyleBeveled, 2)
        self.assertEqual(Quartz.kPDFBorderStyleInset, 3)
        self.assertEqual(Quartz.kPDFBorderStyleUnderline, 4)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Quartz.PDFBorderKeyLineWidth, str)
        self.assertIsInstance(Quartz.PDFBorderKeyStyle, str)
        self.assertIsInstance(Quartz.PDFBorderKeyDashPattern, str)
