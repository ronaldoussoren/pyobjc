from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreMIDI


class TestMIDICIDeviceManager(TestCase):
    @min_os_level("15.0")
    def test_constants(self):
        self.assertIsInstance(CoreMIDI.MIDICIDeviceWasAddedNotification, str)
        self.assertIsInstance(CoreMIDI.MIDICIDeviceWasRemovedNotification, str)
        self.assertIsInstance(CoreMIDI.MIDICIProfileWasRemovedNotification, str)
        self.assertIsInstance(CoreMIDI.MIDICIDeviceObjectKey, str)
        self.assertIsInstance(CoreMIDI.MIDICIProfileObjectKey, str)
