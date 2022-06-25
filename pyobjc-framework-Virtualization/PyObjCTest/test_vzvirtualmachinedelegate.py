from PyObjCTools.TestSupport import TestCase
import Virtualization  # noqa: F401


class TestVZVirtualMachineDelegate(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("VZVirtualMachineDelegate")
