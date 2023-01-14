from PyObjCTools.TestSupport import TestCase

import IOBluetooth  # noqa: F401


class TestIOBluetoothHandsFreeAudioGateway(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("IOBluetoothHandsFreeAudioGatewayDelegate")
