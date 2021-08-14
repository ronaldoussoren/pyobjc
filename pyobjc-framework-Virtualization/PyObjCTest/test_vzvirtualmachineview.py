from PyObjCTools.TestSupport import TestCase

import Virtualization


class TestVZVirtualMachineView(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZVirtualMachineView.capturesSystemKeys,
        )
        self.assertArgIsBOOL(
            Virtualization.VZVirtualMachineView.setCapturesSystemKeys_,
            0,
        )
