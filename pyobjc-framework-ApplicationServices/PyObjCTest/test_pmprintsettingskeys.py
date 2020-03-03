import PrintCore
from PyObjCTools.TestSupport import TestCase


class TestPMPrintSettingsKeys(TestCase):
    def test_constants(self):
        self.assertEqual(
            PrintCore.kPMCopiesStr, b"com.apple.print.PrintSettings.PMCopies"
        )
        self.assertEqual(PrintCore.kPMCopiesKey, PrintCore.kPMCopiesStr.decode("utf-8"))

        self.assertEqual(
            PrintCore.kPMCopyCollateStr, b"com.apple.print.PrintSettings.PMCopyCollate"
        )
        self.assertEqual(
            PrintCore.kPMCopyCollateKey, PrintCore.kPMCopyCollateStr.decode("utf-8")
        )

        self.assertEqual(PrintCore.kPMOutputOrderStr, b"OutputOrder")
        self.assertEqual(
            PrintCore.kPMOutputOrderKey, PrintCore.kPMOutputOrderStr.decode("utf-8")
        )

        self.assertEqual(PrintCore.kPMPageSetStr, b"page-set")
        self.assertEqual(
            PrintCore.kPMPageSetKey, PrintCore.kPMPageSetStr.decode("utf-8")
        )

        self.assertEqual(PrintCore.kPMMirrorStr, b"mirror")
        self.assertEqual(PrintCore.kPMMirrorKey, PrintCore.kPMMirrorStr.decode("utf-8"))

        self.assertEqual(
            PrintCore.kPMPrintSelectionOnlyStr,
            b"com.apple.print.PrintSettings.PMPrintSelectionOnly",
        )
        self.assertEqual(
            PrintCore.kPMPrintSelectionOnlyKey,
            PrintCore.kPMPrintSelectionOnlyStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMBorderStr, b"com.apple.print.PrintSettings.PMBorder"
        )
        self.assertEqual(PrintCore.kPMBorderKey, PrintCore.kPMBorderStr.decode("utf-8"))

        self.assertEqual(
            PrintCore.kPMBorderTypeStr, b"com.apple.print.PrintSettings.PMBorderType"
        )
        self.assertEqual(
            PrintCore.kPMBorderTypeKey, PrintCore.kPMBorderTypeStr.decode("utf-8")
        )

        self.assertEqual(
            PrintCore.kPMLayoutNUpStr, b"com.apple.print.PrintSettings.PMLayoutNUp"
        )
        self.assertEqual(
            PrintCore.kPMLayoutNUpKey, PrintCore.kPMLayoutNUpStr.decode("utf-8")
        )

        self.assertEqual(
            PrintCore.kPMLayoutRowsStr, b"com.apple.print.PrintSettings.PMLayoutRows"
        )
        self.assertEqual(
            PrintCore.kPMLayoutRowsKey, PrintCore.kPMLayoutRowsStr.decode("utf-8")
        )

        self.assertEqual(
            PrintCore.kPMLayoutColumnsStr,
            b"com.apple.print.PrintSettings.PMLayoutColumns",
        )
        self.assertEqual(
            PrintCore.kPMLayoutColumnsKey, PrintCore.kPMLayoutColumnsStr.decode("utf-8")
        )

        self.assertEqual(
            PrintCore.kPMLayoutDirectionStr,
            b"com.apple.print.PrintSettings.PMLayoutDirection",
        )
        self.assertEqual(
            PrintCore.kPMLayoutDirectionKey,
            PrintCore.kPMLayoutDirectionStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMLayoutTileOrientationStr,
            b"com.apple.print.PrintSettings.PMLayoutTileOrientation",
        )
        self.assertEqual(
            PrintCore.kPMLayoutTileOrientationKey,
            PrintCore.kPMLayoutTileOrientationStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMJobStateStr, b"com.apple.print.PrintSettings.PMJobState"
        )
        self.assertEqual(
            PrintCore.kPMJobStateKey, PrintCore.kPMJobStateStr.decode("utf-8")
        )

        self.assertEqual(
            PrintCore.kPMJobHoldUntilTimeStr,
            b"com.apple.print.PrintSettings.PMJobHoldUntilTime",
        )
        self.assertEqual(
            PrintCore.kPMJobHoldUntilTimeKey,
            PrintCore.kPMJobHoldUntilTimeStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMJobPriorityStr, b"com.apple.print.PrintSettings.PMJobPriority"
        )
        self.assertEqual(
            PrintCore.kPMJobPriorityKey, PrintCore.kPMJobPriorityStr.decode("utf-8")
        )

        self.assertEqual(
            PrintCore.kPMDuplexingStr, b"com.apple.print.PrintSettings.PMDuplexing"
        )
        self.assertEqual(
            PrintCore.kPMDuplexingKey, PrintCore.kPMDuplexingStr.decode("utf-8")
        )

        self.assertEqual(
            PrintCore.kPMColorSyncProfileIDStr,
            b"com.apple.print.PrintSettings.PMColorSyncProfileID",
        )
        self.assertEqual(
            PrintCore.kPMColorSyncProfileIDKey,
            PrintCore.kPMColorSyncProfileIDStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMPrimaryPaperFeedStr,
            b"com.apple.print.PrintSettings.PMPrimaryPaperFeed",
        )
        self.assertEqual(
            PrintCore.kPMPrimaryPaperFeedKey,
            PrintCore.kPMPrimaryPaperFeedStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMSecondaryPaperFeedStr,
            b"com.apple.print.PrintSettings.PMSecondaryPaperFeed",
        )
        self.assertEqual(
            PrintCore.kPMSecondaryPaperFeedKey,
            PrintCore.kPMSecondaryPaperFeedStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMPSErrorHandlerStr,
            b"com.apple.print.PrintSettings.PMPSErrorHandler",
        )
        self.assertEqual(
            PrintCore.kPMPSErrorHandlerKey,
            PrintCore.kPMPSErrorHandlerStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMPSTraySwitchStr,
            b"com.apple.print.PrintSettings.PMPSTraySwitch",
        )
        self.assertEqual(
            PrintCore.kPMPSTraySwitchKey, PrintCore.kPMPSTraySwitchStr.decode("utf-8")
        )

        self.assertEqual(
            PrintCore.kPMTotalBeginPagesStr,
            b"com.apple.print.PrintSettings.PMTotalBeginPages",
        )
        self.assertEqual(
            PrintCore.kPMTotalBeginPagesKey,
            PrintCore.kPMTotalBeginPagesStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMTotalSidesImagedStr,
            b"com.apple.print.PrintSettings.PMTotalSidesImaged",
        )
        self.assertEqual(
            PrintCore.kPMTotalSidesImagedKey,
            PrintCore.kPMTotalSidesImagedStr.decode("utf-8"),
        )

        self.assertEqual(PrintCore.kPMFitToPageStr, b"fit-to-page")
        self.assertEqual(
            PrintCore.kPMFitToPageKey, PrintCore.kPMFitToPageStr.decode("utf-8")
        )

        self.assertEqual(
            PrintCore.kPMUseOptionalPINStr,
            b"com.apple.print.PrintSettings.PMUseOptionalPIN",
        )
        self.assertEqual(
            PrintCore.kPMUseOptionalPINKey,
            PrintCore.kPMUseOptionalPINStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMUseOptionalAccountIDStr,
            b"com.apple.print.PrintSettings.PMUseOptionalAccountID",
        )
        self.assertEqual(
            PrintCore.kPMUseOptionalAccountIDKey,
            PrintCore.kPMUseOptionalAccountIDStr.decode("utf-8"),
        )

        self.assertEqual(PrintCore.kPMFaxNumberStr, b"phone")
        self.assertEqual(
            PrintCore.kPMFaxNumberKey, PrintCore.kPMFaxNumberStr.decode("utf-8")
        )

        self.assertEqual(PrintCore.kPMFaxToStr, b"faxTo")
        self.assertEqual(PrintCore.kPMFaxToKey, PrintCore.kPMFaxToStr.decode("utf-8"))

        self.assertEqual(PrintCore.kPMFaxPrefixStr, b"faxPrefix")
        self.assertEqual(
            PrintCore.kPMFaxPrefixKey, PrintCore.kPMFaxPrefixStr.decode("utf-8")
        )

        self.assertEqual(PrintCore.kPMFaxSubjectStr, b"faxSubject")
        self.assertEqual(
            PrintCore.kPMFaxSubjectKey, PrintCore.kPMFaxSubjectStr.decode("utf-8")
        )

        self.assertEqual(PrintCore.kPMFaxCoverSheetStr, b"faxCoverSheet")
        self.assertEqual(
            PrintCore.kPMFaxCoverSheetKey, PrintCore.kPMFaxCoverSheetStr.decode("utf-8")
        )

        self.assertEqual(PrintCore.kPMFaxCoverSheetMessageStr, b"faxCoverSheetMessage")
        self.assertEqual(
            PrintCore.kPMFaxCoverSheetMessageKey,
            PrintCore.kPMFaxCoverSheetMessageStr.decode("utf-8"),
        )

        self.assertEqual(PrintCore.kPMFaxToneDialingStr, b"faxToneDialing")
        self.assertEqual(
            PrintCore.kPMFaxToneDialingKey,
            PrintCore.kPMFaxToneDialingStr.decode("utf-8"),
        )

        self.assertEqual(PrintCore.kPMFaxUseSoundStr, b"faxUseSound")
        self.assertEqual(
            PrintCore.kPMFaxUseSoundKey, PrintCore.kPMFaxUseSoundStr.decode("utf-8")
        )

        self.assertEqual(PrintCore.kPMFaxWaitForDialToneStr, b"faxWaitForDialTone")
        self.assertEqual(
            PrintCore.kPMFaxWaitForDialToneKey,
            PrintCore.kPMFaxWaitForDialToneStr.decode("utf-8"),
        )

        self.assertEqual(PrintCore.kPMFaxToLabelStr, b"faxToLabel")
        self.assertEqual(
            PrintCore.kPMFaxToLabelKey, PrintCore.kPMFaxToLabelStr.decode("utf-8")
        )

        self.assertEqual(PrintCore.kPMFaxFromLabelStr, b"faxFromLabel")
        self.assertEqual(
            PrintCore.kPMFaxFromLabelKey, PrintCore.kPMFaxFromLabelStr.decode("utf-8")
        )

        self.assertEqual(PrintCore.kPMFaxDateLabelStr, b"faxDateLabel")
        self.assertEqual(
            PrintCore.kPMFaxDateLabelKey, PrintCore.kPMFaxDateLabelStr.decode("utf-8")
        )

        self.assertEqual(PrintCore.kPMFaxSubjectLabelStr, b"faxSubjectLabel")
        self.assertEqual(
            PrintCore.kPMFaxSubjectLabelKey,
            PrintCore.kPMFaxSubjectLabelStr.decode("utf-8"),
        )

        self.assertEqual(PrintCore.kPMFaxSheetsLabelStr, b"faxSheetsLabel")
        self.assertEqual(
            PrintCore.kPMFaxSheetsLabelKey,
            PrintCore.kPMFaxSheetsLabelStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMCoverPageStr, b"com.apple.print.PrintSettings.PMCoverPage"
        )
        self.assertEqual(
            PrintCore.kPMCoverPageKey, PrintCore.kPMCoverPageStr.decode("utf-8")
        )

        self.assertEqual(PrintCore.kPMCoverPageNone, 1)
        self.assertEqual(PrintCore.kPMCoverPageBefore, 2)
        self.assertEqual(PrintCore.kPMCoverPageAfter, 3)
        self.assertEqual(PrintCore.kPMCoverPageDefault, PrintCore.kPMCoverPageNone)

        self.assertEqual(
            PrintCore.kPMCoverPageSourceStr,
            b"com.apple.print.PrintSettings.PMCoverPageSource",
        )
        self.assertEqual(
            PrintCore.kPMCoverPageSourceKey,
            PrintCore.kPMCoverPageSourceStr.decode("utf-8"),
        )

        self.assertEqual(PrintCore.kPMDestinationPrinterIDStr, b"DestinationPrinterID")
        self.assertEqual(
            PrintCore.kPMDestinationPrinterIDKey,
            PrintCore.kPMDestinationPrinterIDStr.decode("utf-8"),
        )

        self.assertEqual(PrintCore.kPMInlineWorkflowStr, b"inlineWorkflow")
        self.assertEqual(
            PrintCore.kPMInlineWorkflowKey,
            PrintCore.kPMInlineWorkflowStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMPageToPaperMappingTypeStr,
            b"com.apple.print.PageToPaperMappingType",
        )
        self.assertEqual(
            PrintCore.kPMPageToPaperMappingTypeKey,
            PrintCore.kPMPageToPaperMappingTypeStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMPageToPaperMediaNameStr,
            b"com.apple.print.PageToPaperMappingMediaName",
        )
        self.assertEqual(
            PrintCore.kPMPageToPaperMediaNameKey,
            PrintCore.kPMPageToPaperMediaNameStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMPageToPaperMappingAllowScalingUpStr,
            b"com.apple.print.PageToPaperMappingAllowScalingUp",
        )
        self.assertEqual(
            PrintCore.kPMPageToPaperMappingAllowScalingUpKey,
            PrintCore.kPMPageToPaperMappingAllowScalingUpStr.decode("utf-8"),
        )

        self.assertEqual(PrintCore.kPMCustomProfilePathStr, b"PMCustomProfilePath")
        self.assertEqual(
            PrintCore.kPMCustomProfilePathKey,
            PrintCore.kPMCustomProfilePathStr.decode("utf-8"),
        )

        self.assertEqual(PrintCore.kPMPageToPaperMappingNone, 1)
        self.assertEqual(PrintCore.kPMPageToPaperMappingScaleToFit, 2)

        self.assertEqual(PrintCore.kPMVendorColorMatchingStr, b"AP_VendorColorMatching")
        self.assertEqual(
            PrintCore.kPMVendorColorMatching,
            PrintCore.kPMVendorColorMatchingStr.decode("utf-8"),
        )
        self.assertEqual(
            PrintCore.kPMApplicationColorMatchingStr, b"AP_ApplicationColorMatching"
        )
        self.assertEqual(
            PrintCore.kPMApplicationColorMatching,
            PrintCore.kPMApplicationColorMatchingStr.decode("utf-8"),
        )

        self.assertEqual(PrintCore.kPMColorMatchingModeStr, b"AP_ColorMatchingMode")
        self.assertEqual(
            PrintCore.kPMColorMatchingModeKey,
            PrintCore.kPMColorMatchingModeStr.decode("utf-8"),
        )

        self.assertEqual(
            PrintCore.kPMDestinationTypeStr,
            b"com.apple.print.PrintSettings.PMDestinationType",
        )
        self.assertEqual(
            PrintCore.kPMDestinationTypeKey,
            PrintCore.kPMDestinationTypeStr.decode("utf-8"),
        )
        self.assertEqual(
            PrintCore.kPMOutputFilenameStr,
            b"com.apple.print.PrintSettings.PMOutputFilename",
        )
        self.assertEqual(
            PrintCore.kPMOutputFilenameKey,
            PrintCore.kPMOutputFilenameStr.decode("utf-8"),
        )
