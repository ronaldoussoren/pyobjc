import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSDocumentController(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            AppKit.NSDocumentController.openUntitledDocumentAndDisplay_error_, 0
        )
        self.assertArgIsOut(
            AppKit.NSDocumentController.openUntitledDocumentAndDisplay_error_, 1
        )
        self.assertArgIsOut(
            AppKit.NSDocumentController.makeUntitledDocumentOfType_error_, 1
        )
        self.assertArgIsBOOL(
            AppKit.NSDocumentController.openDocumentWithContentsOfURL_display_error_, 1
        )
        self.assertArgIsOut(
            AppKit.NSDocumentController.openDocumentWithContentsOfURL_display_error_, 2
        )
        self.assertArgIsOut(
            AppKit.NSDocumentController.makeDocumentWithContentsOfURL_ofType_error_, 2
        )
        self.assertResultIsBOOL(
            AppKit.NSDocumentController.reopenDocumentForURL_withContentsOfURL_error_
        )
        self.assertArgIsOut(
            AppKit.NSDocumentController.reopenDocumentForURL_withContentsOfURL_error_, 2
        )
        self.assertArgIsOut(
            AppKit.NSDocumentController.makeDocumentForURL_withContentsOfURL_ofType_error_,
            3,
        )
        self.assertResultIsBOOL(AppKit.NSDocumentController.hasEditedDocuments)
        self.assertArgIsBOOL(
            AppKit.NSDocumentController.reviewUnsavedDocumentsWithAlertTitle_cancellable_delegate_didReviewAllSelector_contextInfo_,  # noqa: B950
            1,
        )
        self.assertArgIsSEL(
            AppKit.NSDocumentController.reviewUnsavedDocumentsWithAlertTitle_cancellable_delegate_didReviewAllSelector_contextInfo_,  # noqa: B950
            3,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocumentController.reviewUnsavedDocumentsWithAlertTitle_cancellable_delegate_didReviewAllSelector_contextInfo_,  # noqa: B950
            4,
            b"^v",
        )
        self.assertArgIsSEL(
            AppKit.NSDocumentController.closeAllDocumentsWithDelegate_didCloseAllSelector_contextInfo_,  # noqa: B950
            1,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocumentController.closeAllDocumentsWithDelegate_didCloseAllSelector_contextInfo_,  # noqa: B950
            2,
            b"^v",
        )
        self.assertArgIsSEL(
            AppKit.NSDocumentController.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_,  # noqa: B950
            3,
            b"v@:" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSDocumentController.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_,  # noqa: B950
            4,
            b"^v",
        )
        self.assertResultIsBOOL(AppKit.NSDocumentController.presentError_)
        self.assertArgIsOut(AppKit.NSDocumentController.typeForContentsOfURL_error_, 1)
        self.assertResultIsBOOL(AppKit.NSDocumentController.validateUserInterfaceItem_)
        self.assertArgIsBOOL(
            AppKit.NSDocumentController.openDocumentWithContentsOfFile_display_, 1
        )
        self.assertArgIsBOOL(
            AppKit.NSDocumentController.openDocumentWithContentsOfURL_display_, 1
        )
        self.assertArgIsBOOL(
            AppKit.NSDocumentController.openUntitledDocumentOfType_display_, 1
        )
        self.assertArgIsBOOL(AppKit.NSDocumentController.setShouldCreateUI_, 0)
        self.assertResultIsBOOL(AppKit.NSDocumentController.shouldCreateUI)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBOOL(
            AppKit.NSDocumentController.openDocumentWithContentsOfURL_display_completionHandler_,  # noqa: B950
            1,
        )
        self.assertArgIsBlock(
            AppKit.NSDocumentController.openDocumentWithContentsOfURL_display_completionHandler_,  # noqa: B950
            2,
            b"v@",
        )
        self.assertArgIsBOOL(
            AppKit.NSDocumentController.reopenDocumentForURL_withContentsOfURL_display_completionHandler_,  # noqa: B950
            2,
        )
        self.assertArgIsBlock(
            AppKit.NSDocumentController.reopenDocumentForURL_withContentsOfURL_display_completionHandler_,  # noqa: B950
            3,
            b"v@" + objc._C_NSBOOL + b"@",
        )
        self.assertArgIsBOOL(
            AppKit.NSDocumentController.duplicateDocumentWithContentsOfURL_copying_displayName_error_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            AppKit.NSDocumentController.duplicateDocumentWithContentsOfURL_copying_displayName_error_,  # noqa: B950
            3,
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertArgIsBlock(
            AppKit.NSDocumentController.beginOpenPanelWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            AppKit.NSDocumentController.beginOpenPanel_forTypes_completionHandler_,
            2,
            b"v" + objc._C_NSInteger,
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(AppKit.NSDocumentController.allowsAutomaticShareMenu)
