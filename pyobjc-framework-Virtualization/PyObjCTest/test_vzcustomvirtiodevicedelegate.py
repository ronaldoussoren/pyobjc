from PyObjCTools.TestSupport import TestCase, min_sdk_level

import Virtualization


class TestVZCustomVirtioDeviceDelegateHelper(Virtualization.NSObject):
    def customVirtioDeviceShouldRestore_saveState_(self, a, b):
        return 1


class TestVZCustomVirtioDeviceDelegate(TestCase):
    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists("VZCustomVirtioDeviceDelegate", Virtualization)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            TestVZCustomVirtioDeviceDelegateHelper.customVirtioDeviceShouldRestore_saveState_
        )
