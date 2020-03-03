import PrintCore
from PyObjCTools.TestSupport import TestCase


class TestPMPrintingDialogExtensions(TestCase):
    def test_constants(self):
        self.assertEqual(
            PrintCore.kPMPageAttributesKindID, "com.apple.print.pde.PageAttributesKind"
        )
        self.assertEqual(
            PrintCore.kPMCopiesAndPagesPDEKindID,
            "com.apple.print.pde.CopiesAndPagesKind",
        )
        self.assertEqual(
            PrintCore.kPMLayoutPDEKindID, "com.apple.print.pde.LayoutUserOptionKind"
        )
        self.assertEqual(
            PrintCore.kPMOutputOptionsPDEKindID, "com.apple.print.pde.OutputOptionsKind"
        )
        self.assertEqual(PrintCore.kPMDuplexPDEKindID, "com.apple.print.pde.DuplexKind")
        self.assertEqual(
            PrintCore.kPMCustomPaperSizePDEKindID,
            "com.apple.print.pde.CustomPaperSizeKind",
        )
        self.assertEqual(
            PrintCore.kPMCoverPagePDEKindID, "com.apple.print.pde.CoverPageKind"
        )
        self.assertEqual(
            PrintCore.kPMColorMatchingPDEKindID, "com.apple.print.pde.ColorMatchingKind"
        )
        self.assertEqual(
            PrintCore.kPMSchedulerPDEKindID, "com.apple.print.pde.SchedulerKind"
        )
        self.assertEqual(
            PrintCore.kPMImagingOptionsPDEKindID,
            "com.apple.print.pde.ImagingOptionsKind",
        )
        self.assertEqual(
            PrintCore.kPMFaxCoverPagePDEKindID, "com.apple.print.pde.FaxCoverPageKind"
        )
        self.assertEqual(
            PrintCore.kPMFaxModemPDEKindID, "com.apple.print.pde.FaxModemKind"
        )
        self.assertEqual(
            PrintCore.kPMFaxAddressesPDEKindID, "com.apple.print.pde.FaxAddressesKind"
        )
        self.assertEqual(
            PrintCore.kPMPaperHandlingPDEKindID, "com.apple.print.pde.PaperHandlingKind"
        )
        self.assertEqual(
            PrintCore.kPMPDFEffectsPDEKindID, "com.apple.print.pde.PDFEffects"
        )
        self.assertEqual(
            PrintCore.kPMSummaryPanelKindID, "com.apple.print.pde.SummaryKind"
        )
        self.assertEqual(
            PrintCore.kPMUniPrinterPDEKindID, "com.apple.print.pde.UniPrinterKind"
        )
        self.assertEqual(PrintCore.kPMJobPINPDEKindID, "com.apple.print.pde.jobPIN")
        self.assertEqual(
            PrintCore.kPMPaperSourcePDEKindID, "com.apple.print.pde.PaperSourceKind"
        )
        self.assertEqual(
            PrintCore.kPMPriorityPDEKindID, "com.apple.print.pde.PriorityKind"
        )
        self.assertEqual(
            PrintCore.kPMRotationScalingPDEKindID,
            "com.apple.print.pde.RotationScalingKind",
        )
        self.assertEqual(
            PrintCore.kPMUnsupportedPDEKindID, "com.apple.print.pde.UnsupportedPDEKind"
        )
        self.assertEqual(
            PrintCore.kPMErrorHandlingPDEKindID, "com.apple.print.pde.ErrorHandlingKind"
        )
        self.assertEqual(
            PrintCore.kPMPaperFeedPDEKindID, "com.apple.print.pde.PaperFeedKind"
        )
        self.assertEqual(
            PrintCore.kPMPrinterFeaturesPDEKindID,
            "com.apple.print.pde.PrinterFeaturesKind",
        )
        self.assertEqual(PrintCore.kPMInkPDEKindID, "com.apple.print.pde.InkKind")
        self.assertEqual(PrintCore.kPMColorPDEKindID, "com.apple.print.pde.ColorKind")
        self.assertEqual(
            PrintCore.kPMMediaQualityPDEKindID,
            "com.apple.print.pde.MediaQualityPDEKind",
        )
        self.assertEqual(PrintCore.SUMMARY_DISPLAY_ORDER, "Summary, Display, Order")
        self.assertEqual(PrintCore.kPMSandboxCompatiblePDEs, "PMSandboxCompatiblePDEs")
        self.assertEqual(
            PrintCore.kDialogExtensionIntfIDStr, "A996FD7E-B738-11D3-8519-0050E4603277"
        )
        self.assertEqual(
            PrintCore.kGeneralPageSetupDialogTypeIDStr,
            "6E6ED964-B738-11D3-952F-0050E4603277",
        )
        self.assertEqual(
            PrintCore.kGeneralPrintDialogTypeIDStr,
            "C1BF838E-B72A-11D3-9644-0050E4603277",
        )
        self.assertEqual(
            PrintCore.kAppPageSetupDialogTypeIDStr,
            "B9A0DA98-E57F-11D3-9E83-0050E4603277",
        )
        self.assertEqual(
            PrintCore.kAppPrintDialogTypeIDStr, "BCB07250-E57F-11D3-8CA6-0050E4603277"
        )
        self.assertEqual(
            PrintCore.kAppPrintThumbnailTypeIDStr,
            "9320FE03-B5D5-11D5-84D1-003065D6135E",
        )
        self.assertEqual(
            PrintCore.kPrinterModuleTypeIDStr, "BDB091F4-E57F-11D3-B5CC-0050E4603277"
        )
