from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreMIDI


class TestMIDICIDevice(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assetResultIsBOOL(CoreMIDI.MIDICIDevice.supportsProtocolNegotiation)
        self.assetResultIsBOOL(CoreMIDI.MIDICIDevice.supportsProfileConfiguration)
        self.assetResultIsBOOL(CoreMIDI.MIDICIDevice.supportsPropertyExchange)
        self.assetResultIsBOOL(CoreMIDI.MIDICIDevice.supportsProcessInquiry)
