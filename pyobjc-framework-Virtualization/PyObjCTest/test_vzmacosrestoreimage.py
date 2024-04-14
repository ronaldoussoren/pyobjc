from PyObjCTools.TestSupport import TestCase, min_os_level, arch_only

import Virtualization


class TestVZMacOSRestoreImage(TestCase):
    @min_os_level("12.0")
    @arch_only("arm64")
    def test_methods(self):
        self.assertArgIsBlock(
            Virtualization.VZMacOSRestoreImage.loadFileURL_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            Virtualization.VZMacOSRestoreImage.fetchLatestSupportedWithCompletionHandler_,
            0,
            b"v@@",
        )

    @min_os_level("13.0")
    @arch_only("arm64")
    def test_methods13_0(self):
        self.assertResultIsBOOL(Virtualization.VZMacOSRestoreImage.isSupported)
