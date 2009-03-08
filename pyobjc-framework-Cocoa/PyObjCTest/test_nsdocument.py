
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSDocument (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSChangeDone, 0)
        self.failUnlessEqual(NSChangeUndone, 1)
        self.failUnlessEqual(NSChangeCleared, 2)
        self.failUnlessEqual(NSChangeRedone, 5)
        self.failUnlessEqual(NSChangeReadOtherContents, 3)
        self.failUnlessEqual(NSChangeAutosaved, 4)

        self.failUnlessEqual(NSSaveOperation, 0)
        self.failUnlessEqual(NSSaveAsOperation, 1)
        self.failUnlessEqual(NSSaveToOperation, 2)
        self.failUnlessEqual(NSAutosaveOperation, 3)

    def testMethods(self):
        self.fail("- (void)saveDocumentWithDelegate:(id)delegate didSaveSelector:(SEL)didSaveSelector contextInfo:(void *)contextInfo;")
        self.fail("- (void)runModalSavePanelForSaveOperation:(NSSaveOperationType)saveOperation delegate:(id)delegate didSaveSelector:(SEL)didSaveSelector contextInfo:(void *)contextInfo;")
        self.fail("- (void)saveToURL:(NSURL *)absoluteURL ofType:(NSString *)typeName forSaveOperation:(NSSaveOperationType)saveOperation delegate:(id)delegate didSaveSelector:(SEL)didSaveSelector contextInfo:(void *)contextInfo;")
        self.fail("- (void)autosaveDocumentWithDelegate:(id)delegate didAutosaveSelector:(SEL)didAutosaveSelector contextInfo:(void *)contextInfo;")
        self.fail("- (void)canCloseDocumentWithDelegate:(id)delegate shouldCloseSelector:(SEL)shouldCloseSelector contextInfo:(void *)contextInfo;")
        self.fail("- (void)runModalPageLayoutWithPrintInfo:(NSPrintInfo *)printInfo delegate:(id)delegate didRunSelector:(SEL)didRunSelector contextInfo:(void *)contextInfo;")
        self.fail("- (void)printDocumentWithSettings:(NSDictionary *)printSettings showPrintPanel:(BOOL)showPrintPanel delegate:(id)delegate didPrintSelector:(SEL)didPrintSelector contextInfo:(void *)contextInfo;")
        self.fail("- (void)runModalPrintOperation:(NSPrintOperation *)printOperation delegate:(id)delegate didRunSelector:(SEL)didRunSelector contextInfo:(void *)contextInfo;")
        self.fail("- (void)presentError:(NSError *)error modalForWindow:(NSWindow *)window delegate:(id)delegate didPresentSelector:(SEL)didPresentSelector contextInfo:(void *)contextInfo;")
        self.fail("- (void)shouldCloseWindowController:(NSWindowController *)windowController delegate:(id)delegate shouldCloseSelector:(SEL)shouldCloseSelector contextInfo:(void *)contextInfo;")


if __name__ == "__main__":
    main()
