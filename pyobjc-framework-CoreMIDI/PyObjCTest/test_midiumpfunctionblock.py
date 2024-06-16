from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreMIDI


class TestMIDIUMPFunctionBlock(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(CoreMIDI.MIDIUMPFunctionBlock.isEnabled)
