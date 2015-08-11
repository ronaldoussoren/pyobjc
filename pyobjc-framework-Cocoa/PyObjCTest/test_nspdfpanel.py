from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPDFPanel (TestCase):
    def testConstants(self):
        self.assertEqual(NSPDFPanelShowsPaperSize, 1 << 2)
        self.assertEqual(NSPDFPanelShowsOrientation, 1 << 3)
        self.assertEqual(NSPDFPanelRequestsParentDirectory, 1 << 24)

    @min_os_level('10.9')
    def testMethods(self):
        self.assertArgIsBlock(NSPDFPanel.beginSheetWithPDFInfo_modalForWindow_completionHandler_, 2, objc._C_VOID + objc._C_NSInteger)

if __name__ == "__main__":
    main()
