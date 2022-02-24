from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEVPNProtocolIPSec(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(NetworkExtension.NEVPNIKEAuthenticationMethod)

    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(NetworkExtension.NEVPNIKEAuthenticationMethodNone, 0)
        self.assertEqual(NetworkExtension.NEVPNIKEAuthenticationMethodCertificate, 1)
        self.assertEqual(NetworkExtension.NEVPNIKEAuthenticationMethodSharedSecret, 2)

    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(
            NetworkExtension.NEVPNProtocolIPSec.useExtendedAuthentication
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEVPNProtocolIPSec.setUseExtendedAuthentication_, 0
        )
