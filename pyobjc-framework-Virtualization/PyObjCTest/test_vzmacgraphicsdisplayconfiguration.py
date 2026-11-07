from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZMacGraphicsDisplayConfiguration(TestCase):
    @min_os_level("27.3")
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZMacGraphicsDisplayConfiguration.enableHDR
        )
        self.assertArgIsBOOL(
            Virtualization.VZMacGraphicsDisplayConfiguration.setEnableHDR_, 0
        )
