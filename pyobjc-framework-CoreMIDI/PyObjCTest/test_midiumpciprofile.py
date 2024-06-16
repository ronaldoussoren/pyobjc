from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreMIDI


class TestMIDIUMPCIProfile(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(CoreMIDI.MIDIUMPCIProfile.isEnabled)

        self.assertResultIsBOOL(
            CoreMIDI.MIDIUMPCIProfile.setProfileState_enabledChannelCount_error_
        )
        self.assertArgIsOut(
            CoreMIDI.MIDIUMPCIProfile.setProfileState_enabledChannelCount_error_, 2
        )
