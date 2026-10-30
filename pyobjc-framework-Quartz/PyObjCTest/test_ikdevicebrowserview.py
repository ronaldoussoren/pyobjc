from PyObjCTools.TestSupport import TestCase
import Quartz


class TestIKDeviceBrowserView(TestCase):
    def test_constants(self):
        self.assertEqual(Quartz.IKDeviceBrowserViewDisplayModeTable, 0)
        self.assertEqual(Quartz.IKDeviceBrowserViewDisplayModeOutline, 1)
        self.assertEqual(Quartz.IKDeviceBrowserViewDisplayModeIcon, 2)

    def test_methods(self):
        self.assertResultIsBOOL(Quartz.IKDeviceBrowserView.displaysLocalCameras)
        self.assertArgIsBOOL(Quartz.IKDeviceBrowserView.setDisplaysLocalCameras_, 0)

        self.assertResultIsBOOL(Quartz.IKDeviceBrowserView.displaysNetworkCameras)
        self.assertArgIsBOOL(Quartz.IKDeviceBrowserView.setDisplaysNetworkCameras_, 0)

        self.assertResultIsBOOL(Quartz.IKDeviceBrowserView.displaysLocalScanners)
        self.assertArgIsBOOL(Quartz.IKDeviceBrowserView.setDisplaysLocalScanners_, 0)

        self.assertResultIsBOOL(Quartz.IKDeviceBrowserView.displaysNetworkScanners)
        self.assertArgIsBOOL(Quartz.IKDeviceBrowserView.setDisplaysNetworkScanners_, 0)

    def test_protocols(self):
        self.assertProtocolExists("IKDeviceBrowserViewDelegate", Quartz)
