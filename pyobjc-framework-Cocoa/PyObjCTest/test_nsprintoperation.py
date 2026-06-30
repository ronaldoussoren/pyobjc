import AppKit
import objc
from PyObjCTools.TestSupport import TestCase


class TestNSPrintOperation(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSPrintRenderingQuality)
        self.assertEqual(AppKit.NSPrintRenderingQualityBest, 0)
        self.assertEqual(AppKit.NSPrintRenderingQualityResponsive, 1)

        self.assertIsEnumType(AppKit.NSPrintingPageOrder)
        self.assertEqual(AppKit.NSDescendingPageOrder, -1)
        self.assertEqual(AppKit.NSSpecialPageOrder, 0)
        self.assertEqual(AppKit.NSAscendingPageOrder, 1)
        self.assertEqual(AppKit.NSUnknownPageOrder, 2)

    def test_constants(self):
        self.assertIsInstance(AppKit.NSPrintOperationExistsException, str)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSPrintOperation.isCopyingOperation)
        self.assertResultIsBOOL(AppKit.NSPrintOperation.showsPrintPanel)
        self.assertArgIsBOOL(AppKit.NSPrintOperation.setShowsPrintPanel_, 0)
        self.assertResultIsBOOL(AppKit.NSPrintOperation.showsProgressPanel)
        self.assertArgIsBOOL(AppKit.NSPrintOperation.setShowsProgressPanel_, 0)
        self.assertResultIsBOOL(AppKit.NSPrintOperation.canSpawnSeparateThread)
        self.assertArgIsBOOL(AppKit.NSPrintOperation.setCanSpawnSeparateThread_, 0)

        self.assertArgIsSEL(
            AppKit.NSPrintOperation.runOperationModalForWindow_delegate_didRunSelector_contextInfo_,  # noqa: B950
            2,
            b"v@:@" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSPrintOperation.runOperationModalForWindow_delegate_didRunSelector_contextInfo_,  # noqa: B950
            3,
            b"^v",
        )

        self.assertResultIsBOOL(AppKit.NSPrintOperation.runOperation)
        self.assertResultIsBOOL(AppKit.NSPrintOperation.deliverResult)
        self.assertResultIsBOOL(AppKit.NSPrintOperation.showPanels)
        self.assertArgIsBOOL(AppKit.NSPrintOperation.setShowPanels_, 0)
