from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import CoreMIDI
import objc

MIDICIProfileChangedBlock = b"v@" + objc._C_NSInteger + b"@" + objc._C_NSBOOL
MIDICISessionDisconnectBlock = b"v@@"
MIDICIProfileSpecificDataBlock = b"v@" + objc._C_NSInteger + b"@@"
MIDICIDiscoveryResponseBlock = b"v@"


class TestMIDICapabilityInquiryHelper(CoreMIDI.NSObject):
    def connectInitiator_withDeviceInfo_(self, a, b):
        return 1

    def willSetProfile_onChannel_enabled_(self, a, b, c):
        return 1


class TestMIDICapabilityInquiry(TestCase):
    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("MIDICIProfileResponderDelegate")

    def test_structs(self):
        # XXX: Not sure if bridge is capable enough
        v = CoreMIDI.MIDICIDeviceIdentification()
        self.assertIs(v.manufacturer, None)
        self.assertIs(v.family, None)
        self.assertIs(v.modelNumber, None)
        self.assertIs(v.revisionLevel, None)
        self.assertIs(v.reserved, None)

    def test_methods(self):
        self.assertResultIsBOOL(
            TestMIDICapabilityInquiryHelper.connectInitiator_withDeviceInfo_
        )
        self.assertArgIsBOOL(
            TestMIDICapabilityInquiryHelper.willSetProfile_onChannel_enabled_, 2
        )

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(CoreMIDI.MIDICISession.supportsProfileCapability)
        self.assertResultIsBOOL(CoreMIDI.MIDICISession.supportsPropertyCapability)

        self.assertResultIsBOOL(CoreMIDI.MIDICISession.enableProfile_onChannel_error_)
        self.assertArgIsOut(CoreMIDI.MIDICISession.enableProfile_onChannel_error_, 2)

        self.assertResultIsBOOL(CoreMIDI.MIDICISession.disableProfile_onChannel_error_)
        self.assertArgIsOut(CoreMIDI.MIDICISession.disableProfile_onChannel_error_, 2)

        self.assertResultIsBlock(
            CoreMIDI.MIDICISession.profileChangedCallback, MIDICIProfileChangedBlock
        )
        self.assertArgIsBlock(
            CoreMIDI.MIDICISession.setProfileChangedCallback_,
            0,
            MIDICIProfileChangedBlock,
        )

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsBlock(
            CoreMIDI.MIDICISession.initWithDiscoveredNode_dataReadyHandler_disconnectHandler_,
            1,
            b"v",
        )
        self.assertArgIsBlock(
            CoreMIDI.MIDICISession.initWithDiscoveredNode_dataReadyHandler_disconnectHandler_,
            2,
            MIDICISessionDisconnectBlock,
        )
        self.assertResultIsBOOL(
            CoreMIDI.MIDICISession.sendProfile_onChannel_profileData_
        )
        self.assertResultIsBOOL(CoreMIDI.MIDICIDiscoveredNode.supportsProfiles)
        self.assertResultIsBOOL(CoreMIDI.MIDICIDiscoveredNode.supportsProperties)

        self.assertArgIsBOOL(
            CoreMIDI.MIDICIResponder.initWithDeviceInfo_profileDelegate_profileStates_supportProperties_,
            3,
        )

        self.assertResultIsBOOL(
            CoreMIDI.MIDICIResponder.notifyProfile_onChannel_isEnabled_
        )
        self.assertArgIsBOOL(
            CoreMIDI.MIDICIResponder.notifyProfile_onChannel_isEnabled_, 2
        )

        self.assertResultIsBOOL(
            CoreMIDI.MIDICIResponder.sendProfile_onChannel_profileData_
        )

        self.assertResultIsBOOL(CoreMIDI.MIDICIResponder.start)

        self.assertArgIsBlock(
            CoreMIDI.MIDICIDiscoveryManager.discoverWithHandler_,
            0,
            MIDICIDiscoveryResponseBlock,
        )
        self.assertResultIsBlock(
            CoreMIDI.MIDICISession.profileSpecificDataHandler,
            MIDICIProfileSpecificDataBlock,
        )
        self.assertArgIsBlock(
            CoreMIDI.MIDICISession.setProfileSpecificDataHandler_,
            0,
            MIDICIProfileSpecificDataBlock,
        )
