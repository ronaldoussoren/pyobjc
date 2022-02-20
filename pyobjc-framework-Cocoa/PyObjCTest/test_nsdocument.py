import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSDocument(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSDocumentChangeType)
        self.assertIsEnumType(AppKit.NSSaveOperationType)

    def testConstants(self):
        self.assertEqual(AppKit.NSChangeDone, 0)
        self.assertEqual(AppKit.NSChangeUndone, 1)
        self.assertEqual(AppKit.NSChangeCleared, 2)
        self.assertEqual(AppKit.NSChangeRedone, 5)
        self.assertEqual(AppKit.NSChangeReadOtherContents, 3)
        self.assertEqual(AppKit.NSChangeAutosaved, 4)

        self.assertEqual(AppKit.NSSaveOperation, 0)
        self.assertEqual(AppKit.NSSaveAsOperation, 1)
        self.assertEqual(AppKit.NSSaveToOperation, 2)
        self.assertEqual(AppKit.NSAutosaveOperation, 3)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSChangeDiscardable, 256)
        self.assertEqual(AppKit.NSAutosaveInPlaceOperation, 4)
        self.assertEqual(AppKit.NSAutosaveElsewhereOperation, 3)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(AppKit.NSAutosaveAsOperation, 5)

    def testMethods(self):
        self.assertArgIsOut(AppKit.NSDocument.initWithType_error_, 1)
        self.assertArgIsOut(AppKit.NSDocument.initWithContentsOfURL_ofType_error_, 2)
        self.assertArgIsOut(
            AppKit.NSDocument.initForURL_withContentsOfURL_ofType_error_, 3
        )
        self.assertResultIsBOOL(AppKit.NSDocument.revertToContentsOfURL_ofType_error_)
        self.assertArgIsOut(AppKit.NSDocument.revertToContentsOfURL_ofType_error_, 2)
        self.assertResultIsBOOL(AppKit.NSDocument.readFromURL_ofType_error_)
        self.assertArgIsOut(AppKit.NSDocument.readFromURL_ofType_error_, 2)
        self.assertResultIsBOOL(AppKit.NSDocument.readFromFileWrapper_ofType_error_)
        self.assertArgIsOut(AppKit.NSDocument.readFromFileWrapper_ofType_error_, 2)
        self.assertResultIsBOOL(AppKit.NSDocument.readFromData_ofType_error_)
        self.assertArgIsOut(AppKit.NSDocument.readFromData_ofType_error_, 2)
        self.assertResultIsBOOL(AppKit.NSDocument.writeToURL_ofType_error_)
        self.assertArgIsOut(AppKit.NSDocument.writeToURL_ofType_error_, 2)
        self.assertArgIsOut(AppKit.NSDocument.fileWrapperOfType_error_, 1)
        self.assertArgIsOut(AppKit.NSDocument.dataOfType_error_, 1)
        self.assertResultIsBOOL(
            AppKit.NSDocument.writeSafelyToURL_ofType_forSaveOperation_error_
        )
        self.assertArgIsOut(
            AppKit.NSDocument.writeSafelyToURL_ofType_forSaveOperation_error_, 3
        )
        self.assertResultIsBOOL(
            AppKit.NSDocument.writeToURL_ofType_forSaveOperation_originalContentsURL_error_
        )
        self.assertArgIsOut(
            AppKit.NSDocument.writeToURL_ofType_forSaveOperation_originalContentsURL_error_,
            4,
        )
        self.assertArgIsOut(
            AppKit.NSDocument.fileAttributesToWriteToURL_ofType_forSaveOperation_originalContentsURL_error_,  # noqa: B950
            4,
        )
        self.assertResultIsBOOL(AppKit.NSDocument.keepBackupFile)
        self.assertArgIsSEL(
            AppKit.NSDocument.saveDocumentWithDelegate_didSaveSelector_contextInfo_,
            1,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocument.saveDocumentWithDelegate_didSaveSelector_contextInfo_,
            2,
            b"^v",
        )
        self.assertArgIsSEL(
            AppKit.NSDocument.runModalSavePanelForSaveOperation_delegate_didSaveSelector_contextInfo_,  # noqa: B950
            2,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocument.runModalSavePanelForSaveOperation_delegate_didSaveSelector_contextInfo_,  # noqa: B950
            3,
            b"^v",
        )
        self.assertResultIsBOOL(AppKit.NSDocument.shouldRunSavePanelWithAccessoryView)
        self.assertResultIsBOOL(AppKit.NSDocument.prepareSavePanel_)
        self.assertResultIsBOOL(
            AppKit.NSDocument.fileNameExtensionWasHiddenInLastRunSavePanel
        )
        self.assertArgIsSEL(
            AppKit.NSDocument.saveToURL_ofType_forSaveOperation_delegate_didSaveSelector_contextInfo_,  # noqa: B950
            4,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocument.saveToURL_ofType_forSaveOperation_delegate_didSaveSelector_contextInfo_,  # noqa: B950
            5,
            b"^v",
        )
        self.assertResultIsBOOL(
            AppKit.NSDocument.saveToURL_ofType_forSaveOperation_error_
        )
        self.assertArgIsOut(
            AppKit.NSDocument.saveToURL_ofType_forSaveOperation_error_, 3
        )
        self.assertResultIsBOOL(AppKit.NSDocument.hasUnautosavedChanges)
        self.assertArgIsSEL(
            AppKit.NSDocument.autosaveDocumentWithDelegate_didAutosaveSelector_contextInfo_,
            1,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocument.autosaveDocumentWithDelegate_didAutosaveSelector_contextInfo_,
            2,
            b"^v",
        )
        self.assertArgIsSEL(
            AppKit.NSDocument.canCloseDocumentWithDelegate_shouldCloseSelector_contextInfo_,
            1,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocument.canCloseDocumentWithDelegate_shouldCloseSelector_contextInfo_,
            2,
            b"^v",
        )
        self.assertArgIsSEL(
            AppKit.NSDocument.runModalPageLayoutWithPrintInfo_delegate_didRunSelector_contextInfo_,  # noqa: B950
            2,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocument.runModalPageLayoutWithPrintInfo_delegate_didRunSelector_contextInfo_,  # noqa: B950
            3,
            b"^v",
        )
        self.assertResultIsBOOL(AppKit.NSDocument.preparePageLayout_)
        self.assertResultIsBOOL(AppKit.NSDocument.shouldChangePrintInfo_)
        self.assertArgIsSEL(
            AppKit.NSDocument.printDocumentWithSettings_showPrintPanel_delegate_didPrintSelector_contextInfo_,  # noqa: B950
            3,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocument.printDocumentWithSettings_showPrintPanel_delegate_didPrintSelector_contextInfo_,  # noqa: B950
            4,
            b"^v",
        )
        self.assertArgIsOut(AppKit.NSDocument.printOperationWithSettings_error_, 1)
        self.assertArgIsSEL(
            AppKit.NSDocument.runModalPrintOperation_delegate_didRunSelector_contextInfo_,
            2,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocument.runModalPrintOperation_delegate_didRunSelector_contextInfo_,
            3,
            b"^v",
        )
        self.assertResultIsBOOL(AppKit.NSDocument.isDocumentEdited)
        self.assertResultIsBOOL(AppKit.NSDocument.hasUndoManager)
        self.assertArgIsBOOL(AppKit.NSDocument.setHasUndoManager_, 0)
        self.assertResultIsBOOL(AppKit.NSDocument.presentError_)
        self.assertArgIsSEL(
            AppKit.NSDocument.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_,  # noqa: B950
            3,
            b"v@:" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocument.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_,  # noqa: B950
            4,
            b"^v",
        )
        self.assertArgIsSEL(
            AppKit.NSDocument.shouldCloseWindowController_delegate_shouldCloseSelector_contextInfo_,  # noqa: B950
            2,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocument.shouldCloseWindowController_delegate_shouldCloseSelector_contextInfo_,  # noqa: B950
            3,
            b"^v",
        )
        self.assertResultIsBOOL(AppKit.NSDocument.isNativeType_)
        self.assertResultIsBOOL(AppKit.NSDocument.validateUserInterfaceItem_)
        self.assertResultIsBOOL(AppKit.NSDocument.loadDataRepresentation_ofType_)
        self.assertArgIsBOOL(AppKit.NSDocument.printShowingPrintPanel_, 0)
        self.assertResultIsBOOL(AppKit.NSDocument.readFromFile_ofType_)
        self.assertResultIsBOOL(AppKit.NSDocument.readFromURL_ofType_)
        self.assertResultIsBOOL(AppKit.NSDocument.revertToSavedFromFile_ofType_)
        self.assertResultIsBOOL(AppKit.NSDocument.revertToSavedFromURL_ofType_)
        self.assertResultIsBOOL(AppKit.NSDocument.writeToFile_ofType_)
        self.assertResultIsBOOL(
            AppKit.NSDocument.writeToFile_ofType_originalFile_saveOperation_
        )
        self.assertResultIsBOOL(AppKit.NSDocument.writeToURL_ofType_)
        self.assertResultIsBOOL(
            AppKit.NSDocument.writeWithBackupToFile_ofType_saveOperation_
        )
        self.assertArgIsSEL(
            AppKit.NSDocument.saveToFile_saveOperation_delegate_didSaveSelector_contextInfo_,
            3,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocument.saveToFile_saveOperation_delegate_didSaveSelector_contextInfo_,
            4,
            b"^v",
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(AppKit.NSDocument.canConcurrentlyReadDocumentsOfType_)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBOOL(
            AppKit.NSDocument.performActivityWithSynchronousWaiting_usingBlock_, 0
        )
        self.assertArgIsBlock(
            AppKit.NSDocument.performActivityWithSynchronousWaiting_usingBlock_, 1, b"v"
        )
        self.assertArgIsBlock(AppKit.NSDocument.continueActivityUsingBlock_, 0, b"v")
        self.assertArgIsBlock(
            AppKit.NSDocument.continueAsynchronousWorkOnMainThreadUsingBlock_, 0, b"v"
        )
        self.assertArgIsBlock(
            AppKit.NSDocument.performSynchronousFileAccessUsingBlock_, 0, b"v"
        )

        self.assertArgIsBlock(
            AppKit.NSDocument.performAsynchronousFileAccessUsingBlock_, 0, b"v@?"
        )  # FIXME: block has a block argument

        self.assertResultIsBOOL(AppKit.NSDocument.isEntireFileLoaded)
        self.assertResultIsBOOL(AppKit.NSDocument.autosavingIsImplicitlyCancellable)

        self.assertArgIsBlock(
            AppKit.NSDocument.saveToURL_ofType_forSaveOperation_completionHandler_,
            3,
            b"v@",
        )
        self.assertResultIsBOOL(
            AppKit.NSDocument.canAsynchronouslyWriteToURL_ofType_forSaveOperation_
        )
        self.assertResultIsBOOL(AppKit.NSDocument.checkAutosavingSafetyAndReturnError_)
        self.assertArgIsOut(AppKit.NSDocument.checkAutosavingSafetyAndReturnError_, 0)
        self.assertArgIsBOOL(
            AppKit.NSDocument.autosaveWithImplicitCancellability_completionHandler_, 0
        )
        self.assertArgIsBlock(
            AppKit.NSDocument.autosaveWithImplicitCancellability_completionHandler_,
            1,
            b"v@",
        )

        self.assertResultIsBOOL(AppKit.NSDocument.autosavesInPlace)
        self.assertResultIsBOOL(AppKit.NSDocument.preservesVersions)

        self.assertArgIsSEL(
            AppKit.NSDocument.duplicateDocumentWithDelegate_didDuplicateSelector_contextInfo_,
            1,
            b"v@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgIsOut(AppKit.NSDocument.duplicateAndReturnError_, 0)
        self.assertResultIsBOOL(AppKit.NSDocument.isInViewingMode)

        self.assertArgIsBlock(
            AppKit.NSDocument.saveToURL_ofType_forSaveOperation_completionHandler_,
            3,
            b"v@",
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertArgIsBOOL(AppKit.NSDocument.setDraft_, 0)
        self.assertResultIsBOOL(AppKit.NSDocument.isDraft)
        self.assertResultIsBOOL(AppKit.NSDocument.autosavesDrafts)

        self.assertArgIsBlock(
            AppKit.NSDocument.moveDocumentWithCompletionHandler_,
            0,
            b"v" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            AppKit.NSDocument.moveToURL_completionHandler_, 1, b"v" + objc._C_NSBOOL
        )
        self.assertArgIsBlock(
            AppKit.NSDocument.lockDocumentWithCompletionHandler_,
            0,
            b"v" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(AppKit.NSDocument.lockWithCompletionHandler_, 0, b"v@")
        self.assertArgIsBlock(
            AppKit.NSDocument.unlockDocumentWithCompletionHandler_,
            0,
            b"v" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(AppKit.NSDocument.unlockWithCompletionHandler_, 0, b"v@")
        self.assertResultIsBOOL(AppKit.NSDocument.isLocked)
        self.assertResultIsBOOL(AppKit.NSDocument.usesUbiquitousStorage)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSDocument.isBrowsingVersions)

        self.assertArgIsBlock(
            AppKit.NSDocument.stopBrowsingVersionsWithCompletionHandler_, 0, b"v"
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(AppKit.NSDocument.allowsDocumentSharing)
        self.assertArgIsBlock(
            AppKit.NSDocument.shareDocumentWithSharingService_completionHandler_,
            1,
            b"vZ",
        )
