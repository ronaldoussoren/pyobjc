from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreMIDI


class TestMIDICIDevice(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(CoreMIDI.MIDICIDevice.supportsProtocolNegotiation)
        self.assertResultIsBOOL(CoreMIDI.MIDICIDevice.supportsProfileConfiguration)
        self.assertResultIsBOOL(CoreMIDI.MIDICIDevice.supportsPropertyExchange)
        self.assertResultIsBOOL(CoreMIDI.MIDICIDevice.supportsProcessInquiry)
