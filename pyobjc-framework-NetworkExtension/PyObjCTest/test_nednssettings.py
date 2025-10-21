from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEDNSSettings(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(NetworkExtension.NEDNSProtocol)

    def testConstants(self):
        self.assertEqual(NetworkExtension.NEDNSProtocolCleartext, 1)
        self.assertEqual(NetworkExtension.NEDNSProtocolTLS, 2)
        self.assertEqual(NetworkExtension.NEDNSProtocolHTTPS, 3)

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertResultIsBOOL(NetworkExtension.NEDNSSettings.matchDomainsNoSearch)
        self.assertArgIsBOOL(NetworkExtension.NEDNSSettings.setMatchDomainsNoSearch_, 0)

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(NetworkExtension.NEDNSSettings.allowFailover)
        self.assertArgIsBOOL(NetworkExtension.NEDNSSettings.setAllowFailover_, 0)
