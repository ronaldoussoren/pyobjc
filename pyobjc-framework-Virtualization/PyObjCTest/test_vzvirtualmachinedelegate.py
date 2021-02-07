from PyObjCTools.TestSupport import TestCase
import objc
import Virtualization  # noqa: F401


class TestVZVirtualMachineDelegate(TestCase):
    def test_protocols(self):
        objc.protocolNamed("VZVirtualMachineDelegate")
