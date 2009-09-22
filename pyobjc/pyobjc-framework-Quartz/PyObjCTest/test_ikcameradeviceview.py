from Quartz import *
from PyObjCTools.TestSupport import *


class TestIKCameraDeviceView (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(IKCameraDeviceViewDisplayModeTable, 0)
        self.failUnlessEqual(IKCameraDeviceViewDisplayModeIcon, 1)

        self.failUnlessEqual(IKCameraDeviceViewTransferModeFileBased, 0)
        self.failUnlessEqual(IKCameraDeviceViewTransferModeMemoryBased, 1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(IKCameraDeviceView.hasDisplayModeTable)
        self.failUnlessArgIsBOOL(IKCameraDeviceView.setHasDisplayModeTable_, 0)

        self.failUnlessResultIsBOOL(IKCameraDeviceView.hasDisplayModeIcon)
        self.failUnlessArgIsBOOL(IKCameraDeviceView.setHasDisplayModeIcon_, 0)

        self.failUnlessResultIsBOOL(IKCameraDeviceView.displaysDownloadsDirectoryControl)
        self.failUnlessArgIsBOOL(IKCameraDeviceView.setDisplaysDownloadsDirectoryControl_, 0)

        self.failUnlessResultIsBOOL(IKCameraDeviceView.displaysPostProcessApplicationControl)
        self.failUnlessArgIsBOOL(IKCameraDeviceView.setDisplaysPostProcessApplicationControl_, 0)
        self.failUnlessResultIsBOOL(IKCameraDeviceView.canRotateSelectedItemsLeft)
        self.failUnlessResultIsBOOL(IKCameraDeviceView.canRotateSelectedItemsRight)
        self.failUnlessResultIsBOOL(IKCameraDeviceView.canDeleteSelectedItems)
        self.failUnlessResultIsBOOL(IKCameraDeviceView.canDeleteSelectedItems)


        self.failUnlessArgIsBOOL(IKCameraDeviceView.selectIndexes_byExtendingSelection_, 1)

if __name__ == "__main__":
    main()
