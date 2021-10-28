from PyObjCTools.TestSupport import TestCase, min_os_level

import Virtualization


class TestVZVirtualMachineView(TestCase):
    @min_os_level("12.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZVirtualMachineView.capturesSystemKeys,
        )
        self.assertArgIsBOOL(
            Virtualization.VZVirtualMachineView.setCapturesSystemKeys_,
            0,
        )
