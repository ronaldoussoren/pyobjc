from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreMIDI


class MIDIUMPMutableFunctionBlock(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertArgIsBOOL(
            CoreMIDI.MIDIUMPMutableFunctionBlock.initWithName_direction_firstGroup_totalGroupsSpanned_maxSysEx8Streams_MIDI1Info_UIHint_isEnabled_,
            7,
        )

        self.assertResultIsBOOL(CoreMIDI.MIDIUMPMutableFunctionBlock.setEnabled_error_)
        self.assertArgIsBOOL(CoreMIDI.MIDIUMPMutableFunctionBlock.setEnabled_error_, 0)
        self.assertArgIsOut(CoreMIDI.MIDIUMPMutableFunctionBlock.setEnabled_error_, 1)

        self.assertResultIsBOOL(CoreMIDI.MIDIUMPMutableFunctionBlock.setName_error_)
        self.assertArgIsOut(CoreMIDI.MIDIUMPMutableFunctionBlock.setName_error_, 1)

        self.assertResultIsBOOL(
            CoreMIDI.MIDIUMPMutableFunctionBlock.reconfigureWithFirstGroup_direction_MIDI1Info_UIHint_error_
        )
        self.assertArgIsOut(
            CoreMIDI.MIDIUMPMutableFunctionBlock.reconfigureWithFirstGroup_direction_MIDI1Info_UIHint_error_,
            4,
        )
