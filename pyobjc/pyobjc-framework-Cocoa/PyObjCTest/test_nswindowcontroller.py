from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSWindowController (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSWindowController.shouldCascadeWindows)
        self.failUnlessArgIsBOOL(NSWindowController.setShouldCascadeWindows_, 0)
        self.failUnlessArgIsBOOL(NSWindowController.setDocumentEdited_, 0)
        self.failUnlessResultIsBOOL(NSWindowController.shouldCloseDocument)
        self.failUnlessArgIsBOOL(NSWindowController.setShouldCloseDocument_, 0)
        self.failUnlessResultIsBOOL(NSWindowController.isWindowLoaded)


if __name__ == "__main__":
    main()
