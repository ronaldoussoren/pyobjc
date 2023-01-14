from PyObjCTools.TestSupport import TestCase

import IOBluetoothUI


class TestIOBluetoothPasskeyDisplay(TestCase):
    def test_constants(self):
        self.assertIsEnumType(IOBluetoothUI.BluetoothKeyboardReturnType)
        self.assertEqual(IOBluetoothUI.kBluetoothKeyboardANSIReturn, 0)
        self.assertEqual(IOBluetoothUI.kBluetoothKeyboardISOReturn, 1)
        self.assertEqual(IOBluetoothUI.kBluetoothKeyboardJISReturn, 2)
        self.assertEqual(IOBluetoothUI.kBluetoothKeyboardNoReturn, 3)

    def test_methods(self):
        self.assertArgIsBOOL(
            IOBluetoothUI.IOBluetoothPasskeyDisplay.setPasskey_forDevice_usingSSP_, 2
        )
