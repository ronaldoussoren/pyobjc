from PyObjCTools.TestSupport import TestCase, min_sdk_level
import CoreMIDI


class TestMIDIMessages(TestCase):
    def test_structs(self):
        v = CoreMIDI.MIDIMessage_64()
        self.assertIsInstance(v.word0, int)
        self.assertIsInstance(v.word1, int)
        self.assertPickleRoundTrips(v)

        v = CoreMIDI.MIDIMessage_96()
        self.assertIsInstance(v.word0, int)
        self.assertIsInstance(v.word1, int)
        self.assertIsInstance(v.word2, int)
        self.assertPickleRoundTrips(v)

        v = CoreMIDI.MIDIMessage_128()
        self.assertIsInstance(v.word0, int)
        self.assertIsInstance(v.word1, int)
        self.assertIsInstance(v.word2, int)
        self.assertIsInstance(v.word3, int)
        self.assertPickleRoundTrips(v)

        # XXX: Contains a union
        self.assertNotHasAttr(CoreMIDI, "MIDIUniversalMessage")

    def test_constants(self):
        self.assertEqual(CoreMIDI.kMIDIMessageTypeUtility, 0x0)
        self.assertEqual(CoreMIDI.kMIDIMessageTypeSystem, 0x1)
        self.assertEqual(CoreMIDI.kMIDIMessageTypeChannelVoice1, 0x2)
        self.assertEqual(CoreMIDI.kMIDIMessageTypeSysEx, 0x3)
        self.assertEqual(CoreMIDI.kMIDIMessageTypeChannelVoice2, 0x4)
        self.assertEqual(CoreMIDI.kMIDIMessageTypeData128, 0x5)
        self.assertEqual(CoreMIDI.kMIDIMessageTypeUnknownF, 0xF)

        self.assertEqual(CoreMIDI.kMIDICVStatusNoteOff, 0x8)
        self.assertEqual(CoreMIDI.kMIDICVStatusNoteOn, 0x9)
        self.assertEqual(CoreMIDI.kMIDICVStatusPolyPressure, 0xA)
        self.assertEqual(CoreMIDI.kMIDICVStatusControlChange, 0xB)
        self.assertEqual(CoreMIDI.kMIDICVStatusProgramChange, 0xC)
        self.assertEqual(CoreMIDI.kMIDICVStatusChannelPressure, 0xD)
        self.assertEqual(CoreMIDI.kMIDICVStatusPitchBend, 0xE)
        self.assertEqual(CoreMIDI.kMIDICVStatusRegisteredPNC, 0x0)
        self.assertEqual(CoreMIDI.kMIDICVStatusAssignablePNC, 0x1)
        self.assertEqual(CoreMIDI.kMIDICVStatusRegisteredControl, 0x2)
        self.assertEqual(CoreMIDI.kMIDICVStatusAssignableControl, 0x3)
        self.assertEqual(CoreMIDI.kMIDICVStatusRelRegisteredControl, 0x4)
        self.assertEqual(CoreMIDI.kMIDICVStatusRelAssignableControl, 0x5)
        self.assertEqual(CoreMIDI.kMIDICVStatusPerNotePitchBend, 0x6)
        self.assertEqual(CoreMIDI.kMIDICVStatusPerNoteMgmt, 0xF)

        self.assertEqual(CoreMIDI.kMIDIStatusStartOfExclusive, 0xF0)
        self.assertEqual(CoreMIDI.kMIDIStatusEndOfExclusive, 0xF7)
        self.assertEqual(CoreMIDI.kMIDIStatusMTC, 0xF1)
        self.assertEqual(CoreMIDI.kMIDIStatusSongPosPointer, 0xF2)
        self.assertEqual(CoreMIDI.kMIDIStatusSongSelect, 0xF3)
        self.assertEqual(CoreMIDI.kMIDIStatusTuneRequest, 0xF6)
        self.assertEqual(CoreMIDI.kMIDIStatusTimingClock, 0xF8)
        self.assertEqual(CoreMIDI.kMIDIStatusStart, 0xFA)
        self.assertEqual(CoreMIDI.kMIDIStatusContinue, 0xFB)
        self.assertEqual(CoreMIDI.kMIDIStatusStop, 0xFC)
        self.assertEqual(CoreMIDI.kMIDIStatusActiveSending, 0xFE)
        self.assertEqual(CoreMIDI.kMIDIStatusActiveSensing, 0xFE)
        self.assertEqual(CoreMIDI.kMIDIStatusSystemReset, 0xFF)

        self.assertEqual(CoreMIDI.kMIDISysExStatusComplete, 0x0)
        self.assertEqual(CoreMIDI.kMIDISysExStatusStart, 0x1)
        self.assertEqual(CoreMIDI.kMIDISysExStatusContinue, 0x2)
        self.assertEqual(CoreMIDI.kMIDISysExStatusEnd, 0x3)
        self.assertEqual(CoreMIDI.kMIDISysExStatusMixedDataSetHeader, 0x8)
        self.assertEqual(CoreMIDI.kMIDISysExStatusMixedDataSetPayload, 0x9)

        self.assertEqual(CoreMIDI.kMIDIUtilityStatusNOOP, 0x0)
        self.assertEqual(CoreMIDI.kMIDIUtilityStatusJitterReductionClock, 0x1)
        self.assertEqual(CoreMIDI.kMIDIUtilityStatusJitterReductionTimestamp, 0x2)

        self.assertEqual(CoreMIDI.kMIDINoteAttributeNone, 0x0)
        self.assertEqual(CoreMIDI.kMIDINoteAttributeManufacturerSpecific, 0x1)
        self.assertEqual(CoreMIDI.kMIDINoteAttributeProfileSpecific, 0x2)
        self.assertEqual(CoreMIDI.kMIDINoteAttributePitch, 0x3)

        self.assertEqual(CoreMIDI.kMIDIProgramChangeBankValid, 0x1)

        self.assertEqual(CoreMIDI.kMIDIPerNoteManagementReset, 0x1)
        self.assertEqual(CoreMIDI.kMIDIPerNoteManagementDetach, 0x2)

    # @expectedFailure  # XXX: Inline functions
    @min_sdk_level("11.0")
    def test_functions11_0(self):
        CoreMIDI.MIDIMessageTypeForUPWord
        CoreMIDI.MIDI1UPChannelVoiceMessage
        CoreMIDI.MIDI1UPNoteOff
        CoreMIDI.MIDI1UPNoteOn
        CoreMIDI.MIDI1UPControlChange
        CoreMIDI.MIDI1UPPitchBend
        CoreMIDI.MIDI1UPSystemCommon
        CoreMIDI.MIDI2ChannelVoiceMessage
        CoreMIDI.MIDI2NoteOn
        CoreMIDI.MIDI2NoteOff
        CoreMIDI.MIDI2PolyPressure
        CoreMIDI.MIDI2RegisteredPNC
        CoreMIDI.MIDI2AssignablePNC
        CoreMIDI.MIDI2PerNoteManagment
        CoreMIDI.MIDI2ControlChange
        CoreMIDI.MIDI2RegisteredControl
        CoreMIDI.MIDI2AssignableControl
        CoreMIDI.MIDI2RelRegisteredControl
        CoreMIDI.MIDI2RelAssignableControl
        CoreMIDI.MIDI2ProgramChange
        CoreMIDI.MIDI2ChannelPressure
        CoreMIDI.MIDI2PitchBend
        CoreMIDI.MIDI2PerNotePitchBend

    @min_sdk_level("12.0")
    def test_functions12_0(self):
        # These have an API that's not easily reproduced in Python
        # CoreMIDI.MIDI1UPSysEx
        # CoreMIDI.MIDI1UPSysExArray

        # 'MIDIUniversalMessage' is not available in Python
        self.assertNotHasAttr(CoreMIDI, "MIDIEventListForEachEvent")
