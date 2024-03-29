from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFAnnotation(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Quartz.PDFAnnotationKey, str)
        self.assertIsTypedEnum(Quartz.PDFAnnotationSubtype, str)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotation.allowsToggleToOff)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setAllowsToggleToOff_, 0)
        self.assertResultIsBOOL(Quartz.PDFAnnotation.radiosInUnison)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setRadiosInUnison_, 0)
        self.assertResultIsBOOL(Quartz.PDFAnnotation.isReadOnly)
        # self.assertArgIsBOOL(Quartz.PDFAnnotation.setReadOnly_, 0)
        self.assertResultIsBOOL(Quartz.PDFAnnotation.isListChoice)
        # self.assertArgIsBOOL(Quartz.PDFAnnotation.setListChoice_, 0)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_AppearanceDictionary, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_AppearanceState, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Border, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Color, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Contents, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Flags, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Date, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Name, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Page, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Rect, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Subtype, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Action, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_AdditionalActions, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_BorderStyle, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_DefaultAppearance, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Destination, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_HighlightingMode, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Inklist, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_InteriorColor, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_LinePoints, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_LineEndingStyles, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_IconName, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Open, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Parent, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Popup, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_Quadding, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_QuadPoints, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_TextLabel, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_WidgetDefaultValue, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_WidgetFieldFlags, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_WidgetFieldType, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_WidgetAppearanceDictionary, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_WidgetMaxLen, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_WidgetOptions, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_WidgetTextLabelUI, str)
        self.assertIsInstance(Quartz.kPDFAnnotationKey_WidgetValue, str)

        # Not present in most recent SDK:
        # self.assertIsInstance(Quartz.kPDFAnnotationKey_AppleExtras, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Quartz.PDFAnnotationKeyAppearanceDictionary, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyAppearanceState, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyBorder, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyColor, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyContents, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyFlags, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyDate, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyName, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyPage, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyRect, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeySubtype, str)

        self.assertIsInstance(Quartz.PDFAnnotationKeyAction, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyAdditionalActions, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyBorderStyle, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyDefaultAppearance, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyDestination, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyHighlightingMode, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyInklist, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyInteriorColor, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyLinePoints, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyLineEndingStyles, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyIconName, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyOpen, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyParent, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyPopup, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyQuadding, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyQuadPoints, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyTextLabel, str)

        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetDownCaption, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetBorderColor, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetBackgroundColor, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetCaption, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetDefaultValue, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetFieldFlags, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetFieldType, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetAppearanceDictionary, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetMaxLen, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetOptions, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetRotation, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetRolloverCaption, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetTextLabelUI, str)
        self.assertIsInstance(Quartz.PDFAnnotationKeyWidgetValue, str)

    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotation.shouldDisplay)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setShouldDisplay_, 0)
        self.assertResultIsBOOL(Quartz.PDFAnnotation.shouldPrint)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setShouldPrint_, 0)
        self.assertResultIsBOOL(Quartz.PDFAnnotation.hasAppearanceStream)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotation.setValue_forAnnotationKey_)
        self.assertResultIsBOOL(Quartz.PDFAnnotation.setBoolean_forAnnotationKey_)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setBoolean_forAnnotationKey_, 0)
        self.assertResultIsBOOL(Quartz.PDFAnnotation.setRect_forAnnotationKey_)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotation.isPasswordField)
        # self.assertArgIsBOOL(Quartz.PDFAnnotation.setIsPasswordField_, 0)
        self.assertResultIsBOOL(Quartz.PDFAnnotation.isMultiline)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setMultiline_, 0)
        self.assertResultIsBOOL(Quartz.PDFAnnotation.isHighlighted)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setHighlighted_, 0)
        self.assertResultIsBOOL(Quartz.PDFAnnotation.hasComb)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setComb_, 0)
        self.assertResultIsBOOL(Quartz.PDFAnnotation.isOpen)
        self.assertArgIsBOOL(Quartz.PDFAnnotation.setOpen_, 0)
