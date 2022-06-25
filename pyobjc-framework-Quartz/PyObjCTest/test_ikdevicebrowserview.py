from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestIKDeviceBrowserView(TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Quartz.IKDeviceBrowserViewDisplayModeTable, 0)
        self.assertEqual(Quartz.IKDeviceBrowserViewDisplayModeOutline, 1)
        self.assertEqual(Quartz.IKDeviceBrowserViewDisplayModeIcon, 2)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(Quartz.IKDeviceBrowserView.displaysLocalCameras)
        self.assertArgIsBOOL(Quartz.IKDeviceBrowserView.setDisplaysLocalCameras_, 0)

        self.assertResultIsBOOL(Quartz.IKDeviceBrowserView.displaysNetworkCameras)
        self.assertArgIsBOOL(Quartz.IKDeviceBrowserView.setDisplaysNetworkCameras_, 0)

        self.assertResultIsBOOL(Quartz.IKDeviceBrowserView.displaysLocalScanners)
        self.assertArgIsBOOL(Quartz.IKDeviceBrowserView.setDisplaysLocalScanners_, 0)

        self.assertResultIsBOOL(Quartz.IKDeviceBrowserView.displaysNetworkScanners)
        self.assertArgIsBOOL(Quartz.IKDeviceBrowserView.setDisplaysNetworkScanners_, 0)

    @min_os_level("10.10")
    def testProtocols(self):
        self.assertProtocolExists("IKDeviceBrowserViewDelegate")
