import Security
from PyObjCTools.TestSupport import TestCase, min_os_level

sec_protocol_key_update_complete_t = b"v"
sec_protocol_key_update_t = b"v@@?"
sec_protocol_challenge_complete_t = b"v@"
sec_protocol_challenge_t = b"v@@?"
sec_protocol_verify_complete_t = b"vB"
sec_protocol_verify_t = b"v@@@?"
sec_protocol_pre_shared_key_selection_t = b"v@@@?"


class TestSecProtocolOptions(TestCase):
    @min_os_level("10.14")
    def test_functions(self):
        Security.sec_protocol_options_set_local_identity
        Security.sec_protocol_options_add_tls_ciphersuite
        Security.sec_protocol_options_add_tls_ciphersuite_group
        Security.sec_protocol_options_set_tls_min_version
        Security.sec_protocol_options_set_tls_max_version
        Security.sec_protocol_options_add_tls_application_protocol
        Security.sec_protocol_options_set_tls_diffie_hellman_parameters

        self.assertArgHasType(
            Security.sec_protocol_options_set_tls_server_name, 1, b"n^t"
        )
        self.assertArgIsNullTerminated(
            Security.sec_protocol_options_set_tls_server_name, 1
        )

        Security.sec_protocol_options_add_pre_shared_key
        Security.sec_protocol_options_set_tls_tickets_enabled
        Security.sec_protocol_options_set_tls_is_fallback_attempt
        Security.sec_protocol_options_set_tls_resumption_enabled
        Security.sec_protocol_options_set_tls_false_start_enabled
        Security.sec_protocol_options_set_tls_ocsp_enabled
        Security.sec_protocol_options_set_tls_sct_enabled
        Security.sec_protocol_options_set_tls_renegotiation_enabled
        Security.sec_protocol_options_set_peer_authentication_required

    @min_os_level("10.15")
    def test_functions10_15(self):
        Security.sec_protocol_options_are_equal
        Security.sec_protocol_options_append_tls_ciphersuite
        Security.sec_protocol_options_append_tls_ciphersuite_group
        Security.sec_protocol_options_set_min_tls_protocol_version
        Security.sec_protocol_options_get_default_min_tls_protocol_version
        Security.sec_protocol_options_get_default_min_dtls_protocol_version
        Security.sec_protocol_options_set_max_tls_protocol_version
        Security.sec_protocol_options_get_default_max_tls_protocol_version
        Security.sec_protocol_options_get_default_max_dtls_protocol_version

        self.assertArgIsBlock(
            Security.sec_protocol_options_set_key_update_block,
            1,
            sec_protocol_key_update_t,
        )
        self.assertArgIsBlock(
            Security.sec_protocol_options_set_challenge_block,
            1,
            sec_protocol_challenge_t,
        )
        self.assertArgIsBlock(
            Security.sec_protocol_options_set_verify_block, 1, sec_protocol_verify_t
        )

        Security.sec_protocol_options_set_tls_pre_shared_key_identity_hint

        self.assertArgIsBlock(
            Security.sec_protocol_options_set_pre_shared_key_selection_block,
            1,
            sec_protocol_verify_t,
        )

    @min_os_level("10.16")
    def test_functions10_16(self):
        Security.sec_protocol_options_set_peer_authentication_optional
