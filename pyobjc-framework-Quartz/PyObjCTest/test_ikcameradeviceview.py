from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import Quartz


class TestIKCameraDeviceView(TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Quartz.IKCameraDeviceViewDisplayModeNone, -1)
        self.assertEqual(Quartz.IKCameraDeviceViewDisplayModeTable, 0)
        self.assertEqual(Quartz.IKCameraDeviceViewDisplayModeIcon, 1)

        self.assertEqual(Quartz.IKCameraDeviceViewTransferModeFileBased, 0)
        self.assertEqual(Quartz.IKCameraDeviceViewTransferModeMemoryBased, 1)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(Quartz.IKCameraDeviceView.hasDisplayModeTable)
        self.assertArgIsBOOL(Quartz.IKCameraDeviceView.setHasDisplayModeTable_, 0)

        self.assertResultIsBOOL(Quartz.IKCameraDeviceView.hasDisplayModeIcon)
        self.assertArgIsBOOL(Quartz.IKCameraDeviceView.setHasDisplayModeIcon_, 0)

        self.assertResultIsBOOL(
            Quartz.IKCameraDeviceView.displaysDownloadsDirectoryControl
        )
        self.assertArgIsBOOL(
            Quartz.IKCameraDeviceView.setDisplaysDownloadsDirectoryControl_, 0
        )

        self.assertResultIsBOOL(
            Quartz.IKCameraDeviceView.displaysPostProcessApplicationControl
        )
        self.assertArgIsBOOL(
            Quartz.IKCameraDeviceView.setDisplaysPostProcessApplicationControl_, 0
        )

        self.assertResultIsBOOL(Quartz.IKCameraDeviceView.canRotateSelectedItemsLeft)
        self.assertResultIsBOOL(Quartz.IKCameraDeviceView.canRotateSelectedItemsRight)
        self.assertResultIsBOOL(Quartz.IKCameraDeviceView.canDeleteSelectedItems)
        self.assertResultIsBOOL(Quartz.IKCameraDeviceView.canDownloadSelectedItems)

        self.assertArgIsBOOL(
            Quartz.IKCameraDeviceView.selectIndexes_byExtendingSelection_, 1
        )

    @min_sdk_level("10.10")
    def testProtocols(self):
        self.assertProtocolExists("IKCameraDeviceViewDelegate")
