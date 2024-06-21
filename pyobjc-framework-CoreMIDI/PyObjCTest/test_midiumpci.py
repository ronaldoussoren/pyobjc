from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreMIDI


class TestMIDIUMPCI(TestCase):
    def test_enum(self):
        self.assertIsEnumType(CoreMIDI.MIDICICategoryBitmap)
        self.assertEqual(CoreMIDI.kMIDICICategoryBitmapProtocolNegotiation, 1 << 1)
        self.assertEqual(
            CoreMIDI.kMIDICICategoryBitmapProfileConfigurationSupported, 1 << 2
        )
        self.assertEqual(
            CoreMIDI.kMIDICICategoryBitmapPropertyExchangeSupported, 1 << 3
        )
        self.assertEqual(CoreMIDI.kMIDICICategoryBitmapProcessInquirySupported, 1 << 4)

        self.assertIsEnumType(CoreMIDI.MIDICIDeviceType)
        self.assertEqual(CoreMIDI.kMIDICIDeviceTypeUnknown, 0)
        self.assertEqual(CoreMIDI.kMIDICIDeviceTypeLegacyMIDI1, 1)
        self.assertEqual(CoreMIDI.kMIDICIDeviceTypeVirtual, 2)
        self.assertEqual(CoreMIDI.kMIDICIDeviceTypeUSBMIDI, 3)

        self.assertIsEnumType(CoreMIDI.MIDICIProfileMessageType)
        self.assertEqual(CoreMIDI.kMIDICIProfileMessageTypeProfileInquiry, 0x20)
        self.assertEqual(CoreMIDI.kMIDICIProfileMessageTypeReplyToProfileInquiry, 0x21)
        self.assertEqual(CoreMIDI.kMIDICIProfileMessageTypeSetProfileOn, 0x22)
        self.assertEqual(CoreMIDI.kMIDICIProfileMessageTypeSetProfileOff, 0x23)
        self.assertEqual(CoreMIDI.kMIDICIProfileMessageTypeProfileEnabledReport, 0x24)
        self.assertEqual(CoreMIDI.kMIDICIProfileMessageTypeProfileDisabledReport, 0x25)
        self.assertEqual(CoreMIDI.kMIDICIProfileMessageTypeProfileAdded, 0x26)
        self.assertEqual(CoreMIDI.kMIDICIProfileMessageTypeProfileRemoved, 0x27)
        self.assertEqual(CoreMIDI.kMIDICIProfileMessageTypeDetailsInquiry, 0x28)
        self.assertEqual(CoreMIDI.kMIDICIProfileMessageTypeReplyToDetailsInquiry, 0x29)
        self.assertEqual(CoreMIDI.kMIDICIProfileMessageTypeProfileSpecificData, 0x2F)

        self.assertIsEnumType(CoreMIDI.MIDICIPropertyExchangeMessageType)
        self.assertEqual(
            CoreMIDI.kMIDICIPropertyExchangeMessageTypeInquiryPropertyExchangeCapabilities,
            0x30,
        )
        self.assertEqual(
            CoreMIDI.kMIDICIPropertyExchangeMessageTypeReplyToPropertyExchangeCapabilities,
            0x31,
        )
        self.assertEqual(
            CoreMIDI.kMIDICIPropertyExchangeMessageTypeInquiryHasPropertyData_Reserved,
            0x32,
        )
        self.assertEqual(
            CoreMIDI.kMIDICIPropertyExchangeMessageTypeInquiryReplyToHasPropertyData_Reserved,
            0x33,
        )
        self.assertEqual(
            CoreMIDI.kMIDICIPropertyExchangeMessageTypeInquiryGetPropertyData, 0x34
        )
        self.assertEqual(
            CoreMIDI.kMIDICIPropertyExchangeMessageTypeReplyToGetProperty, 0x35
        )
        self.assertEqual(
            CoreMIDI.kMIDICIPropertyExchangeMessageTypeInquirySetPropertyData, 0x36
        )
        self.assertEqual(
            CoreMIDI.kMIDICIPropertyExchangeMessageTypeReplyToSetPropertyData, 0x37
        )
        self.assertEqual(CoreMIDI.kMIDICIPropertyExchangeMessageTypeSubscription, 0x38)
        self.assertEqual(
            CoreMIDI.kMIDICIPropertyExchangeMessageTypeReplyToSubscription, 0x39
        )
        self.assertEqual(CoreMIDI.kMIDICIPropertyExchangeMessageTypeNotify, 0x3F)

        self.assertIsEnumType(CoreMIDI.MIDICIProcessInquiryMessageType)
        self.assertEqual(
            CoreMIDI.kMIDICIProcessInquiryMessageTypeInquiryProcessInquiryCapabilities,
            0x40,
        )
        self.assertEqual(
            CoreMIDI.kMIDICIProcessInquiryMessageTypeReplyToProcessInquiryCapabilities,
            0x41,
        )
        self.assertEqual(
            CoreMIDI.kMIDICIProcessInquiryMessageTypeInquiryMIDIMessageReport, 0x42
        )
        self.assertEqual(
            CoreMIDI.kMIDICIProcessInquiryMessageTypeReplyToMIDIMessageReport, 0x43
        )
        self.assertEqual(
            CoreMIDI.kMIDICIProcessInquiryMessageTypeEndOfMIDIMessageReport, 0x44
        )

        self.assertIsEnumType(CoreMIDI.MIDICIManagementMessageType)
        self.assertEqual(CoreMIDI.kMIDICIManagementMessageTypeDiscovery, 0x70)
        self.assertEqual(CoreMIDI.kMIDICIManagementMessageTypeReplyToDiscovery, 0x71)
        self.assertEqual(
            CoreMIDI.kMIDICIManagementMessageTypeInquiryEndpointInformation, 0x72
        )
        self.assertEqual(
            CoreMIDI.kMIDICIManagementMessageTypeReplyToEndpointInformation, 0x73
        )
        self.assertEqual(CoreMIDI.kMIDICIManagementMessageTypeMIDICIACK, 0x7D)
        self.assertEqual(CoreMIDI.kMIDICIManagementMessageTypeInvalidateMUID, 0x7E)
        self.assertEqual(CoreMIDI.kMIDICIManagementMessageTypeMIDICINAK, 0x7F)

        self.assertIsEnumType(CoreMIDI.MIDICIProfileType)
        self.assertEqual(CoreMIDI.kMIDICIProfileTypeSingleChannel, 1)
        self.assertEqual(CoreMIDI.kMIDICIProfileTypeGroup, 2)
        self.assertEqual(CoreMIDI.kMIDICIProfileTypeFunctionBlock, 3)
        self.assertEqual(CoreMIDI.kMIDICIProfileTypeMultichannel, 4)

        self.assertIsEnumType(CoreMIDI.MIDIUMPCIObjectBackingType)
        self.assertEqual(CoreMIDI.kMIDIUMPCIObjectBackingTypeUnknown, 0)
        self.assertEqual(CoreMIDI.kMIDIUMPCIObjectBackingTypeVirtual, 1)
        self.assertEqual(CoreMIDI.kMIDIUMPCIObjectBackingTypeDriverDevice, 2)
        self.assertEqual(CoreMIDI.kMIDIUMPCIObjectBackingTypeUSBMIDI, 3)

        self.assertEqual(CoreMIDI.kMIDICIPropertyExchangeBadRequestID, 0xFF)

    def test_structs(self):
        v = CoreMIDI.MIDI2DeviceManufacturer()
        self.assertEqual(v.sysExIDByte, None)

        v = CoreMIDI.MIDI2DeviceRevisionLevel()
        self.assertEqual(v.revisionLevel, None)

        v = CoreMIDI.MIDICIProfileIDStandard()
        self.assertIsInstance(v.profileIDByte1, int)
        self.assertIsInstance(v.profileBank, int)
        self.assertIsInstance(v.profileNumber, int)
        self.assertIsInstance(v.profileVersion, int)
        self.assertIsInstance(v.profileLevel, int)

        v = CoreMIDI.MIDICIProfileIDManufacturerSpecific()
        self.assertIsInstance(v.sysExID1, int)
        self.assertIsInstance(v.sysExID2, int)
        self.assertIsInstance(v.sysExID3, int)
        self.assertIsInstance(v.info1, int)
        self.assertIsInstance(v.info2, int)

        self.assertNotHasAttr(CoreMIDI, "MIDICIProfileID")  # union

    @min_os_level("13.0")
    def test_functions(self):
        CoreMIDI.MIDIBluetoothDriverActivateAllConnections
        CoreMIDI.MIDIBluetoothDriverDisconnect
