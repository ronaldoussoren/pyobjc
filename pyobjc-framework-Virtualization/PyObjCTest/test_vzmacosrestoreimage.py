from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZMacOSRestoreImage(TestCase):
    @min_os_level("12.0")
    def test_methods(self):
        self.assertArgIsBlock(
            Virtualization.VZMacOSRestoreImage.loadRestoreImageFromURL_completionHandler_,
            1,
            b"v@@",
        )
