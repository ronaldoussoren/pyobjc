from PyObjCTools.TestSupport import TestCase

import Virtualization


class TestVZVirtualMachineView(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZVirtualMachineView.capturesSystem,
        )
        self.assertArgIsBOOL(
            Virtualization.VZVirtualMachineView.setCapturesSystem_,
            1,
        )
