import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPDFPanel(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSPDFPanelOptions)

    def testConstants(self):
        self.assertEqual(AppKit.NSPDFPanelShowsPaperSize, 1 << 2)
        self.assertEqual(AppKit.NSPDFPanelShowsOrientation, 1 << 3)
        self.assertEqual(AppKit.NSPDFPanelRequestsParentDirectory, 1 << 24)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertArgIsBlock(
            AppKit.NSPDFPanel.beginSheetWithPDFInfo_modalForWindow_completionHandler_,
            2,
            objc._C_VOID + objc._C_NSInteger,
        )
