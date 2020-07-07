from PyObjCTools.TestSupport import TestCase
import CoreMIDI


class TestMIDIDriver(TestCase):
    def test_types(self):
        self.assertOpaqueType(CoreMIDI.MIDIDeviceRef)
        self.assertOpaqueType(CoreMIDI.MIDIDeviceListRef)
        self.assertOpaqueType(CoreMIDI.MIDIEndpointRef)

    def test_constants(self):
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
