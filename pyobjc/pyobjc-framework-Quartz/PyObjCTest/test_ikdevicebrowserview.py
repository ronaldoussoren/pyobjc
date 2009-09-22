from Quartz import *
from PyObjCTools.TestSupport import *


class TestIKDeviceBrowserView (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(IKDeviceBrowserViewDisplayModeTable, 0)
        self.failUnlessEqual(IKDeviceBrowserViewDisplayModeOutline, 1)
        self.failUnlessEqual(IKDeviceBrowserViewDisplayModeIcon, 2)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(IKDeviceBrowserView.displaysLocalCameras)
        self.failUnlessArgIsBOOL(IKDeviceBrowserView.setDisplaysLocalCameras_, 0)
        self.failUnlessResultIsBOOL(IKDeviceBrowserView.displaysNetworkCameras)
        self.failUnlessArgIsBOOL(IKDeviceBrowserView.setDisplaysNetworkCameras_, 0)

        self.failUnlessResultIsBOOL(IKDeviceBrowserView.displaysLocalScanners)
        self.failUnlessArgIsBOOL(IKDeviceBrowserView.setDisplaysLocalScanners_, 0)

        self.failUnlessResultIsBOOL(IKDeviceBrowserView.displaysNetworkScanners)
        self.failUnlessArgIsBOOL(IKDeviceBrowserView.setDisplaysNetworkScanners_, 0)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
