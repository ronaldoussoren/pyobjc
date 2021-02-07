from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreMIDI


class TestMIDISetup(TestCase):
    def test_functions(self):
        CoreMIDI.MIDISetupCreate
        CoreMIDI.MIDISetupDispose
        CoreMIDI.MIDISetupInstall

        self.assertArgIsOut(CoreMIDI.MIDISetupGetCurrent, 0)

        self.assertArgIsOut(CoreMIDI.MIDISetupToData, 1)
        self.assertArgIsCFRetained(CoreMIDI.MIDISetupToData, 1)

        self.assertArgIsOut(CoreMIDI.MIDISetupFromData, 1)

        self.assertArgIsBOOL(CoreMIDI.MIDIDeviceAddEntity, 2)
        self.assertArgIsOut(CoreMIDI.MIDIDeviceAddEntity, 5)

        CoreMIDI.MIDIDeviceRemoveEntity
        CoreMIDI.MIDIEntityAddOrRemoveEndpoints
        CoreMIDI.MIDISetupAddDevice
        CoreMIDI.MIDISetupRemoveDevice
        CoreMIDI.MIDISetupAddExternalDevice
        CoreMIDI.MIDISetupRemoveExternalDevice

        self.assertArgIsOut(CoreMIDI.MIDIGetSerialPortOwner, 1)

        CoreMIDI.MIDISetSerialPortOwner

        self.assertArgIsOut(CoreMIDI.MIDIGetSerialPortDrivers, 0)
        self.assertArgIsCFRetained(CoreMIDI.MIDIGetSerialPortDrivers, 0)

        self.assertArgIsOut(CoreMIDI.MIDIExternalDeviceCreate, 2)

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsBOOL(CoreMIDI.MIDIDeviceNewEntity, 3)
        self.assertArgIsOut(CoreMIDI.MIDIDeviceNewEntity, 6)
