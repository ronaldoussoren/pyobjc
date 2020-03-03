import PrintCore
import objc
from PyObjCTools.TestSupport import TestCase


class TestPMDefinitions(TestCase):
    def test_constants(self):
        self.assertEqual(PrintCore.kPMCancel, 0x0080)

        self.assertIs(PrintCore.kPMNoData, objc.NULL)
        self.assertIs(PrintCore.kPMDontWantSize, objc.NULL)
        self.assertIs(PrintCore.kPMDontWantData, objc.NULL)
        self.assertIs(PrintCore.kPMDontWantBoolean, objc.NULL)
        self.assertIs(PrintCore.kPMNoReference, objc.NULL)

        self.assertIs(PrintCore.kPMDuplexDefault, PrintCore.kPMDuplexNone)
        self.assertIs(PrintCore.kPMNoPrintSettings, None)
        self.assertIs(PrintCore.kPMNoPageFormat, None)
        self.assertIs(PrintCore.kPMServerLocal, None)

        self.assertEqual(PrintCore.kPMDestinationInvalid, 0)
        self.assertEqual(PrintCore.kPMDestinationPrinter, 1)
        self.assertEqual(PrintCore.kPMDestinationFile, 2)
        self.assertEqual(PrintCore.kPMDestinationFax, 3)
        self.assertEqual(PrintCore.kPMDestinationPreview, 4)
        self.assertEqual(PrintCore.kPMDestinationProcessPDF, 5)

        self.assertEqual(PrintCore.kPMPortrait, 1)
        self.assertEqual(PrintCore.kPMLandscape, 2)
        self.assertEqual(PrintCore.kPMReversePortrait, 3)
        self.assertEqual(PrintCore.kPMReverseLandscape, 4)

        self.assertEqual(PrintCore.kPMPrinterIdle, 3)
        self.assertEqual(PrintCore.kPMPrinterProcessing, 4)
        self.assertEqual(PrintCore.kPMPrinterStopped, 5)

        self.assertEqual(PrintCore.kPMUnknownColorSpaceModel, 0)
        self.assertEqual(PrintCore.kPMGrayColorSpaceModel, 1)
        self.assertEqual(PrintCore.kPMRGBColorSpaceModel, 2)
        self.assertEqual(PrintCore.kPMCMYKColorSpaceModel, 3)
        self.assertEqual(PrintCore.kPMDevNColorSpaceModel, 4)

        self.assertEqual(PrintCore.kPMColorSpaceModelCount, 4)

        self.assertEqual(PrintCore.kPMQualityLowest, 0x0000)
        self.assertEqual(PrintCore.kPMQualityInkSaver, 0x0001)
        self.assertEqual(PrintCore.kPMQualityDraft, 0x0004)
        self.assertEqual(PrintCore.kPMQualityNormal, 0x0008)
        self.assertEqual(PrintCore.kPMQualityPhoto, 0x000B)
        self.assertEqual(PrintCore.kPMQualityBest, 0x000D)
        self.assertEqual(PrintCore.kPMQualityHighest, 0x000F)

        self.assertEqual(PrintCore.kPMPaperTypeUnknown, 0x0000)
        self.assertEqual(PrintCore.kPMPaperTypePlain, 0x0001)
        self.assertEqual(PrintCore.kPMPaperTypeCoated, 0x0002)
        self.assertEqual(PrintCore.kPMPaperTypePremium, 0x0003)
        self.assertEqual(PrintCore.kPMPaperTypeGlossy, 0x0004)
        self.assertEqual(PrintCore.kPMPaperTypeTransparency, 0x0005)
        self.assertEqual(PrintCore.kPMPaperTypeTShirt, 0x0006)

        self.assertEqual(PrintCore.kPMScalingPinTopLeft, 1)
        self.assertEqual(PrintCore.kPMScalingPinTopRight, 2)
        self.assertEqual(PrintCore.kPMScalingPinBottomLeft, 3)
        self.assertEqual(PrintCore.kPMScalingPinBottomRight, 4)
        self.assertEqual(PrintCore.kPMScalingCenterOnPaper, 5)
        self.assertEqual(PrintCore.kPMScalingCenterOnImgArea, 6)

        self.assertEqual(PrintCore.kPMDuplexNone, 0x0001)
        self.assertEqual(PrintCore.kPMDuplexNoTumble, 0x0002)
        self.assertEqual(PrintCore.kPMDuplexTumble, 0x0003)
        self.assertEqual(PrintCore.kPMSimplexTumble, 0x0004)

        self.assertEqual(PrintCore.kPMLayoutLeftRightTopBottom, 1)
        self.assertEqual(PrintCore.kPMLayoutLeftRightBottomTop, 2)
        self.assertEqual(PrintCore.kPMLayoutRightLeftTopBottom, 3)
        self.assertEqual(PrintCore.kPMLayoutRightLeftBottomTop, 4)
        self.assertEqual(PrintCore.kPMLayoutTopBottomLeftRight, 5)
        self.assertEqual(PrintCore.kPMLayoutTopBottomRightLeft, 6)
        self.assertEqual(PrintCore.kPMLayoutBottomTopLeftRight, 7)
        self.assertEqual(PrintCore.kPMLayoutBottomTopRightLeft, 8)

        self.assertEqual(PrintCore.kPMBorderSingleHairline, 1)
        self.assertEqual(PrintCore.kPMBorderDoubleHairline, 2)
        self.assertEqual(PrintCore.kPMBorderSingleThickline, 3)
        self.assertEqual(PrintCore.kPMBorderDoubleThickline, 4)

        self.assertEqual(PrintCore.kPMHideInlineItems, 0 << 0)
        self.assertEqual(PrintCore.kPMShowDefaultInlineItems, 1 << 15)
        self.assertEqual(PrintCore.kPMShowInlineCopies, 1 << 0)
        self.assertEqual(PrintCore.kPMShowInlinePageRange, 1 << 1)
        self.assertEqual(PrintCore.kPMShowInlinePageRangeWithSelection, 1 << 6)
        self.assertEqual(PrintCore.kPMShowInlinePaperSize, 1 << 2)
        self.assertEqual(PrintCore.kPMShowInlineOrientation, 1 << 3)
        self.assertEqual(PrintCore.kPMShowInlineScale, 1 << 7)
        self.assertEqual(PrintCore.kPMShowPageAttributesPDE, 1 << 8)

        self.assertEqual(PrintCore.kAllPPDDomains, 1)
        self.assertEqual(PrintCore.kSystemPPDDomain, 2)
        self.assertEqual(PrintCore.kLocalPPDDomain, 3)
        self.assertEqual(PrintCore.kNetworkPPDDomain, 4)
        self.assertEqual(PrintCore.kUserPPDDomain, 5)
        self.assertEqual(PrintCore.kCUPSPPDDomain, 6)

        self.assertEqual(PrintCore.kPMPPDDescriptionType, "PMPPDDescriptionType")
        self.assertEqual(
            PrintCore.kPMDocumentFormatDefault, "com.apple.documentformat.default"
        )
        self.assertEqual(PrintCore.kPMDocumentFormatPDF, "application/pdf")
        self.assertEqual(
            PrintCore.kPMDocumentFormatPostScript, "application/postscript"
        )
        self.assertEqual(
            PrintCore.kPMGraphicsContextDefault, "com.apple.graphicscontext.default"
        )
        self.assertEqual(
            PrintCore.kPMGraphicsContextCoreGraphics,
            "com.apple.graphicscontext.coregraphics",
        )
        self.assertEqual(PrintCore.kPDFWorkflowItemURLKey, "itemURL")
        self.assertEqual(PrintCore.kPDFWorkflowDisplayNameKey, "displayName")
        self.assertEqual(PrintCore.kPDFWorkflowItemsKey, "items")
        self.assertEqual(PrintCore.kPDFWorkflowModifiedKey, "wasModifiedInline")
        self.assertEqual(
            PrintCore.kPMPrintSelectionTitleKey, "com.apple.printSelection.title"
        )

        self.assertEqual(PrintCore.kPMNoError, 0)
        self.assertEqual(PrintCore.kPMGeneralError, -30870)
        self.assertEqual(PrintCore.kPMOutOfScope, -30871)
        self.assertEqual(PrintCore.kPMInvalidParameter, -50)
        self.assertEqual(PrintCore.kPMNoDefaultPrinter, -30872)
        self.assertEqual(PrintCore.kPMNotImplemented, -30873)
        self.assertEqual(PrintCore.kPMNoSuchEntry, -30874)
        self.assertEqual(PrintCore.kPMInvalidPrintSettings, -30875)
        self.assertEqual(PrintCore.kPMInvalidPageFormat, -30876)
        self.assertEqual(PrintCore.kPMValueOutOfRange, -30877)
        self.assertEqual(PrintCore.kPMLockIgnored, -30878)

        self.assertEqual(PrintCore.kPMInvalidPrintSession, -30879)
        self.assertEqual(PrintCore.kPMInvalidPrinter, -30880)
        self.assertEqual(PrintCore.kPMObjectInUse, -30881)
        self.assertEqual(PrintCore.kPMInvalidPreset, -30899)

        self.assertEqual(PrintCore.kPMPrintAllPages, -1)

        self.assertEqual(PrintCore.kPMUnlocked, 0)

        self.assertEqual(PrintCore.kPMDataFormatXMLDefault, 0)
        self.assertEqual(PrintCore.kPMDataFormatXMLMinimal, 1)
        self.assertEqual(PrintCore.kPMDataFormatXMLCompressed, 2)

        self.assertEqual(
            PrintCore.kPMPresetGraphicsTypeKey, "com.apple.print.preset.graphicsType"
        )
        self.assertEqual(PrintCore.kPMPresetGraphicsTypePhoto, "Photo")
        self.assertEqual(PrintCore.kPMPresetGraphicsTypeAll, "All")
        self.assertEqual(PrintCore.kPMPresetGraphicsTypeGeneral, "General")
        self.assertEqual(PrintCore.kPMPresetGraphicsTypeNone, "None")

    def test_structs(self):
        v = PrintCore.PMRect()
        self.assertIsInstance(v.top, float)
        self.assertIsInstance(v.left, float)
        self.assertIsInstance(v.bottom, float)
        self.assertIsInstance(v.right, float)

        v = PrintCore.PMResolution()
        self.assertIsInstance(v.hRes, float)
        self.assertIsInstance(v.vRes, float)

        v = PrintCore.PMLanguageInfo()
        self.assertIs(v.level, None)
        self.assertIs(v.version, None)
        self.assertIs(v.release, None)
