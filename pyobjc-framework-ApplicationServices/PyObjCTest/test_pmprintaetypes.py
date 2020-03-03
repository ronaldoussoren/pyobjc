import PrintCore
from PyObjCTools.TestSupport import TestCase


class TestPMPrintAETypes(TestCase):
    def test_not_exposed(self):
        self.assertFalse(hasattr(PrintCore, "kPMPrintSettingsAEType"))
        self.assertFalse(hasattr(PrintCore, "kPMShowPrintDialogAEType"))
        self.assertFalse(hasattr(PrintCore, "kPMPrinterAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMCopiesAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMCopiesAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMCopieAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMCollateAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMCollateAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMCollateAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMFirstPageAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMFirstPageAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMFirstPageAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMLastPageAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMLastPageAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMLastPageAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMLayoutAcrossAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMLayoutAcrossAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMLayoutAcrossAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMLayoutDownAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMLayoutDownAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMLayoutDownAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMErrorHandlingAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMErrorHandlingAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMErrorHandlingAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMPrintTimeAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMPrintTimeAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMPrintTimeAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMFeatureAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMFeatureAEKey	"))
        self.assertFalse(hasattr(PrintCore, "kPMFeatureAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMFaxNumberAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMFaxNumberAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMFaxNumberAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMTargetPrinterAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMTargetPrinterAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMTargetPrinterAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMPDFWorkFlowAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMPDFWorkFlowAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMPDFWorkFlowAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMPresetAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMPresetAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMPresetAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMSaveAsPDFAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMSaveAsPDFAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMSaveAsPDFAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMSaveAsPSAEProp"))
        self.assertFalse(hasattr(PrintCore, "kPMSaveAsPSAEKey"))
        self.assertFalse(hasattr(PrintCore, "kPMSaveAsPSAEType"))

        self.assertFalse(hasattr(PrintCore, "kPMErrorHandlingStandardEnum"))
        self.assertFalse(hasattr(PrintCore, "kPMErrorHandlingDetailedEnum"))
