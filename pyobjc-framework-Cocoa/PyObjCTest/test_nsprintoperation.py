
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPrintOperation (TestCase):
    def testConstants(self):
        self.assertEqual(NSDescendingPageOrder, -1)
        self.assertEqual(NSSpecialPageOrder, 0)
        self.assertEqual(NSAscendingPageOrder, 1)
        self.assertEqual(NSUnknownPageOrder, 2)

        self.assertIsInstance(NSPrintOperationExistsException, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSPrintOperation.isCopyingOperation)
        self.assertResultIsBOOL(NSPrintOperation.showsPrintPanel)
        self.assertArgIsBOOL(NSPrintOperation.setShowsPrintPanel_, 0)
        self.assertResultIsBOOL(NSPrintOperation.showsProgressPanel)
        self.assertArgIsBOOL(NSPrintOperation.setShowsProgressPanel_, 0)
        self.assertResultIsBOOL(NSPrintOperation.canSpawnSeparateThread)
        self.assertArgIsBOOL(NSPrintOperation.setCanSpawnSeparateThread_, 0)

        self.assertArgIsSEL(NSPrintOperation.runOperationModalForWindow_delegate_didRunSelector_contextInfo_, 2, b'v@:@' + objc._C_NSBOOL + b'^v')
        self.assertArgHasType(NSPrintOperation.runOperationModalForWindow_delegate_didRunSelector_contextInfo_, 3, b'^v')

        self.assertResultIsBOOL(NSPrintOperation.runOperation)
        self.assertResultIsBOOL(NSPrintOperation.deliverResult)
        self.assertResultIsBOOL(NSPrintOperation.showPanels)
        self.assertArgIsBOOL(NSPrintOperation.setShowPanels_, 0)


if __name__ == "__main__":
    main()
