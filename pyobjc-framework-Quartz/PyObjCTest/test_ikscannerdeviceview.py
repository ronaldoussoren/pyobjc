from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Quartz


class TestIKScannerDeviceView(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Quartz.IKScannerDeviceViewTransferMode)
        self.assertEqual(Quartz.IKScannerDeviceViewTransferModeFileBased, 0)
        self.assertEqual(Quartz.IKScannerDeviceViewTransferModeMemoryBased, 1)

        self.assertIsEnumType(Quartz.IKScannerDeviceViewDisplayMode)
        self.assertEqual(Quartz.IKScannerDeviceViewDisplayModeSimple, 0)
        self.assertEqual(Quartz.IKScannerDeviceViewDisplayModeAdvanced, 1)

    @min_sdk_level("10.10")
    def test_protocols(self):
        self.assertProtocolExists("IKScannerDeviceViewDelegate", Quartz)

    def test_methods(self):
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
