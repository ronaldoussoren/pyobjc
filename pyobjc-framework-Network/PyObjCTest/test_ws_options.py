from PyObjCTools.TestSupport import TestCase, min_os_level

import Network

nw_ws_pong_handler_t = b"v@"
nw_ws_subprotocol_enumerator_t = b"Bn^t"
nw_ws_additional_header_enumerator_t = b"Bn^tn^t"
nw_ws_client_request_handler_t = b"@@"


class TestWSOptions(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_ws_opcode_invalid, -1)
        self.assertEqual(Network.nw_ws_opcode_cont, 0x0)
        self.assertEqual(Network.nw_ws_opcode_text, 0x1)
        self.assertEqual(Network.nw_ws_opcode_binary, 0x2)
        self.assertEqual(Network.nw_ws_opcode_close, 0x8)
        self.assertEqual(Network.nw_ws_opcode_ping, 0x9)
        self.assertEqual(Network.nw_ws_opcode_pong, 0xA)

        self.assertEqual(Network.nw_ws_close_code_normal_closure, 1000)
        self.assertEqual(Network.nw_ws_close_code_going_away, 1001)
        self.assertEqual(Network.nw_ws_close_code_protocol_error, 1002)
        self.assertEqual(Network.nw_ws_close_code_unsupported_data, 1003)
        self.assertEqual(Network.nw_ws_close_code_no_status_received, 1005)
        self.assertEqual(Network.nw_ws_close_code_abnormal_closure, 1006)
        self.assertEqual(Network.nw_ws_close_code_invalid_frame_payload_data, 1007)
        self.assertEqual(Network.nw_ws_close_code_policy_violation, 1008)
        self.assertEqual(Network.nw_ws_close_code_message_too_big, 1009)
        self.assertEqual(Network.nw_ws_close_code_mandatory_extension, 1010)
        self.assertEqual(Network.nw_ws_close_code_internal_server_error, 1011)
        self.assertEqual(Network.nw_ws_close_code_tls_handshake, 1015)

        self.assertEqual(Network.nw_ws_version_13, 1)

        self.assertEqual(Network.nw_ws_response_status_invalid, 0)
        self.assertEqual(Network.nw_ws_response_status_accept, 1)
        self.assertEqual(Network.nw_ws_response_status_reject, 2)

    @min_os_level("10.15")
    def test_functions10_15(self):
        self.assertResultIsRetained(Network.nw_protocol_copy_ws_definition)
        self.assertResultIsRetained(Network.nw_ws_create_options)

        Network.nw_ws_options_add_additional_header
        Network.nw_ws_options_add_subprotocol
        Network.nw_ws_options_set_auto_reply_ping
        Network.nw_ws_options_set_skip_handshake
        Network.nw_ws_options_set_maximum_message_size
        Network.nw_protocol_metadata_is_ws

        self.assertResultIsRetained(Network.nw_ws_create_metadata)

        Network.nw_ws_metadata_get_opcode
        Network.nw_ws_metadata_set_close_code
        Network.nw_ws_metadata_get_close_code

        self.assertArgIsBlock(
            Network.nw_ws_metadata_set_pong_handler, 2, nw_ws_pong_handler_t
        )
        self.assertArgIsBlock(
            Network.nw_ws_request_enumerate_subprotocols,
            1,
            nw_ws_subprotocol_enumerator_t,
        )
        self.assertArgIsBlock(
            Network.nw_ws_request_enumerate_additional_headers,
            1,
            nw_ws_additional_header_enumerator_t,
        )

        self.assertResultIsRetained(Network.nw_ws_response_create)
        self.assertArgHasType(Network.nw_ws_response_create, 1, b"n^t")
        self.assertArgSizeInArg(Network.nw_ws_response_create, 1, 2)

        Network.nw_ws_response_get_status

        self.assertResultIsNullTerminated(
            Network.nw_ws_response_get_selected_subprotocol
        )
        self.assertResultHasType(Network.nw_ws_response_get_selected_subprotocol, b"^t")

        self.assertArgHasType(Network.nw_ws_response_add_additional_header, 1, b"n^t")
        self.assertArgIsNullTerminated(Network.nw_ws_response_add_additional_header, 1)
        self.assertArgHasType(Network.nw_ws_response_add_additional_header, 2, b"n^t")
        self.assertArgIsNullTerminated(Network.nw_ws_response_add_additional_header, 2)

        self.assertResultIsRetained(Network.nw_ws_metadata_copy_server_response)

        self.assertArgIsBlock(
            Network.nw_ws_response_enumerate_additional_headers,
            1,
            nw_ws_additional_header_enumerator_t,
        )
        self.assertArgIsBlock(
            Network.nw_ws_options_set_client_request_handler,
            2,
            nw_ws_client_request_handler_t,
        )
