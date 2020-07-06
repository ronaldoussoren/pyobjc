from PyObjCTools.TestSupport import TestCase
import CoreMIDI


class TestMIDIServices(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMIDI.kMIDIInvalidClient, -10830)
        self.assertEqual(CoreMIDI.kMIDIInvalidPort, -10831)
        self.assertEqual(CoreMIDI.kMIDIWrongEndpointType, -10832)
        self.assertEqual(CoreMIDI.kMIDINoConnection, -10833)
        self.assertEqual(CoreMIDI.kMIDIUnknownEndpoint, -10834)
        self.assertEqual(CoreMIDI.kMIDIUnknownProperty, -10835)
        self.assertEqual(CoreMIDI.kMIDIWrongPropertyType, -10836)
        self.assertEqual(CoreMIDI.kMIDINoCurrentSetup, -10837)
        self.assertEqual(CoreMIDI.kMIDIMessageSendErr, -10838)
        self.assertEqual(CoreMIDI.kMIDIServerStartErr, -10839)
        self.assertEqual(CoreMIDI.kMIDISetupFormatErr, -10840)
        self.assertEqual(CoreMIDI.kMIDIWrongThread, -10841)
        self.assertEqual(CoreMIDI.kMIDIObjectNotFound, -10842)
        self.assertEqual(CoreMIDI.kMIDIIDNotUnique, -10843)
        self.assertEqual(CoreMIDI.kMIDINotPermitted, -10844)
        self.assertEqual(CoreMIDI.kMIDIUnknownError, -10845)

        self.assertEqual(CoreMIDI.kMIDIObjectType_Other, -1)
        self.assertEqual(CoreMIDI.kMIDIObjectType_Device, 0)
        self.assertEqual(CoreMIDI.kMIDIObjectType_Entity, 1)
        self.assertEqual(CoreMIDI.kMIDIObjectType_Source, 2)
        self.assertEqual(CoreMIDI.kMIDIObjectType_Destination, 3)

        self.assertEqual(
            CoreMIDI.kMIDIObjectType_ExternalDevice,
            0x10 | CoreMIDI.kMIDIObjectType_Device,
        )
        self.assertEqual(
            CoreMIDI.kMIDIObjectType_ExternalEntity,
            0x10 | CoreMIDI.kMIDIObjectType_Entity,
        )
        self.assertEqual(
            CoreMIDI.kMIDIObjectType_ExternalSource,
            0x10 | CoreMIDI.kMIDIObjectType_Source,
        )
        self.assertEqual(
            CoreMIDI.kMIDIObjectType_ExternalDestination,
            0x10 | CoreMIDI.kMIDIObjectType_Destination,
        )

        self.assertEqual(CoreMIDI.kMIDIObjectType_ExternalMask, 0x10)

        self.assertEqual(CoreMIDI.kMIDIProtocol_1_0, 1)
        self.assertEqual(CoreMIDI.kMIDIProtocol_2_0, 2)
