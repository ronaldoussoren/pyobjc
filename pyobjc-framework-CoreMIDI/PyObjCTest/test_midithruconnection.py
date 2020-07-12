from PyObjCTools.TestSupport import TestCase
import CoreMIDI


class TestMIDIThruConnection(TestCase):
    def test_structs(self):
        v = CoreMIDI.MIDIValueMap()
        self.assertIs(v.value, None)

        v = CoreMIDI.MIDITransform()
        self.assertIsInstance(v.transform, int)
        self.assertIsInstance(v.param, int)

        v = CoreMIDI.MIDIControlTransform()
        self.assertIsInstance(v.controlType, int)
        self.assertIsInstance(v.remappedControlType, int)
        self.assertIsInstance(v.controlNumber, int)
        self.assertIsInstance(v.transform, int)
        self.assertIsInstance(v.param, int)

        v = CoreMIDI.MIDIThruConnectionEndpoint()
        self.assertIsInstance(v.endpointRef, int)
        self.assertIsInstance(v.uniqueID, int)

        v = CoreMIDI.MIDIThruConnectionParams()
        self.assertIsInstance(v.version, int)
        self.assertIsInstance(v.numSources, int)
        self.assertIs(v.sources, None)
        self.assertIsInstance(v.numDestinations, int)
        self.assertIs(v.destinations, None)
        self.assertIs(v.channelMap, None)
        self.assertIsInstance(v.lowVelocity, int)
        self.assertIsInstance(v.highVelocity, int)
        self.assertIsInstance(v.lowNote, int)
        self.assertIsInstance(v.highNote, int)
        self.assertIsInstance(v.noteNumber, CoreMIDI.MIDITransform)
        self.assertIsInstance(v.velocity, CoreMIDI.MIDITransform)
        self.assertIsInstance(v.keyPressure, CoreMIDI.MIDITransform)
        self.assertIsInstance(v.channelPressure, CoreMIDI.MIDITransform)
        self.assertIsInstance(v.programChange, CoreMIDI.MIDITransform)
        self.assertIsInstance(v.pitchBend, CoreMIDI.MIDITransform)
        self.assertIsInstance(v.filterOutSysEx, int)
        self.assertIsInstance(v.filterOutMTC, int)
        self.assertIsInstance(v.filterOutBeatClock, int)
        self.assertIsInstance(v.filterOutTuneRequest, int)
        # self.assertIs(None)
        self.assertIsInstance(v.filterOutAllControls, int)
        self.assertIsInstance(v.numControlTransforms, int)
        self.assertIsInstance(v.numMaps, int)
        self.assertIs(v.reserved3, None)

    def test_constants(self):
        self.assertEqual(CoreMIDI.kMIDITransform_None, 0)
        self.assertEqual(CoreMIDI.kMIDITransform_FilterOut, 1)
        self.assertEqual(CoreMIDI.kMIDITransform_MapControl, 2)
        self.assertEqual(CoreMIDI.kMIDITransform_Add, 8)
        self.assertEqual(CoreMIDI.kMIDITransform_Scale, 9)
        self.assertEqual(CoreMIDI.kMIDITransform_MinValue, 10)
        self.assertEqual(CoreMIDI.kMIDITransform_MaxValue, 11)
        self.assertEqual(CoreMIDI.kMIDITransform_MapValue, 12)

        self.assertEqual(CoreMIDI.kMIDIThruConnection_MaxEndpoints, 8)

        self.assertEqual(CoreMIDI.kMIDIControlType_7Bit, 0)
        self.assertEqual(CoreMIDI.kMIDIControlType_14Bit, 1)
        self.assertEqual(CoreMIDI.kMIDIControlType_7BitRPN, 2)
        self.assertEqual(CoreMIDI.kMIDIControlType_14BitRPN, 3)
        self.assertEqual(CoreMIDI.kMIDIControlType_7BitNRPN, 4)
        self.assertEqual(CoreMIDI.kMIDIControlType_14BitNRPN, 5)

    def test_functions(self):
        self.assertArgIsIn(CoreMIDI.MIDIThruConnectionParamsInitialize, 0)

        self.assertArgIsOut(CoreMIDI.MIDIThruConnectionCreate, 2)

        CoreMIDI.MIDIThruConnectionDispose

        self.assertArgIsOut(CoreMIDI.MIDIThruConnectionGetParams, 1)

        CoreMIDI.MIDIThruConnectionSetParams

        self.assertArgIsOut(CoreMIDI.MIDIThruConnectionFind, 1)
