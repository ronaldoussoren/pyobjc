import Security
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSecProtocolTypes(TestCase):
    def test_constants(self):
        self.assertEqual(Security.tls_protocol_version_TLSv10, 0x0301)
        self.assertEqual(Security.tls_protocol_version_TLSv11, 0x0302)
        self.assertEqual(Security.tls_protocol_version_TLSv12, 0x0303)
        self.assertEqual(Security.tls_protocol_version_TLSv13, 0x0304)
        self.assertEqual(Security.tls_protocol_version_DTLSv10, 0xFEFF)
        self.assertEqual(Security.tls_protocol_version_DTLSv12, 0xFEFD)

        self.assertEqual(Security.tls_ciphersuite_RSA_WITH_3DES_EDE_CBC_SHA, 0x000A)
        self.assertEqual(Security.tls_ciphersuite_RSA_WITH_AES_128_CBC_SHA, 0x002F)
        self.assertEqual(Security.tls_ciphersuite_RSA_WITH_AES_256_CBC_SHA, 0x0035)
        self.assertEqual(Security.tls_ciphersuite_RSA_WITH_AES_128_GCM_SHA256, 0x009C)
        self.assertEqual(Security.tls_ciphersuite_RSA_WITH_AES_256_GCM_SHA384, 0x009D)
        self.assertEqual(Security.tls_ciphersuite_RSA_WITH_AES_128_CBC_SHA256, 0x003C)
        self.assertEqual(Security.tls_ciphersuite_RSA_WITH_AES_256_CBC_SHA256, 0x003D)
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA, 0xC008
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, 0xC009
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, 0xC00A
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, 0xC012
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_RSA_WITH_AES_128_CBC_SHA, 0xC013
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_RSA_WITH_AES_256_CBC_SHA, 0xC014
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256, 0xC023
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384, 0xC024
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_RSA_WITH_AES_128_CBC_SHA256, 0xC027
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_RSA_WITH_AES_256_CBC_SHA384, 0xC028
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, 0xC02B
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, 0xC02C
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_RSA_WITH_AES_128_GCM_SHA256, 0xC02F
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_RSA_WITH_AES_256_GCM_SHA384, 0xC030
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256, 0xCCA8
        )
        self.assertEqual(
            Security.tls_ciphersuite_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256, 0xCCA9
        )
        self.assertEqual(Security.tls_ciphersuite_AES_128_GCM_SHA256, 0x1301)
        self.assertEqual(Security.tls_ciphersuite_AES_256_GCM_SHA384, 0x1302)
        self.assertEqual(Security.tls_ciphersuite_CHACHA20_POLY1305_SHA256, 0x1303)

        self.assertEqual(Security.tls_ciphersuite_group_default, 0)
        self.assertEqual(Security.tls_ciphersuite_group_compatibility, 1)
        self.assertEqual(Security.tls_ciphersuite_group_legacy, 2)
        self.assertEqual(Security.tls_ciphersuite_group_ats, 3)
        self.assertEqual(Security.tls_ciphersuite_group_ats_compatibility, 4)

        self.assertEqual(Security.kSSLProtocolUnknown, 0)
        self.assertEqual(Security.kTLSProtocol1, 4)
        self.assertEqual(Security.kTLSProtocol11, 7)
        self.assertEqual(Security.kTLSProtocol12, 8)
        self.assertEqual(Security.kDTLSProtocol1, 9)
        self.assertEqual(Security.kTLSProtocol13, 10)
        self.assertEqual(Security.kDTLSProtocol12, 11)
        self.assertEqual(Security.kTLSProtocolMaxSupported, 999)
        self.assertEqual(Security.kSSLProtocol2, 1)
        self.assertEqual(Security.kSSLProtocol3, 2)
        self.assertEqual(Security.kSSLProtocol3Only, 3)
        self.assertEqual(Security.kTLSProtocol1Only, 5)
        self.assertEqual(Security.kSSLProtocolAll, 6)

    @min_os_level("10.14")
    def test_functions(self):
        self.assertResultIsRetained(Security.sec_trust_create)
        self.assertResultIsCFRetained(Security.sec_trust_copy_ref)

        self.assertResultIsRetained(Security.sec_identity_create)
        self.assertResultIsRetained(Security.sec_identity_create_with_certificates)
        self.assertResultIsCFRetained(Security.sec_identity_copy_ref)
        self.assertResultIsCFRetained(Security.sec_identity_copy_certificates_ref)

        self.assertResultIsRetained(Security.sec_certificate_create)
        self.assertResultIsCFRetained(Security.sec_certificate_copy_ref)

    @min_os_level("10.15")
    def test_functions10_15(self):
        self.assertArgIsBlock(Security.sec_identity_access_certificates, 1, b"v@")
