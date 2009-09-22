from Quartz import *
from PyObjCTools.TestSupport import *

class TestIKScannerDeviceView (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(IKScannerDeviceViewTransferModeFileBased, 0)
        self.failUnlessEqual(IKScannerDeviceViewTransferModeMemoryBased, 1)

        self.failUnlessEqual(IKScannerDeviceViewDisplayModeSimple, 0)
        self.failUnlessEqual(IKScannerDeviceViewDisplayModeAdvanced, 1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(IKScannerDeviceView.hasDisplayModeSimple)
        self.failUnlessArgIsBOOL(IKScannerDeviceView.setHasDisplayModeSimple_, 0)
        self.failUnlessResultIsBOOL(IKScannerDeviceView.hasDisplayModeAdvanced)
        self.failUnlessArgIsBOOL(IKScannerDeviceView.setHasDisplayModeAdvanced_, 0)
        self.failUnlessResultIsBOOL(IKScannerDeviceView.displaysDownloadsDirectoryControl)
        self.failUnlessArgIsBOOL(IKScannerDeviceView.setDisplaysDownloadsDirectoryControl_, 0)
        self.failUnlessResultIsBOOL(IKScannerDeviceView.displaysPostProcessApplicationControl)
        self.failUnlessArgIsBOOL(IKScannerDeviceView.setDisplaysPostProcessApplicationControl_, 0)

if __name__ == "__main__":
    main()
