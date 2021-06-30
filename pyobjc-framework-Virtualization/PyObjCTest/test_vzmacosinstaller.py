from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZMacOSInstaller(TestCase):
    @min_os_level("12.0")
    def test_methods(self):
        self.assertArgIsBlock(
            Virtualization.VZMacOSInstaller.installWithCompletionHandler_, 0, b"v@"
        )
