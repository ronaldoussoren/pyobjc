import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPrintPanel(TestCase):
    def testProtocols(self):
        objc.protocolNamed("NSPrintPanelAccessorizing")

    def testConstants(self):
        self.assertEqual(AppKit.NSPrintPanelShowsCopies, 0x01)
        self.assertEqual(AppKit.NSPrintPanelShowsPageRange, 0x02)
        self.assertEqual(AppKit.NSPrintPanelShowsPaperSize, 0x04)
        self.assertEqual(AppKit.NSPrintPanelShowsOrientation, 0x08)
        self.assertEqual(AppKit.NSPrintPanelShowsScaling, 0x10)
        self.assertEqual(AppKit.NSPrintPanelShowsPageSetupAccessory, 0x100)
        self.assertEqual(AppKit.NSPrintPanelShowsPreview, 0x20000)

        self.assertIsInstance(AppKit.NSPrintPhotoJobStyleHint, str)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(AppKit.NSPrintPanelAccessorySummaryItemNameKey, str)
        self.assertIsInstance(
            AppKit.NSPrintPanelAccessorySummaryItemDescriptionKey, str
        )

    def testMethods(self):
        self.assertArgIsSEL(
            AppKit.NSPrintPanel.beginSheetWithPrintInfo_modalForWindow_delegate_didEndSelector_contextInfo_,  # noqa: B950
            3,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSPrintPanel.beginSheetWithPrintInfo_modalForWindow_delegate_didEndSelector_contextInfo_,  # noqa: B950
            4,
            b"^v",
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(AppKit.NSPrintPanelShowsPrintSelection, 1 << 5)

        self.assertIsInstance(AppKit.NSPrintAllPresetsJobStyleHint, str)
        self.assertIsInstance(AppKit.NSPrintNoPresetsJobStyleHint, str)
