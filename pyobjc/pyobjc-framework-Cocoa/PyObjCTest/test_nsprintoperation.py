
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPrintOperation (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSDescendingPageOrder, -1)
        self.failUnlessEqual(NSSpecialPageOrder, 0)
        self.failUnlessEqual(NSAscendingPageOrder, 1)
        self.failUnlessEqual(NSUnknownPageOrder, 2)

        self.failUnlessIsInstance(NSPrintOperationExistsException, unicode)

    def testMethods(self):
        self.fail("- (void)runOperationModalForWindow:(NSWindow *)docWindow delegate:(id)delegate didRunSelector:(SEL)didRunSelector contextInfo:(void *)contextInfo;")



if __name__ == "__main__":
    main()
