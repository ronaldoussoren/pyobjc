from PyObjCTools.TestSupport import TestCase
import NetworkExtension


class TestNEDNSSettings(TestCase):
    def testConstants(self):
        self.assertEqual(NetworkExtension.NEDNSProtocolCleartext, 1)
        self.assertEqual(NetworkExtension.NEDNSProtocolTLS, 2)
        self.assertEqual(NetworkExtension.NEDNSProtocolHTTPS, 3)
