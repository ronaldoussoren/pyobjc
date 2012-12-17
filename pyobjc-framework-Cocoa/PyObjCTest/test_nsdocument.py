
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSDocument (TestCase):
    def testConstants(self):
        self.assertEqual(NSChangeDone, 0)
        self.assertEqual(NSChangeUndone, 1)
        self.assertEqual(NSChangeCleared, 2)
        self.assertEqual(NSChangeRedone, 5)
        self.assertEqual(NSChangeReadOtherContents, 3)
        self.assertEqual(NSChangeAutosaved, 4)

        self.assertEqual(NSSaveOperation, 0)
        self.assertEqual(NSSaveAsOperation, 1)
        self.assertEqual(NSSaveToOperation, 2)
        self.assertEqual(NSAutosaveOperation, 3)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSChangeDiscardable, 256)
        self.assertEqual(NSAutosaveInPlaceOperation, 4)
        self.assertEqual(NSAutosaveElsewhereOperation, 3)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(NSAutosaveAsOperation, 5)


    def testMethods(self):
        self.assertArgIsOut(NSDocument.initWithType_error_, 1)
        self.assertArgIsOut(NSDocument.initWithContentsOfURL_ofType_error_, 2)
        self.assertArgIsOut(NSDocument.initForURL_withContentsOfURL_ofType_error_, 3)
        self.assertResultIsBOOL(NSDocument.revertToContentsOfURL_ofType_error_)
        self.assertArgIsOut(NSDocument.revertToContentsOfURL_ofType_error_, 2)
        self.assertResultIsBOOL(NSDocument.readFromURL_ofType_error_)
        self.assertArgIsOut(NSDocument.readFromURL_ofType_error_, 2)
        self.assertResultIsBOOL(NSDocument.readFromFileWrapper_ofType_error_)
        self.assertArgIsOut(NSDocument.readFromFileWrapper_ofType_error_, 2)
        self.assertResultIsBOOL(NSDocument.readFromData_ofType_error_)
        self.assertArgIsOut(NSDocument.readFromData_ofType_error_, 2)
        self.assertResultIsBOOL(NSDocument.writeToURL_ofType_error_)
        self.assertArgIsOut(NSDocument.writeToURL_ofType_error_, 2)
        self.assertArgIsOut(NSDocument.fileWrapperOfType_error_, 1)
        self.assertArgIsOut(NSDocument.dataOfType_error_, 1)
        self.assertResultIsBOOL(NSDocument.writeSafelyToURL_ofType_forSaveOperation_error_)
        self.assertArgIsOut(NSDocument.writeSafelyToURL_ofType_forSaveOperation_error_, 3)
        self.assertResultIsBOOL(NSDocument.writeToURL_ofType_forSaveOperation_originalContentsURL_error_)
        self.assertArgIsOut(NSDocument.writeToURL_ofType_forSaveOperation_originalContentsURL_error_, 4)
        self.assertArgIsOut(NSDocument.fileAttributesToWriteToURL_ofType_forSaveOperation_originalContentsURL_error_, 4)
        self.assertResultIsBOOL(NSDocument.keepBackupFile)
        self.assertArgIsSEL(NSDocument.saveDocumentWithDelegate_didSaveSelector_contextInfo_, 1, b"v@:@"+objc._C_NSBOOL+b"^v")
        self.assertArgHasType(NSDocument.saveDocumentWithDelegate_didSaveSelector_contextInfo_, 2, b"^v")
        self.assertArgIsSEL(NSDocument.runModalSavePanelForSaveOperation_delegate_didSaveSelector_contextInfo_, 2, b"v@:@"+objc._C_NSBOOL+b"^v")
        self.assertArgHasType(NSDocument.runModalSavePanelForSaveOperation_delegate_didSaveSelector_contextInfo_, 3, b"^v")
        self.assertResultIsBOOL(NSDocument.shouldRunSavePanelWithAccessoryView)
        self.assertResultIsBOOL(NSDocument.prepareSavePanel_)
        self.assertResultIsBOOL(NSDocument.fileNameExtensionWasHiddenInLastRunSavePanel)
        self.assertArgIsSEL(NSDocument.saveToURL_ofType_forSaveOperation_delegate_didSaveSelector_contextInfo_, 4, b"v@:@"+objc._C_NSBOOL+b"^v")
        self.assertArgHasType(NSDocument.saveToURL_ofType_forSaveOperation_delegate_didSaveSelector_contextInfo_, 5, b"^v")
        self.assertResultIsBOOL(NSDocument.saveToURL_ofType_forSaveOperation_error_)
        self.assertArgIsOut(NSDocument.saveToURL_ofType_forSaveOperation_error_, 3)
        self.assertResultIsBOOL(NSDocument.hasUnautosavedChanges)
        self.assertArgIsSEL(NSDocument.autosaveDocumentWithDelegate_didAutosaveSelector_contextInfo_, 1, b"v@:@"+objc._C_NSBOOL+b"^v")
        self.assertArgHasType(NSDocument.autosaveDocumentWithDelegate_didAutosaveSelector_contextInfo_, 2, b"^v")
        self.assertArgIsSEL(NSDocument.canCloseDocumentWithDelegate_shouldCloseSelector_contextInfo_, 1, b"v@:@"+objc._C_NSBOOL+b"^v")
        self.assertArgHasType(NSDocument.canCloseDocumentWithDelegate_shouldCloseSelector_contextInfo_, 2, b"^v")
        self.assertArgIsSEL(NSDocument.runModalPageLayoutWithPrintInfo_delegate_didRunSelector_contextInfo_, 2, b"v@:@"+objc._C_NSBOOL+b"^v")
        self.assertArgHasType(NSDocument.runModalPageLayoutWithPrintInfo_delegate_didRunSelector_contextInfo_, 3, b"^v")
        self.assertResultIsBOOL(NSDocument.preparePageLayout_)
        self.assertResultIsBOOL(NSDocument.shouldChangePrintInfo_)
        self.assertArgIsSEL(NSDocument.printDocumentWithSettings_showPrintPanel_delegate_didPrintSelector_contextInfo_, 3, b"v@:@"+objc._C_NSBOOL+b"^v")
        self.assertArgHasType(NSDocument.printDocumentWithSettings_showPrintPanel_delegate_didPrintSelector_contextInfo_, 4, b"^v")
        self.assertArgIsOut(NSDocument.printOperationWithSettings_error_, 1)
        self.assertArgIsSEL(NSDocument.runModalPrintOperation_delegate_didRunSelector_contextInfo_, 2, b"v@:@"+objc._C_NSBOOL+b"^v")
        self.assertArgHasType(NSDocument.runModalPrintOperation_delegate_didRunSelector_contextInfo_, 3, b"^v")
        self.assertResultIsBOOL(NSDocument.isDocumentEdited)
        self.assertResultIsBOOL(NSDocument.hasUndoManager)
        self.assertArgIsBOOL(NSDocument.setHasUndoManager_, 0)
        self.assertResultIsBOOL(NSDocument.presentError_)
        self.assertArgIsSEL(NSDocument.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_, 3, b"v@:"+objc._C_NSBOOL+b"^v")
        self.assertArgHasType(NSDocument.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_, 4, b"^v")
        self.assertArgIsSEL(NSDocument.shouldCloseWindowController_delegate_shouldCloseSelector_contextInfo_, 2, b"v@:@"+objc._C_NSBOOL+b"^v")
        self.assertArgHasType(NSDocument.shouldCloseWindowController_delegate_shouldCloseSelector_contextInfo_, 3, b"^v")
        self.assertResultIsBOOL(NSDocument.isNativeType_)
        self.assertResultIsBOOL(NSDocument.validateUserInterfaceItem_)
        self.assertResultIsBOOL(NSDocument.loadDataRepresentation_ofType_)
        self.assertArgIsBOOL(NSDocument.printShowingPrintPanel_, 0)
        self.assertResultIsBOOL(NSDocument.readFromFile_ofType_)
        self.assertResultIsBOOL(NSDocument.readFromURL_ofType_)
        self.assertResultIsBOOL(NSDocument.revertToSavedFromFile_ofType_)
        self.assertResultIsBOOL(NSDocument.revertToSavedFromURL_ofType_)
        self.assertResultIsBOOL(NSDocument.writeToFile_ofType_)
        self.assertResultIsBOOL(NSDocument.writeToFile_ofType_originalFile_saveOperation_)
        self.assertResultIsBOOL(NSDocument.writeToURL_ofType_)
        self.assertResultIsBOOL(NSDocument.writeWithBackupToFile_ofType_saveOperation_)
        self.assertArgIsSEL(NSDocument.saveToFile_saveOperation_delegate_didSaveSelector_contextInfo_, 3, b'v@:@'+objc._C_NSBOOL+b'^v')
        self.assertArgHasType(NSDocument.saveToFile_saveOperation_delegate_didSaveSelector_contextInfo_, 4, b'^v')


    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSDocument.canConcurrentlyReadDocumentsOfType_)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsBOOL(NSDocument.performActivityWithSynchronousWaiting_usingBlock_, 0)
        self.assertArgIsBlock(NSDocument.performActivityWithSynchronousWaiting_usingBlock_, 1, b'v')
        self.assertArgIsBlock(NSDocument.continueActivityUsingBlock_, 0, b'v')
        self.assertArgIsBlock(NSDocument.continueAsynchronousWorkOnMainThreadUsingBlock_, 0, b'v')
        self.assertArgIsBlock(NSDocument.performSynchronousFileAccessUsingBlock_, 0, b'v')

        self.assertArgIsBlock(NSDocument.performAsynchronousFileAccessUsingBlock_, 0, b'v@?') #FIXME: block has a block argument

        self.assertResultIsBOOL(NSDocument.isEntireFileLoaded)
        self.assertResultIsBOOL(NSDocument.autosavingIsImplicitlyCancellable)

        self.assertArgIsBlock(NSDocument.saveToURL_ofType_forSaveOperation_completionHandler_, 3, b'v@')
        self.assertResultIsBOOL(NSDocument.canAsynchronouslyWriteToURL_ofType_forSaveOperation_)
        self.assertResultIsBOOL(NSDocument.checkAutosavingSafetyAndReturnError_)
        self.assertArgIsOut(NSDocument.checkAutosavingSafetyAndReturnError_, 0)
        self.assertArgIsBOOL(NSDocument.autosaveWithImplicitCancellability_completionHandler_, 0)
        self.assertArgIsBlock(NSDocument.autosaveWithImplicitCancellability_completionHandler_, 1, b'v@')

        self.assertResultIsBOOL(NSDocument.autosavesInPlace)
        self.assertResultIsBOOL(NSDocument.preservesVersions)

        self.assertArgIsSEL(NSDocument.duplicateDocumentWithDelegate_didDuplicateSelector_contextInfo_, 1, b'v@' + objc._C_NSBOOL + b'^v')
        self.assertArgIsOut(NSDocument.duplicateAndReturnError_, 0)
        self.assertResultIsBOOL(NSDocument.isInViewingMode)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertArgIsBOOL(NSDocument.setDraft_, 0)
        self.assertResultIsBOOL(NSDocument.isDraft)
        self.assertResultIsBOOL(NSDocument.autosavesDrafts)

        self.assertArgIsBlock(NSDocument.moveDocumentWithCompletionHandler_, 0,
                b'v' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSDocument.moveToURL_completionHandler_, 1,
                b'v' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSDocument.lockDocumentWithCompletionHandler_, 0,
                b'v' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSDocument.lockWithCompletionHandler_, 0,
                b'v@')
        self.assertArgIsBlock(NSDocument.unlockDocumentWithCompletionHandler_, 0,
                b'v' + objc._C_NSBOOL)
        self.assertArgIsBlock(NSDocument.unlockWithCompletionHandler_, 0,
                b'v@')
        self.assertResultIsBOOL(NSDocument.isLocked)
        self.assertResultIsBOOL(NSDocument.usesUbiquitousStorage)

if __name__ == "__main__":
    main()
