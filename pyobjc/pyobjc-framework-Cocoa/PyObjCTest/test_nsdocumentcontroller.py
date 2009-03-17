
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSDocumentController (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSDocumentController.openUntitledDocumentAndDisplay_error_, 0)
        self.failUnlessArgIsOut(NSDocumentController.openUntitledDocumentAndDisplay_error_, 1)
        self.failUnlessArgIsOut(NSDocumentController.makeUntitledDocumentOfType_error_, 1)
        self.failUnlessArgIsBOOL(NSDocumentController.openDocumentWithContentsOfURL_display_error_, 1)
        self.failUnlessArgIsOut(NSDocumentController.openDocumentWithContentsOfURL_display_error_, 2)
        self.failUnlessArgIsOut(NSDocumentController.makeDocumentWithContentsOfURL_ofType_error_, 2)
        self.failUnlessResultIsBOOL(NSDocumentController.reopenDocumentForURL_withContentsOfURL_error_)
        self.failUnlessArgIsOut(NSDocumentController.reopenDocumentForURL_withContentsOfURL_error_, 2)
        self.failUnlessArgIsOut(NSDocumentController.makeDocumentForURL_withContentsOfURL_ofType_error_, 3)
        self.failUnlessResultIsBOOL(NSDocumentController.hasEditedDocuments)
        self.failUnlessArgIsBOOL(NSDocumentController.reviewUnsavedDocumentsWithAlertTitle_cancellable_delegate_didReviewAllSelector_contextInfo_, 1)
        self.failUnlessArgIsSEL(NSDocumentController.reviewUnsavedDocumentsWithAlertTitle_cancellable_delegate_didReviewAllSelector_contextInfo_, 3, 'v@:@'+objc._C_NSBOOL+'^v')
        self.failUnlessArgHasType(NSDocumentController.reviewUnsavedDocumentsWithAlertTitle_cancellable_delegate_didReviewAllSelector_contextInfo_, 4, '^v')
        self.failUnlessArgIsSEL(NSDocumentController.closeAllDocumentsWithDelegate_didCloseAllSelector_contextInfo_, 1, 'v@:@'+objc._C_NSBOOL+'^v')
        self.failUnlessArgHasType(NSDocumentController.closeAllDocumentsWithDelegate_didCloseAllSelector_contextInfo_, 2, '^v')
        self.failUnlessArgIsSEL(NSDocumentController.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_, 3, 'v@:'+objc._C_NSBOOL+'^v')
        self.failUnlessArgHasType(NSDocumentController.presentError_modalForWindow_delegate_didPresentSelector_contextInfo_, 4, '^v')
        self.failUnlessResultIsBOOL(NSDocumentController.presentError_)
        self.failUnlessArgIsOut(NSDocumentController.typeForContentsOfURL_error_, 1)
        self.failUnlessResultIsBOOL(NSDocumentController.validateUserInterfaceItem_)
        self.failUnlessArgIsBOOL(NSDocumentController.openDocumentWithContentsOfFile_display_, 1)
        self.failUnlessArgIsBOOL(NSDocumentController.openDocumentWithContentsOfURL_display_, 1)
        self.failUnlessArgIsBOOL(NSDocumentController.openUntitledDocumentOfType_display_, 1)
        self.failUnlessArgIsBOOL(NSDocumentController.setShouldCreateUI_, 0)
        self.failUnlessResultIsBOOL(NSDocumentController.shouldCreateUI)


if __name__ == "__main__":
    main()
