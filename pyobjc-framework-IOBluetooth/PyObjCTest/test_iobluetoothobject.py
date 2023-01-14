from PyObjCTools.TestSupport import TestCase

import IOBluetooth


class TestIOBluetoothObject(TestCase):
    def test_constants(self):
        self.assertEqual(
            IOBluetooth.kBluetoothTargetDoesNotRespondToCallbackExceptionName,
            "BluetoothTargetDoesNotRespondToCallbackException",
        )
