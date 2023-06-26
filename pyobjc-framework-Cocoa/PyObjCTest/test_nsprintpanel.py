import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPrintPanel(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSPrintPanelAccessorySummaryKey, str)
        self.assertIsTypedEnum(AppKit.NSPrintPanelJobStyleHint, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSPrintPanelOptions)

    def testProtocols(self):
        self.assertProtocolExists("NSPrintPanelAccessorizing")

    def testConstants(self):
        self.assertEqual(AppKit.NSPrintPanelShowsCopies, 0x01)
        self.assertEqual(AppKit.NSPrintPanelShowsPageRange, 0x02)
        self.assertEqual(AppKit.NSPrintPanelShowsPaperSize, 0x04)
        self.assertEqual(AppKit.NSPrintPanelShowsOrientation, 0x08)
        self.assertEqual(AppKit.NSPrintPanelShowsScaling, 0x10)
        self.assertEqual(AppKit.NSPrintPanelShowsPageSetupAccessory, 0x100)
        self.assertEqual(AppKit.NSPrintPanelShowsPreview, 0x20000)

        self.assertIsInstance(AppKit.NSPrintPhotoJobStyleHint, str)

        self.assertIsEnumType(AppKit.NSPrintPanelResult)
        self.assertEqual(AppKit.NSPrintPanelResultCancelled, 0)
        self.assertEqual(AppKit.NSPrintPanelResultPrinted, 1)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(AppKit.NSPrintPanelAccessorySummaryItemNameKey, str)
        self.assertIsInstance(
            AppKit.NSPrintPanelAccessorySummaryItemDescriptionKey, str
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(AppKit.NSPrintPanelShowsPrintSelection, 1 << 5)

        self.assertIsInstance(AppKit.NSPrintAllPresetsJobStyleHint, str)
        self.assertIsInstance(AppKit.NSPrintNoPresetsJobStyleHint, str)

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

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsBlock(
            AppKit.NSPrintPanel.beginSheetUsingPrintInfo_onWindow_completionHandler_,
            2,
            b"vq",
        )
