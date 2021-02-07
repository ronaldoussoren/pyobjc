from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFAnnotationUtilities(TestCase):
    def test_constants(self):
        self.assertEqual(Quartz.kPDFLineStyleNone, 0)
        self.assertEqual(Quartz.kPDFLineStyleSquare, 1)
        self.assertEqual(Quartz.kPDFLineStyleCircle, 2)
        self.assertEqual(Quartz.kPDFLineStyleDiamond, 3)
        self.assertEqual(Quartz.kPDFLineStyleOpenArrow, 4)
        self.assertEqual(Quartz.kPDFLineStyleClosedArrow, 5)

        self.assertEqual(Quartz.kPDFTextAnnotationIconComment, 0)
        self.assertEqual(Quartz.kPDFTextAnnotationIconKey, 1)
        self.assertEqual(Quartz.kPDFTextAnnotationIconNote, 2)
        self.assertEqual(Quartz.kPDFTextAnnotationIconHelp, 3)
        self.assertEqual(Quartz.kPDFTextAnnotationIconNewParagraph, 4)
        self.assertEqual(Quartz.kPDFTextAnnotationIconParagraph, 5)
        self.assertEqual(Quartz.kPDFTextAnnotationIconInsert, 6)

        self.assertEqual(Quartz.kPDFMarkupTypeHighlight, 0)
        self.assertEqual(Quartz.kPDFMarkupTypeStrikeOut, 1)
        self.assertEqual(Quartz.kPDFMarkupTypeUnderline, 2)
        self.assertEqual(Quartz.kPDFMarkupTypeRedact, 3)

        self.assertEqual(Quartz.kPDFWidgetUnknownControl, -1)
        self.assertEqual(Quartz.kPDFWidgetPushButtonControl, 0)
        self.assertEqual(Quartz.kPDFWidgetRadioButtonControl, 1)
        self.assertEqual(Quartz.kPDFWidgetCheckBoxControl, 2)

        self.assertEqual(Quartz.kPDFWidgetMixedState, -1)
        self.assertEqual(Quartz.kPDFWidgetOffState, 0)
        self.assertEqual(Quartz.kPDFWidgetOnState, 1)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Quartz.PDFAnnotationSubtypeText, str)
        self.assertIsInstance(Quartz.PDFAnnotationSubtypeLink, str)
        self.assertIsInstance(Quartz.PDFAnnotationSubtypeFreeText, str)
        self.assertIsInstance(Quartz.PDFAnnotationSubtypeLine, str)
        self.assertIsInstance(Quartz.PDFAnnotationSubtypeSquare, str)
        self.assertIsInstance(Quartz.PDFAnnotationSubtypeCircle, str)
        self.assertIsInstance(Quartz.PDFAnnotationSubtypeHighlight, str)
        self.assertIsInstance(Quartz.PDFAnnotationSubtypeUnderline, str)
        self.assertIsInstance(Quartz.PDFAnnotationSubtypeStrikeOut, str)
        self.assertIsInstance(Quartz.PDFAnnotationSubtypeInk, str)
        self.assertIsInstance(Quartz.PDFAnnotationSubtypeStamp, str)
        self.assertIsInstance(Quartz.PDFAnnotationSubtypePopup, str)
        self.assertIsInstance(Quartz.PDFAnnotationSubtypeWidget, str)
        self.assertIsInstance(Quartz.PDFAnnotationWidgetSubtypeButton, str)
        self.assertIsInstance(Quartz.PDFAnnotationWidgetSubtypeChoice, str)
        self.assertIsInstance(Quartz.PDFAnnotationWidgetSubtypeSignature, str)
        self.assertIsInstance(Quartz.PDFAnnotationWidgetSubtypeText, str)
        self.assertIsInstance(Quartz.PDFAnnotationLineEndingStyleNone, str)
        self.assertIsInstance(Quartz.PDFAnnotationLineEndingStyleSquare, str)
        self.assertIsInstance(Quartz.PDFAnnotationLineEndingStyleCircle, str)
        self.assertIsInstance(Quartz.PDFAnnotationLineEndingStyleDiamond, str)
        self.assertIsInstance(Quartz.PDFAnnotationLineEndingStyleOpenArrow, str)
        self.assertIsInstance(Quartz.PDFAnnotationLineEndingStyleClosedArrow, str)
        self.assertIsInstance(Quartz.PDFAnnotationTextIconTypeComment, str)
        self.assertIsInstance(Quartz.PDFAnnotationTextIconTypeKey, str)
        self.assertIsInstance(Quartz.PDFAnnotationTextIconTypeNote, str)
        self.assertIsInstance(Quartz.PDFAnnotationTextIconTypeHelp, str)
        self.assertIsInstance(Quartz.PDFAnnotationTextIconTypeNewParagraph, str)
        self.assertIsInstance(Quartz.PDFAnnotationTextIconTypeParagraph, str)
        self.assertIsInstance(Quartz.PDFAnnotationTextIconTypeInsert, str)
        self.assertIsInstance(Quartz.PDFAnnotationHighlightingModeNone, str)
        self.assertIsInstance(Quartz.PDFAnnotationHighlightingModeInvert, str)
        self.assertIsInstance(Quartz.PDFAnnotationHighlightingModeOutline, str)
        self.assertIsInstance(Quartz.PDFAnnotationHighlightingModePush, str)

    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotation.isMultiline)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setMultiline_, 0)

        self.assertResultIsBOOL(Quartz.PDFAnnotation.isPasswordField)

        self.assertResultIsBOOL(Quartz.PDFAnnotation.hasComb)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setComb_, 0)

        self.assertResultIsBOOL(Quartz.PDFAnnotation.allowsToggleToOff)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setAllowsToggleToOff_, 0)

        self.assertResultIsBOOL(Quartz.PDFAnnotation.radiosInUnison)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setRadiosInUnison_, 0)

        self.assertResultIsBOOL(Quartz.PDFAnnotation.isReadOnly)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setReadOnly_, 0)

        self.assertResultIsBOOL(Quartz.PDFAnnotation.isListChoice)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setListChoice_, 0)

        self.assertResultIsBOOL(Quartz.PDFAnnotation.isOpen)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setOpen_, 0)
