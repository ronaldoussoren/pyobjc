from Quartz import *
from PyObjCTools.TestSupport import *


class TestIKDeviceBrowserView (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(IKDeviceBrowserViewDisplayModeTable, 0)
        self.assertEqual(IKDeviceBrowserViewDisplayModeOutline, 1)
        self.assertEqual(IKDeviceBrowserViewDisplayModeIcon, 2)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(IKDeviceBrowserView.displaysLocalCameras)
        self.assertArgIsBOOL(IKDeviceBrowserView.setDisplaysLocalCameras_, 0)
        self.assertResultIsBOOL(IKDeviceBrowserView.displaysNetworkCameras)
        self.assertArgIsBOOL(IKDeviceBrowserView.setDisplaysNetworkCameras_, 0)

        self.assertResultIsBOOL(IKDeviceBrowserView.displaysLocalScanners)
        self.assertArgIsBOOL(IKDeviceBrowserView.setDisplaysLocalScanners_, 0)

        self.assertResultIsBOOL(IKDeviceBrowserView.displaysNetworkScanners)
        self.assertArgIsBOOL(IKDeviceBrowserView.setDisplaysNetworkScanners_, 0)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
