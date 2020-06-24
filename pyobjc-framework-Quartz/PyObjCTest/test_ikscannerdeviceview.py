from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestIKScannerDeviceView(TestCase):
    @min_os_level("10.10")
    def testProtocolObjects(self):
        objc.protocolNamed("IKScannerDeviceViewDelegate")

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Quartz.IKScannerDeviceViewTransferModeFileBased, 0)
        self.assertEqual(Quartz.IKScannerDeviceViewTransferModeMemoryBased, 1)

        self.assertEqual(Quartz.IKScannerDeviceViewDisplayModeSimple, 0)
        self.assertEqual(Quartz.IKScannerDeviceViewDisplayModeAdvanced, 1)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(Quartz.IKScannerDeviceView.hasDisplayModeSimple)
        self.assertArgIsBOOL(Quartz.IKScannerDeviceView.setHasDisplayModeSimple_, 0)
        self.assertResultIsBOOL(Quartz.IKScannerDeviceView.hasDisplayModeAdvanced)
        self.assertArgIsBOOL(Quartz.IKScannerDeviceView.setHasDisplayModeAdvanced_, 0)
        self.assertResultIsBOOL(
            Quartz.IKScannerDeviceView.displaysDownloadsDirectoryControl
        )
        self.assertArgIsBOOL(
            Quartz.IKScannerDeviceView.setDisplaysDownloadsDirectoryControl_, 0
        )
        self.assertResultIsBOOL(
            Quartz.IKScannerDeviceView.displaysPostProcessApplicationControl
        )
        self.assertArgIsBOOL(
            Quartz.IKScannerDeviceView.setDisplaysPostProcessApplicationControl_, 0
        )
