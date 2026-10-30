import AppKit
import objc
from PyObjCTools.TestSupport import TestCase


class TestNSPDFPanel(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSPDFPanelOptions)
        self.assertEqual(AppKit.NSPDFPanelShowsPaperSize, 1 << 2)
        self.assertEqual(AppKit.NSPDFPanelShowsOrientation, 1 << 3)
        self.assertEqual(AppKit.NSPDFPanelRequestsParentDirectory, 1 << 24)

    def test_methods(self):
        self.assertArgIsBlock(
            AppKit.NSPDFPanel.beginSheetWithPDFInfo_modalForWindow_completionHandler_,
            2,
            objc._C_VOID + objc._C_NSInteger,
        )
