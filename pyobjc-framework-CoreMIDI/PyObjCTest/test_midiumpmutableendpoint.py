from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreMIDI


class TestMIDIUMPMutableEndpoint(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(CoreMIDI.MIDIUMPMutableEndpoint.isEnabled)

        self.assertArgIsBlock(
            CoreMIDI.MIDIUMPMutableEndpoint.initWithName_deviceInfo_productInstanceID_MIDIProtocol_destinationCallback_,
            4,
            b"v^{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}^v",
        )

        self.assertResultIsBOOL(CoreMIDI.MIDIUMPMutableEndpoint.setName_error_)
        self.assertArgIsOut(CoreMIDI.MIDIUMPMutableEndpoint.setName_error_, 1)

        self.assertResultIsBOOL(
            CoreMIDI.MIDIUMPMutableEndpoint.registerFunctionBlocks_markAsStatic_error_
        )
        self.assertArgIsBOOL(
            CoreMIDI.MIDIUMPMutableEndpoint.registerFunctionBlocks_markAsStatic_error_,
            1,
        )
        self.assertArgIsOut(
            CoreMIDI.MIDIUMPMutableEndpoint.registerFunctionBlocks_markAsStatic_error_,
            2,
        )

        self.assertResultIsBOOL(CoreMIDI.MIDIUMPMutableEndpoint.setEnabled_error_)
        self.assertArgIsBOOL(CoreMIDI.MIDIUMPMutableEndpoint.setEnabled_error_, 0)
        self.assertArgIsOut(CoreMIDI.MIDIUMPMutableEndpoint.setEnabled_error_, 1)
