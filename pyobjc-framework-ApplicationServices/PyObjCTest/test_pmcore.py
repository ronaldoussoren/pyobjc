import PrintCore
import objc
from PyObjCTools.TestSupport import TestCase


class TestPMCore(TestCase):
    def testFunctions(self):
        PrintCore.PMRetain
        PrintCore.PMRelease

        self.assertArgIsOut(PrintCore.PMCreateSession, 0)

        PrintCore.PMSessionError
        PrintCore.PMSessionSetError
        PrintCore.PMSessionBeginCGDocumentNoDialog
        PrintCore.PMSessionEndDocumentNoDialog
        PrintCore.PMSessionBeginPageNoDialog
        PrintCore.PMSessionEndPageNoDialog
        self.assertArgIsOut(PrintCore.PMSessionGetCGGraphicsContext, 1)
        self.assertArgIsOut(PrintCore.PMSessionGetDestinationType, 2)

        self.assertArgIsOut(PrintCore.PMSessionCopyDestinationFormat, 2)
        self.assertArgIsCFRetained(PrintCore.PMSessionCopyDestinationFormat, 2)

        self.assertArgIsOut(PrintCore.PMSessionCopyDestinationLocation, 2)
        self.assertArgIsCFRetained(PrintCore.PMSessionCopyDestinationLocation, 2)

        PrintCore.PMSessionSetDestination

        self.assertArgIsOut(PrintCore.PMSessionCopyOutputFormatList, 2)
        self.assertArgIsCFRetained(PrintCore.PMSessionCopyOutputFormatList, 2)

        self.assertArgIsOut(PrintCore.PMSessionCreatePageFormatList, 2)
        self.assertArgIsCFRetained(PrintCore.PMSessionCreatePageFormatList, 2)

        self.assertArgIsOut(PrintCore.PMSessionCreatePrinterList, 1)
        self.assertArgIsCFRetained(PrintCore.PMSessionCreatePrinterList, 1)
        self.assertArgIsOut(PrintCore.PMSessionCreatePrinterList, 2)
        self.assertArgIsOut(PrintCore.PMSessionCreatePrinterList, 3)

        self.assertArgIsOut(PrintCore.PMSessionGetCurrentPrinter, 1)

        PrintCore.PMSessionSetCurrentPMPrinter

        self.assertArgIsOut(PrintCore.PMSessionGetDataFromSession, 2)
        self.assertArgHasType(PrintCore.PMSessionGetDataFromSession, 2, b"o^@")

        self.assertArgHasType(PrintCore.PMSessionSetDataInSession, 2, b"@")

        self.assertArgIsOut(PrintCore.PMCreatePageFormat, 0)

        PrintCore.PMSessionDefaultPageFormat

        self.assertArgIsOut(PrintCore.PMSessionValidatePageFormat, 2)

        PrintCore.PMCopyPageFormat

        self.assertArgIsOut(PrintCore.PMCreatePageFormatWithPMPaper, 0)

        self.assertArgIsOut(PrintCore.PMPageFormatCreateDataRepresentation, 1)
        self.assertArgIsCFRetained(PrintCore.PMPageFormatCreateDataRepresentation, 1)

        self.assertArgIsOut(PrintCore.PMPageFormatCreateWithDataRepresentation, 1)

        self.assertArgIsOut(PrintCore.PMGetAdjustedPageRect, 1)

        self.assertArgIsOut(PrintCore.PMGetAdjustedPaperRect, 1)

        self.assertArgIsOut(PrintCore.PMGetOrientation, 1)

        self.assertArgIsInOut(PrintCore.PMGetPageFormatExtendedData, 2)
        self.assertArgIsOut(PrintCore.PMGetPageFormatExtendedData, 3)
        self.assertArgSizeInArg(PrintCore.PMGetPageFormatExtendedData, 3, 2)

        self.assertArgIsOut(PrintCore.PMPageFormatGetPrinterID, 1)

        self.assertArgIsOut(PrintCore.PMGetScale, 1)

        self.assertArgIsOut(PrintCore.PMGetUnadjustedPageRect, 1)

        self.assertArgIsOut(PrintCore.PMGetUnadjustedPaperRect, 1)

        self.assertArgIsBOOL(PrintCore.PMSetOrientation, 2)

        self.assertArgIsIn(PrintCore.PMSetPageFormatExtendedData, 3)
        self.assertArgSizeInArg(PrintCore.PMSetPageFormatExtendedData, 3, 2)

        PrintCore.PMSetScale

        self.assertArgIsOut(PrintCore.PMCreatePrintSettings, 0)

        PrintCore.PMSessionDefaultPrintSettings

        self.assertArgIsOut(PrintCore.PMSessionValidatePrintSettings, 2)

        PrintCore.PMCopyPrintSettings

        self.assertArgIsOut(PrintCore.PMPrintSettingsCreateDataRepresentation, 1)
        self.assertArgIsCFRetained(PrintCore.PMPrintSettingsCreateDataRepresentation, 1)

        self.assertArgIsOut(PrintCore.PMPrintSettingsCreateWithDataRepresentation, 1)

        self.assertArgIsOut(PrintCore.PMGetCollate, 1)

        self.assertArgIsOut(PrintCore.PMGetCopies, 1)

        self.assertArgIsOut(PrintCore.PMGetDuplex, 1)

        self.assertArgIsOut(PrintCore.PMGetFirstPage, 1)

        self.assertArgIsOut(PrintCore.PMGetLastPage, 1)

        self.assertArgIsOut(PrintCore.PMGetPageRange, 1)
        self.assertArgIsOut(PrintCore.PMGetPageRange, 2)

        self.assertArgIsOut(PrintCore.PMPrintSettingsGetJobName, 1)

        self.assertArgIsOut(PrintCore.PMPrintSettingsGetValue, 2)

        self.assertArgIsBOOL(PrintCore.PMSetCollate, 1)

        self.assertArgIsBOOL(PrintCore.PMSetCopies, 2)

        PrintCore.PMSetDuplex

        self.assertArgIsBOOL(PrintCore.PMSetFirstPage, 2)

        self.assertArgIsBOOL(PrintCore.PMSetLastPage, 2)

        PrintCore.PMSetPageRange
        PrintCore.PMPrintSettingsSetJobName

        self.assertArgHasType(PrintCore.PMPrintSettingsSetValue, 2, objc._C_ID)
        self.assertArgIsBOOL(PrintCore.PMPrintSettingsSetValue, 3)

        self.assertArgIsOut(PrintCore.PMPrintSettingsCopyAsDictionary, 1)
        self.assertArgIsCFRetained(PrintCore.PMPrintSettingsCopyAsDictionary, 1)

        self.assertArgIsOut(PrintCore.PMPrintSettingsCopyKeys, 1)
        self.assertArgIsCFRetained(PrintCore.PMPrintSettingsCopyKeys, 1)

        self.assertArgIsOut(PrintCore.PMCreateGenericPrinter, 0)

        self.assertArgIsOut(PrintCore.PMServerCreatePrinterList, 1)
        self.assertArgIsCFRetained(PrintCore.PMServerCreatePrinterList, 1)

        PrintCore.PMServerLaunchPrinterBrowser
        PrintCore.PMPrinterCreateFromPrinterID

        self.assertArgIsOut(PrintCore.PMPrinterCopyDescriptionURL, 2)
        self.assertArgIsCFRetained(PrintCore.PMPrinterCopyDescriptionURL, 2)

        self.assertArgIsOut(PrintCore.PMPrinterCopyDeviceURI, 1)
        self.assertArgIsCFRetained(PrintCore.PMPrinterCopyDeviceURI, 1)

        self.assertArgIsOut(PrintCore.PMPrinterCopyHostName, 1)
        self.assertArgIsCFRetained(PrintCore.PMPrinterCopyHostName, 1)

        self.assertArgIsOut(PrintCore.PMPrinterCopyPresets, 1)
        self.assertArgIsCFRetained(PrintCore.PMPrinterCopyPresets, 1)

        self.assertArgIsOut(PrintCore.PMPrinterGetCommInfo, 1)
        self.assertArgIsOut(PrintCore.PMPrinterGetCommInfo, 2)

        PrintCore.PMPrinterGetID
        PrintCore.PMPrinterGetLocation

        self.assertArgIsOut(PrintCore.PMPrinterGetDriverCreator, 1)

        self.assertArgIsOut(PrintCore.PMPrinterGetDriverReleaseInfo, 1)

        self.assertArgIsOut(PrintCore.PMPrinterGetPrinterResolutionCount, 1)

        self.assertArgIsOut(PrintCore.PMPrinterGetIndexedPrinterResolution, 2)

        self.assertArgIsOut(PrintCore.PMPrinterGetOutputResolution, 2)

        self.assertArgIsIn(PrintCore.PMPrinterSetOutputResolution, 2)

        self.assertArgIsOut(PrintCore.PMPrinterGetLanguageInfo, 1)

        self.assertArgIsOut(PrintCore.PMPrinterGetMakeAndModelName, 1)

        self.assertArgIsOut(PrintCore.PMPrinterGetMimeTypes, 2)

        PrintCore.PMPrinterGetName

        self.assertArgIsOut(PrintCore.PMPrinterGetPaperList, 1)

        self.assertArgIsOut(PrintCore.PMPrinterGetState, 1)

        self.assertResultIsBOOL(PrintCore.PMPrinterIsDefault)

        self.assertResultIsBOOL(PrintCore.PMPrinterIsFavorite)

        self.assertResultIsBOOL(PrintCore.PMPrinterIsPostScriptCapable)

        self.assertArgIsOut(PrintCore.PMPrinterIsPostScriptPrinter, 1)

        self.assertArgIsOut(PrintCore.PMPrinterIsRemote, 1)

        PrintCore.PMPrinterSetDefault

        self.assertArgIsOut(PrintCore.PMPresetCopyName, 1)
        self.assertArgIsCFRetained(PrintCore.PMPresetCopyName, 1)

        self.assertArgIsOut(PrintCore.PMPresetCreatePrintSettings, 2)

        self.assertArgIsOut(PrintCore.PMPresetGetAttributes, 1)

        self.assertArgIsOut(PrintCore.PMGetPageFormatPaper, 1)

        self.assertArgIsIn(PrintCore.PMPaperCreateCustom, 5)
        self.assertArgIsOut(PrintCore.PMPaperCreateCustom, 6)

        self.assertArgIsOut(PrintCore.PMPaperGetWidth, 1)

        self.assertArgIsOut(PrintCore.PMPaperGetHeight, 1)

        self.assertArgIsOut(PrintCore.PMPaperGetMargins, 1)

        self.assertArgIsOut(PrintCore.PMPaperGetID, 1)

        self.assertArgIsOut(PrintCore.PMPaperGetPPDPaperName, 1)

        self.assertArgIsOut(PrintCore.PMPaperCreateLocalizedName, 2)
        self.assertArgIsCFRetained(PrintCore.PMPaperCreateLocalizedName, 2)

        self.assertArgIsOut(PrintCore.PMPaperGetPrinterID, 1)

        self.assertResultIsBOOL(PrintCore.PMPaperIsCustom)

        self.assertArgIsOut(PrintCore.PMWorkflowCopyItems, 0)
        self.assertArgIsCFRetained(PrintCore.PMWorkflowCopyItems, 0)

        self.assertArgIsIn(PrintCore.PMWorkflowSubmitPDFWithOptions, 2)
        self.assertArgIsNullTerminated(PrintCore.PMWorkflowSubmitPDFWithOptions, 2)

        PrintCore.PMWorkflowSubmitPDFWithSettings
        PrintCore.PMPrinterPrintWithProvider
        PrintCore.PMPrinterPrintWithFile
        PrintCore.PMPrinterWritePostScriptToURL

        self.assertFalse(hasattr(PrintCore, "PMPrintSettingsToOptions"))
        self.assertFalse(
            hasattr(PrintCore, "PMPrintSettingsToOptionsWithPrinterAndPageFormat")
        )
        # self.assertArgIsOut(PrintCore.PMPrintSettingsToOptions, 1)

        PrintCore.PMPrinterSendCommand

        self.assertArgIsOut(PrintCore.PMPrinterCopyState, 1)
        self.assertArgIsCFRetained(PrintCore.PMPrinterCopyState, 1)

        self.assertArgIsOut(PrintCore.PMCopyAvailablePPDs, 1)
        self.assertArgIsCFRetained(PrintCore.PMCopyAvailablePPDs, 1)

        self.assertArgIsOut(PrintCore.PMCopyLocalizedPPD, 1)
        self.assertArgIsCFRetained(PrintCore.PMCopyLocalizedPPD, 1)

        self.assertArgIsOut(PrintCore.PMCopyPPDData, 1)
        self.assertArgIsCFRetained(PrintCore.PMCopyPPDData, 1)

        self.assertResultIsCFRetained(PrintCore.PMCGImageCreateWithEPSDataProvider)
