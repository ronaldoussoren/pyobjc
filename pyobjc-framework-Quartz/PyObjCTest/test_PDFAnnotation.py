
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotation (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(PDFAnnotation.shouldDisplay)
        self.assertArgIsBOOL(PDFAnnotation.setShouldDisplay_, 0)
        self.assertResultIsBOOL(PDFAnnotation.shouldPrint)
        self.assertArgIsBOOL(PDFAnnotation.setShouldPrint_, 0)
        self.assertResultIsBOOL(PDFAnnotation.hasAppearanceStream)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(PDFAnnotation.setValue_forAnnotationKey_)
        self.assertResultIsBOOL(PDFAnnotation.setBoolean_forAnnotationKey_)
        self.assertArgIsBOOL(PDFAnnotation.setBoolean_forAnnotationKey_, e)
        self.assertResultIsBOOL(PDFAnnotation.setRect_forAnnotationKey_)

    def testConstants(self):
        self.assertIsInstance(kPDFAnnotationKey_AppearanceDictionary, unicode)
        self.assertIsInstance(kPDFAnnotationKey_AppearanceState, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Border, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Color, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Contents, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Flags, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Date, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Name, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Page, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Rect, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Subtype, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Action, unicode)
        self.assertIsInstance(kPDFAnnotationKey_AdditionalActions, unicode)
        self.assertIsInstance(kPDFAnnotationKey_AppleExtras, unicode)
        self.assertIsInstance(kPDFAnnotationKey_BorderStyle, unicode)
        self.assertIsInstance(kPDFAnnotationKey_DefaultAppearance, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Destination, unicode)
        self.assertIsInstance(kPDFAnnotationKey_HighlightingMode, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Inklist, unicode)
        self.assertIsInstance(kPDFAnnotationKey_InteriorColor, unicode)
        self.assertIsInstance(kPDFAnnotationKey_LinePoints, unicode)
        self.assertIsInstance(kPDFAnnotationKey_LineEndingStyles, unicode)
        self.assertIsInstance(kPDFAnnotationKey_IconName, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Open, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Parent, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Popup, unicode)
        self.assertIsInstance(kPDFAnnotationKey_Quadding, unicode)
        self.assertIsInstance(kPDFAnnotationKey_QuadPoints, unicode)
        self.assertIsInstance(kPDFAnnotationKey_TextLabel, unicode)
        self.assertIsInstance(kPDFAnnotationKey_WidgetDefaultValue, unicode)
        self.assertIsInstance(kPDFAnnotationKey_WidgetFieldFlags, unicode)
        self.assertIsInstance(kPDFAnnotationKey_WidgetFieldType, unicode)
        self.assertIsInstance(kPDFAnnotationKey_WidgetAppearanceDictionary, unicode)
        self.assertIsInstance(kPDFAnnotationKey_WidgetMaxLen, unicode)
        self.assertIsInstance(kPDFAnnotationKey_WidgetOptions, unicode)
        self.assertIsInstance(kPDFAnnotationKey_WidgetTextLabelUI, unicode)
        self.assertIsInstance(kPDFAnnotationKey_WidgetValue, unicode)


if __name__ == "__main__":
    main()
