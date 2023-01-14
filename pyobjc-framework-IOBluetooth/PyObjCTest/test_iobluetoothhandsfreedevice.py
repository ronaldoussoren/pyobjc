from PyObjCTools.TestSupport import TestCase

import IOBluetooth  # noqa: F401


class TestIOBluetoothHandsFreeDevice(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("IOBluetoothHandsFreeDeviceDelegate")
