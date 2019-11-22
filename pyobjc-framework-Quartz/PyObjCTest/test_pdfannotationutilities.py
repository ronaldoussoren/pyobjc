from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *


class TestPDFAnnotationUtilities(TestCase):
    def test_constants(self):
        self.assertEqual(kPDFLineStyleNone, 0)
        self.assertEqual(kPDFLineStyleSquare, 1)
        self.assertEqual(kPDFLineStyleCircle, 2)
        self.assertEqual(kPDFLineStyleDiamond, 3)
        self.assertEqual(kPDFLineStyleOpenArrow, 4)
        self.assertEqual(kPDFLineStyleClosedArrow, 5)

        self.assertEqual(kPDFTextAnnotationIconComment, 0)
        self.assertEqual(kPDFTextAnnotationIconKey, 1)
        self.assertEqual(kPDFTextAnnotationIconNote, 2)
        self.assertEqual(kPDFTextAnnotationIconHelp, 3)
        self.assertEqual(kPDFTextAnnotationIconNewParagraph, 4)
        self.assertEqual(kPDFTextAnnotationIconParagraph, 5)
        self.assertEqual(kPDFTextAnnotationIconInsert, 6)

        self.assertEqual(kPDFMarkupTypeHighlight, 0)
        self.assertEqual(kPDFMarkupTypeStrikeOut, 1)
        self.assertEqual(kPDFMarkupTypeUnderline, 2)

        self.assertEqual(kPDFWidgetUnknownControl, -1)
        self.assertEqual(kPDFWidgetPushButtonControl, 0)
        self.assertEqual(kPDFWidgetRadioButtonControl, 1)
        self.assertEqual(kPDFWidgetCheckBoxControl, 2)

        self.assertEqual(kPDFWidgetMixedState, -1)
        self.assertEqual(kPDFWidgetOffState, 0)
        self.assertEqual(kPDFWidgetOnState, 1)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(PDFAnnotationSubtypeText, unicode)
        self.assertIsInstance(PDFAnnotationSubtypeLink, unicode)
        self.assertIsInstance(PDFAnnotationSubtypeFreeText, unicode)
        self.assertIsInstance(PDFAnnotationSubtypeLine, unicode)
        self.assertIsInstance(PDFAnnotationSubtypeSquare, unicode)
        self.assertIsInstance(PDFAnnotationSubtypeCircle, unicode)
        self.assertIsInstance(PDFAnnotationSubtypeHighlight, unicode)
        self.assertIsInstance(PDFAnnotationSubtypeUnderline, unicode)
        self.assertIsInstance(PDFAnnotationSubtypeStrikeOut, unicode)
        self.assertIsInstance(PDFAnnotationSubtypeInk, unicode)
        self.assertIsInstance(PDFAnnotationSubtypeStamp, unicode)
        self.assertIsInstance(PDFAnnotationSubtypePopup, unicode)
        self.assertIsInstance(PDFAnnotationSubtypeWidget, unicode)
        self.assertIsInstance(PDFAnnotationWidgetSubtypeButton, unicode)
        self.assertIsInstance(PDFAnnotationWidgetSubtypeChoice, unicode)
        self.assertIsInstance(PDFAnnotationWidgetSubtypeSignature, unicode)
        self.assertIsInstance(PDFAnnotationWidgetSubtypeText, unicode)
        self.assertIsInstance(PDFAnnotationLineEndingStyleNone, unicode)
        self.assertIsInstance(PDFAnnotationLineEndingStyleSquare, unicode)
        self.assertIsInstance(PDFAnnotationLineEndingStyleCircle, unicode)
        self.assertIsInstance(PDFAnnotationLineEndingStyleDiamond, unicode)
        self.assertIsInstance(PDFAnnotationLineEndingStyleOpenArrow, unicode)
        self.assertIsInstance(PDFAnnotationLineEndingStyleClosedArrow, unicode)
        self.assertIsInstance(PDFAnnotationTextIconTypeComment, unicode)
        self.assertIsInstance(PDFAnnotationTextIconTypeKey, unicode)
        self.assertIsInstance(PDFAnnotationTextIconTypeNote, unicode)
        self.assertIsInstance(PDFAnnotationTextIconTypeHelp, unicode)
        self.assertIsInstance(PDFAnnotationTextIconTypeNewParagraph, unicode)
        self.assertIsInstance(PDFAnnotationTextIconTypeParagraph, unicode)
        self.assertIsInstance(PDFAnnotationTextIconTypeInsert, unicode)
        self.assertIsInstance(PDFAnnotationHighlightingModeNone, unicode)
        self.assertIsInstance(PDFAnnotationHighlightingModeInvert, unicode)
        self.assertIsInstance(PDFAnnotationHighlightingModeOutline, unicode)
        self.assertIsInstance(PDFAnnotationHighlightingModePush, unicode)

    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(PDFAnnotation.isMultiline)
        self.assertArgIsBOOL(PDFAnnotation.setMultiline_, 0)

        self.assertResultIsBOOL(PDFAnnotation.isPasswordField)

        self.assertResultIsBOOL(PDFAnnotation.hasComb)
        self.assertArgIsBOOL(PDFAnnotation.setComb_, 0)

        self.assertResultIsBOOL(PDFAnnotation.allowsToggleToOff)
        self.assertArgIsBOOL(PDFAnnotation.setAllowsToggleToOff_, 0)

        self.assertResultIsBOOL(PDFAnnotation.radiosInUnison)
        self.assertArgIsBOOL(PDFAnnotation.setRadiosInUnison_, 0)

        self.assertResultIsBOOL(PDFAnnotation.isReadOnly)
        self.assertArgIsBOOL(PDFAnnotation.setReadOnly_, 0)

        self.assertResultIsBOOL(PDFAnnotation.isListChoice)
        self.assertArgIsBOOL(PDFAnnotation.setListChoice_, 0)

        self.assertResultIsBOOL(PDFAnnotation.isOpen)
        self.assertArgIsBOOL(PDFAnnotation.setOpen_, 0)


if __name__ == "__main__":
    main()
