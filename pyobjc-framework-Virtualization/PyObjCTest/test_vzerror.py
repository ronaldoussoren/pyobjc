from PyObjCTools.TestSupport import TestCase

import Virtualization


class TestVZError(TestCase):
    def test_constants(self):
        self.assertEqual(Virtualization.VZErrorInternal, 1)
        self.assertEqual(Virtualization.VZErrorInvalidVirtualMachineConfiguration, 2)
        self.assertEqual(Virtualization.VZErrorInvalidVirtualMachineState, 3)
        self.assertEqual(Virtualization.VZErrorInvalidVirtualMachineStateTransition, 4)
        self.assertEqual(Virtualization.VZErrorInvalidDiskImage, 5)
