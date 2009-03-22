
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
        self.failUnlessResultIsBOOL(NSPrintOperation.isCopyingOperation)
        self.failUnlessResultIsBOOL(NSPrintOperation.showsPrintPanel)
        self.failUnlessArgIsBOOL(NSPrintOperation.setShowsPrintPanel_, 0)
        self.failUnlessResultIsBOOL(NSPrintOperation.showsProgressPanel)
        self.failUnlessArgIsBOOL(NSPrintOperation.setShowsProgressPanel_, 0)
        self.failUnlessResultIsBOOL(NSPrintOperation.canSpawnSeparateThread)
        self.failUnlessArgIsBOOL(NSPrintOperation.setCanSpawnSeparateThread_, 0)

        self.failUnlessArgIsSEL(NSPrintOperation.runOperationModalForWindow_delegate_didRunSelector_contextInfo_, 2, 'v@:@' + objc._C_NSBOOL + '^v')
        self.failUnlessArgHasType(NSPrintOperation.runOperationModalForWindow_delegate_didRunSelector_contextInfo_, 3, '^v')

        self.failUnlessResultIsBOOL(NSPrintOperation.runOperation)
        self.failUnlessResultIsBOOL(NSPrintOperation.deliverResult)
        self.failUnlessResultIsBOOL(NSPrintOperation.showPanels)
        self.failUnlessArgIsBOOL(NSPrintOperation.setShowPanels_, 0)


if __name__ == "__main__":
    main()
