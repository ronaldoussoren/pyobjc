
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPrintPanel (TestCase):

    def testConstants(self):
        self.assertEqual(NSPrintPanelShowsCopies, 0x01)
        self.assertEqual(NSPrintPanelShowsPageRange, 0x02)
        self.assertEqual(NSPrintPanelShowsPaperSize, 0x04)
        self.assertEqual(NSPrintPanelShowsOrientation, 0x08)
        self.assertEqual(NSPrintPanelShowsScaling, 0x10)
        self.assertEqual(NSPrintPanelShowsPageSetupAccessory, 0x100)
        self.assertEqual(NSPrintPanelShowsPreview, 0x20000)

        self.assertIsInstance(NSPrintPhotoJobStyleHint, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(NSPrintPanelAccessorySummaryItemNameKey, unicode)
        self.assertIsInstance(NSPrintPanelAccessorySummaryItemDescriptionKey, unicode)

    def testMethods(self):
        self.assertArgIsSEL(NSPrintPanel.beginSheetWithPrintInfo_modalForWindow_delegate_didEndSelector_contextInfo_, 3, b'v@:@' + objc._C_NSInteger + b'^v')
        self.assertArgHasType(NSPrintPanel.beginSheetWithPrintInfo_modalForWindow_delegate_didEndSelector_contextInfo_, 4, b'^v')

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSPrintPanelShowsPrintSelection, 1 << 5)

        self.assertIsInstance(NSPrintAllPresetsJobStyleHint, unicode)
        self.assertIsInstance(NSPrintNoPresetsJobStyleHint, unicode)


if __name__ == "__main__":
    main()
