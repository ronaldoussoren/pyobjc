from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSWindowController (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSWindowController.shouldCascadeWindows)
        self.assertArgIsBOOL(NSWindowController.setShouldCascadeWindows_, 0)
        self.assertArgIsBOOL(NSWindowController.setDocumentEdited_, 0)
        self.assertResultIsBOOL(NSWindowController.shouldCloseDocument)
        self.assertArgIsBOOL(NSWindowController.setShouldCloseDocument_, 0)
        self.assertResultIsBOOL(NSWindowController.isWindowLoaded)


if __name__ == "__main__":
    main()
