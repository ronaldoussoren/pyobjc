import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestSecProtocolMetadata(TestCase):
    @min_os_level("10.14")
    def test_functions(self):
        self.assertResultIsNullTerminated(
            Security.sec_protocol_metadata_get_negotiated_protocol
        )
        self.assertResultHasType(
            Security.sec_protocol_metadata_get_negotiated_protocol, b"^t"
        )

        self.assertResultIsRetained(Security.sec_protocol_metadata_copy_peer_public_key)

        Security.sec_protocol_metadata_get_negotiated_protocol_version

        Security.sec_protocol_metadata_get_negotiated_ciphersuite

        self.assertResultHasType(
            Security.sec_protocol_metadata_get_early_data_accepted, objc._C_BOOL
        )

        self.assertResultHasType(
            Security.sec_protocol_metadata_access_peer_certificate_chain, objc._C_BOOL
        )
        self.assertArgIsBlock(
            Security.sec_protocol_metadata_access_peer_certificate_chain, 1, b"v@"
        )

        self.assertResultHasType(
            Security.sec_protocol_metadata_access_ocsp_response, objc._C_BOOL
        )
        self.assertArgIsBlock(
            Security.sec_protocol_metadata_access_ocsp_response, 1, b"v@"
        )

        self.assertResultHasType(
            Security.sec_protocol_metadata_access_supported_signature_algorithms,
            objc._C_BOOL,
        )
        self.assertArgIsBlock(
            Security.sec_protocol_metadata_access_supported_signature_algorithms,
            1,
            b"v" + objc._C_USHT,
        )

        self.assertResultHasType(
            Security.sec_protocol_metadata_access_distinguished_names, objc._C_BOOL
        )
        self.assertArgIsBlock(
            Security.sec_protocol_metadata_access_distinguished_names, 1, b"v@"
        )

        self.assertResultHasType(
            Security.sec_protocol_metadata_peers_are_equal, objc._C_BOOL
        )
        self.assertResultHasType(
            Security.sec_protocol_metadata_challenge_parameters_are_equal, objc._C_BOOL
        )

        self.assertResultIsRetained(Security.sec_protocol_metadata_create_secret)
        self.assertArgHasType(Security.sec_protocol_metadata_create_secret, 2, b"n^t")
        self.assertArgSizeInArg(Security.sec_protocol_metadata_create_secret, 2, 1)

        self.assertResultIsRetained(
            Security.sec_protocol_metadata_create_secret_with_context
        )
        self.assertArgHasType(
            Security.sec_protocol_metadata_create_secret_with_context, 2, b"n^t"
        )
        self.assertArgSizeInArg(
            Security.sec_protocol_metadata_create_secret_with_context, 2, 1
        )
        self.assertArgHasType(
            Security.sec_protocol_metadata_create_secret_with_context, 4, b"n^v"
        )
        self.assertArgSizeInArg(
            Security.sec_protocol_metadata_create_secret_with_context, 4, 3
        )

    @min_os_level("10.15")
    def test_functions10_14_missing(self):
        Security.sec_protocol_metadata_get_negotiated_tls_ciphersuite

        self.assertResultIsNullTerminated(
            Security.sec_protocol_metadata_get_server_name
        )
        self.assertResultHasType(Security.sec_protocol_metadata_get_server_name, b"^t")

    @min_os_level("10.15")
    def test_functions10_15(self):
        Security.sec_protocol_metadata_get_negotiated_tls_protocol_version

        self.assertArgIsBlock(
            Security.sec_protocol_metadata_access_pre_shared_keys, 1, b"v@@"
        )
        Security.sec_protocol_options_set_tls_pre_shared_key_identity_hint
