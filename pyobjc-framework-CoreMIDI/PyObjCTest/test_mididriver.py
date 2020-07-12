from PyObjCTools.TestSupport import TestCase
import CoreMIDI


class TestMIDIDriver(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(CoreMIDI.MIDIDriverRef)

    def test_constants(self):
        if CoreMIDI.kMIDIDriverPropertyUsesSerial is not None:
            self.assertIsInstance(CoreMIDI.kMIDIDriverPropertyUsesSerial, str)

    def test_not_exposed(self):
        self.assertNotHasAttr(CoreMIDI, "kMIDIDriverTypeID")
        self.assertNotHasAttr(CoreMIDI, "kMIDIDriverInterfaceID")
        self.assertNotHasAttr(CoreMIDI, "kMIDIDriverInterface2ID")
        self.assertNotHasAttr(CoreMIDI, "kMIDIDriverInterfaceXID")

        self.assertNotHasAttr(CoreMIDI, "MIDIEndpointSetRefCons")
        self.assertNotHasAttr(CoreMIDI, "MIDIEndpointGetRefCons")

    def test_functions(self):
        self.assertArgIsOut(CoreMIDI.MIDIDeviceCreate, 4)
        CoreMIDI.MIDIDeviceDispose
        CoreMIDI.MIDIDeviceListGetNumberOfDevices
        CoreMIDI.MIDIDeviceListGetDevice
        CoreMIDI.MIDIDeviceListAddDevice
        CoreMIDI.MIDIDeviceListDispose
        CoreMIDI.MIDIGetDriverIORunLoop
        CoreMIDI.MIDIGetDriverDeviceList
        self.assertArgIsBOOL(CoreMIDI.MIDIDriverEnableMonitoring, 1)
