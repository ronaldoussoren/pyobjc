from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreMIDI


class TestMIDIUMPEndpoint(TestCase):
    def test_enum(self):
        self.assertIsEnumType(CoreMIDI.MIDIUMPProtocolOptions)
        self.assertEqual(CoreMIDI.kMIDIUMPProtocolOptionsMIDI1, 1)
        self.assertEqual(CoreMIDI.kMIDIUMPProtocolOptionsMIDI2, 1 << 1)

    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(CoreMIDI.MIDIUMPEndpoint.hasStaticFunctionBlocks)
        self.assertResultIsBOOL(CoreMIDI.MIDIUMPEndpoint.hasJRTSReceiveCapability)
        self.assertResultIsBOOL(CoreMIDI.MIDIUMPEndpoint.hasJRTSTransmitCapability)
