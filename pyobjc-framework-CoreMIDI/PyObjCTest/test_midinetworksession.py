from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreMIDI


class TestMIDINetworkSession(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreMIDI.MIDINetworkConnectionPolicy)

    def test_constants(self):
        self.assertEqual(CoreMIDI.MIDINetworkConnectionPolicy_NoOne, 0)
        self.assertEqual(CoreMIDI.MIDINetworkConnectionPolicy_HostsInContactList, 1)
        self.assertEqual(CoreMIDI.MIDINetworkConnectionPolicy_Anyone, 2)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(CoreMIDI.MIDINetworkBonjourServiceType, str)
        self.assertIsInstance(CoreMIDI.MIDINetworkNotificationContactsDidChange, str)
        self.assertIsInstance(CoreMIDI.MIDINetworkNotificationSessionDidChange, str)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(CoreMIDI.MIDINetworkSession.isEnabled)
        self.assertArgIsBOOL(CoreMIDI.MIDINetworkSession.setEnabled_, 0)

        self.assertResultIsBOOL(CoreMIDI.MIDINetworkSession.addContact_)
        self.assertResultIsBOOL(CoreMIDI.MIDINetworkSession.removeContact_)

        self.assertResultIsBOOL(CoreMIDI.MIDINetworkSession.addConnection_)
        self.assertResultIsBOOL(CoreMIDI.MIDINetworkSession.removeConnection_)
