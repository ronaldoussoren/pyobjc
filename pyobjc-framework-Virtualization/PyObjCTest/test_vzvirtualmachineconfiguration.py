from PyObjCTools.TestSupport import TestCase

import Virtualization


class TestVZVirtualMachineConfiguration(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZVirtualMachineConfiguration.validateWithError_
        )
        self.assertArgIsOut(
            Virtualization.VZVirtualMachineConfiguration.validateWithError_, 0
        )
