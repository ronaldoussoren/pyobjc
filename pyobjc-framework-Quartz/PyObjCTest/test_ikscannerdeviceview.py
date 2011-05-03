from Quartz import *
from PyObjCTools.TestSupport import *

class TestIKScannerDeviceView (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(IKScannerDeviceViewTransferModeFileBased, 0)
        self.assertEqual(IKScannerDeviceViewTransferModeMemoryBased, 1)

        self.assertEqual(IKScannerDeviceViewDisplayModeSimple, 0)
        self.assertEqual(IKScannerDeviceViewDisplayModeAdvanced, 1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(IKScannerDeviceView.hasDisplayModeSimple)
        self.assertArgIsBOOL(IKScannerDeviceView.setHasDisplayModeSimple_, 0)
        self.assertResultIsBOOL(IKScannerDeviceView.hasDisplayModeAdvanced)
        self.assertArgIsBOOL(IKScannerDeviceView.setHasDisplayModeAdvanced_, 0)
        self.assertResultIsBOOL(IKScannerDeviceView.displaysDownloadsDirectoryControl)
        self.assertArgIsBOOL(IKScannerDeviceView.setDisplaysDownloadsDirectoryControl_, 0)
        self.assertResultIsBOOL(IKScannerDeviceView.displaysPostProcessApplicationControl)
        self.assertArgIsBOOL(IKScannerDeviceView.setDisplaysPostProcessApplicationControl_, 0)

if __name__ == "__main__":
    main()
