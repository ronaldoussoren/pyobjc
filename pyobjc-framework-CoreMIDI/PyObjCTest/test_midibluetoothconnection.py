from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreMIDI


class TestMIDIBluetoothConnection(TestCase):
    @min_os_level("13.0")
    def test_functions(self):
        CoreMIDI.MIDIBluetoothDriverActivateAllConnections
        CoreMIDI.MIDIBluetoothDriverDisconnect
