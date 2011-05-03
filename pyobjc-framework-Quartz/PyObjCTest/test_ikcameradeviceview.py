from Quartz import *
from PyObjCTools.TestSupport import *


class TestIKCameraDeviceView (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(IKCameraDeviceViewDisplayModeTable, 0)
        self.assertEqual(IKCameraDeviceViewDisplayModeIcon, 1)

        self.assertEqual(IKCameraDeviceViewTransferModeFileBased, 0)
        self.assertEqual(IKCameraDeviceViewTransferModeMemoryBased, 1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(IKCameraDeviceView.hasDisplayModeTable)
        self.assertArgIsBOOL(IKCameraDeviceView.setHasDisplayModeTable_, 0)

        self.assertResultIsBOOL(IKCameraDeviceView.hasDisplayModeIcon)
        self.assertArgIsBOOL(IKCameraDeviceView.setHasDisplayModeIcon_, 0)

        self.assertResultIsBOOL(IKCameraDeviceView.displaysDownloadsDirectoryControl)
        self.assertArgIsBOOL(IKCameraDeviceView.setDisplaysDownloadsDirectoryControl_, 0)

        self.assertResultIsBOOL(IKCameraDeviceView.displaysPostProcessApplicationControl)
        self.assertArgIsBOOL(IKCameraDeviceView.setDisplaysPostProcessApplicationControl_, 0)
        self.assertResultIsBOOL(IKCameraDeviceView.canRotateSelectedItemsLeft)
        self.assertResultIsBOOL(IKCameraDeviceView.canRotateSelectedItemsRight)
        self.assertResultIsBOOL(IKCameraDeviceView.canDeleteSelectedItems)
        self.assertResultIsBOOL(IKCameraDeviceView.canDeleteSelectedItems)


        self.assertArgIsBOOL(IKCameraDeviceView.selectIndexes_byExtendingSelection_, 1)

if __name__ == "__main__":
    main()
