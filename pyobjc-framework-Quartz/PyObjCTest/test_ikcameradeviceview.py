from PyObjCTools.TestSupport import TestCase
import Quartz


class TestIKCameraDeviceView(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Quartz.IKCameraDeviceViewDisplayMode)
        self.assertEqual(Quartz.IKCameraDeviceViewDisplayModeNone, -1)
        self.assertEqual(Quartz.IKCameraDeviceViewDisplayModeTable, 0)
        self.assertEqual(Quartz.IKCameraDeviceViewDisplayModeIcon, 1)

        self.assertIsEnumType(Quartz.IKCameraDeviceViewTransferMode)
        self.assertEqual(Quartz.IKCameraDeviceViewTransferModeFileBased, 0)
        self.assertEqual(Quartz.IKCameraDeviceViewTransferModeMemoryBased, 1)

    def test_methods(self):
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

    def test_protocols(self):
        self.assertProtocolExists("IKCameraDeviceViewDelegate", Quartz)
