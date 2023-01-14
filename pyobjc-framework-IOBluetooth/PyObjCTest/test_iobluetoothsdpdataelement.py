from PyObjCTools.TestSupport import TestCase

import IOBluetooth


class TestIOBluetoothSDPDataElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothSDPDataElement.containsValue_)
