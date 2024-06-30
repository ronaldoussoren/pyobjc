from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreMIDI


class TestMIDIUMPEndpointManager(TestCase):
    @min_os_level("15.0")
    def test_constants(self):
        self.assertIsInstance(CoreMIDI.MIDIUMPEndpointWasAddedNotification, str)
        self.assertIsInstance(CoreMIDI.MIDIUMPEndpointWasRemovedNotification, str)
        self.assertIsInstance(CoreMIDI.MIDIUMPEndpointObjectKey, str)
        self.assertIsInstance(CoreMIDI.MIDIUMPFunctionBlockObjectKey, str)
