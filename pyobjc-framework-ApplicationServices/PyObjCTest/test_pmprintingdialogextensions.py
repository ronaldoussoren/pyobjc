
import PrintCore
import sys
from PyObjCTools.TestSupport import *

class TestPMPrintingDialogExtensions (TestCase):
    def test_constants(self):
        self.assertEqual(PrintCore.kPMPageAttributesKindID, u"com.apple.print.pde.PageAttributesKind")
        self.assertEqual(PrintCore.kPMCopiesAndPagesPDEKindID, u"com.apple.print.pde.CopiesAndPagesKind")
        self.assertEqual(PrintCore.kPMLayoutPDEKindID, u"com.apple.print.pde.LayoutUserOptionKind")
        self.assertEqual(PrintCore.kPMOutputOptionsPDEKindID, u"com.apple.print.pde.OutputOptionsKind")
        self.assertEqual(PrintCore.kPMDuplexPDEKindID, u"com.apple.print.pde.DuplexKind")
        self.assertEqual(PrintCore.kPMCustomPaperSizePDEKindID, u"com.apple.print.pde.CustomPaperSizeKind")
        self.assertEqual(PrintCore.kPMCoverPagePDEKindID, u"com.apple.print.pde.CoverPageKind")
        self.assertEqual(PrintCore.kPMColorMatchingPDEKindID, u"com.apple.print.pde.ColorMatchingKind")
        self.assertEqual(PrintCore.kPMSchedulerPDEKindID, u"com.apple.print.pde.SchedulerKind")
        self.assertEqual(PrintCore.kPMImagingOptionsPDEKindID, u"com.apple.print.pde.ImagingOptionsKind")
        self.assertEqual(PrintCore.kPMFaxCoverPagePDEKindID, u"com.apple.print.pde.FaxCoverPageKind")
        self.assertEqual(PrintCore.kPMFaxModemPDEKindID, u"com.apple.print.pde.FaxModemKind")
        self.assertEqual(PrintCore.kPMFaxAddressesPDEKindID, u"com.apple.print.pde.FaxAddressesKind")
        self.assertEqual(PrintCore.kPMPaperHandlingPDEKindID, u"com.apple.print.pde.PaperHandlingKind")
        self.assertEqual(PrintCore.kPMPDFEffectsPDEKindID, u"com.apple.print.pde.PDFEffects")
        self.assertEqual(PrintCore.kPMSummaryPanelKindID, u"com.apple.print.pde.SummaryKind")
        self.assertEqual(PrintCore.kPMUniPrinterPDEKindID, u"com.apple.print.pde.UniPrinterKind")
        self.assertEqual(PrintCore.kPMJobPINPDEKindID, u"com.apple.print.pde.jobPIN")
        self.assertEqual(PrintCore.kPMPaperSourcePDEKindID, u"com.apple.print.pde.PaperSourceKind")
        self.assertEqual(PrintCore.kPMPriorityPDEKindID, u"com.apple.print.pde.PriorityKind")
        self.assertEqual(PrintCore.kPMRotationScalingPDEKindID, u"com.apple.print.pde.RotationScalingKind")
        self.assertEqual(PrintCore.kPMUnsupportedPDEKindID, u"com.apple.print.pde.UnsupportedPDEKind")
        self.assertEqual(PrintCore.kPMErrorHandlingPDEKindID, u"com.apple.print.pde.ErrorHandlingKind")
        self.assertEqual(PrintCore.kPMPaperFeedPDEKindID, u"com.apple.print.pde.PaperFeedKind")
        self.assertEqual(PrintCore.kPMPrinterFeaturesPDEKindID, u"com.apple.print.pde.PrinterFeaturesKind")
        self.assertEqual(PrintCore.kPMInkPDEKindID, u"com.apple.print.pde.InkKind")
        self.assertEqual(PrintCore.kPMColorPDEKindID, u"com.apple.print.pde.ColorKind")
        self.assertEqual(PrintCore.kPMMediaQualityPDEKindID, u"com.apple.print.pde.MediaQualityPDEKind")
        self.assertEqual(PrintCore.kPMWatermarkPDEKindID, u"com.apple.print.pde.WatermarkPDEKind")
        self.assertEqual(PrintCore.SUMMARY_DISPLAY_ORDER, u"Summary, Display, Order")
        self.assertEqual(PrintCore.kPMSandboxCompatiblePDEs, u"PMSandboxCompatiblePDEs")
        self.assertEqual(PrintCore.kDialogExtensionIntfIDStr, u"A996FD7E-B738-11D3-8519-0050E4603277")
        self.assertEqual(PrintCore.kGeneralPageSetupDialogTypeIDStr, u"6E6ED964-B738-11D3-952F-0050E4603277")
        self.assertEqual(PrintCore.kGeneralPrintDialogTypeIDStr, u"C1BF838E-B72A-11D3-9644-0050E4603277")
        self.assertEqual(PrintCore.kAppPageSetupDialogTypeIDStr, u"B9A0DA98-E57F-11D3-9E83-0050E4603277")
        self.assertEqual(PrintCore.kAppPrintDialogTypeIDStr, u"BCB07250-E57F-11D3-8CA6-0050E4603277")
        self.assertEqual(PrintCore.kAppPrintThumbnailTypeIDStr, u"9320FE03-B5D5-11D5-84D1-003065D6135E")
        self.assertEqual(PrintCore.kPrinterModuleTypeIDStr, u"BDB091F4-E57F-11D3-B5CC-0050E4603277")

if __name__ == "__main__":
    main()
