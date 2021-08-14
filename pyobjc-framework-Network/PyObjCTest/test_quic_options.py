from PyObjCTools.TestSupport import TestCase, min_os_level

import Network


class TestQUICOptions(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_quic_stream_type_unknown, 0)
        self.assertEqual(Network.nw_quic_stream_type_bidirectional, 1)
        self.assertEqual(Network.nw_quic_stream_type_unidirectional, 2)

    @min_os_level("12.0")
    def test_functions12_0(self):
        self.assertResultIsRetained(Network.nw_protocol_copy_quic_definition)
        self.assertResultIsRetained(Network.nw_quic_create_options)
        Network.nw_protocol_options_is_quic
        Network.nw_quic_add_tls_application_protocol
        self.assertResultIsRetained(Network.nw_quic_copy_sec_protocol_options)
        Network.nw_quic_get_stream_is_unidirectional
        Network.nw_quic_set_stream_is_unidirectional
        Network.nw_quic_get_initial_max_data
        Network.nw_quic_set_initial_max_data
        Network.nw_quic_get_max_udp_payload_size
        Network.nw_quic_set_max_udp_payload_size
        Network.nw_quic_get_idle_timeout
        Network.nw_quic_set_idle_timeout
        Network.nw_quic_get_initial_max_streams_bidirectional
        Network.nw_quic_set_initial_max_streams_bidirectional
        Network.nw_quic_get_initial_max_streams_unidirectional
        Network.nw_quic_set_initial_max_streams_unidirectional
        Network.nw_quic_get_initial_max_stream_data_bidirectional_local
        Network.nw_quic_set_initial_max_stream_data_bidirectional_local
        Network.nw_quic_get_initial_max_stream_data_bidirectional_remote
        Network.nw_quic_set_initial_max_stream_data_bidirectional_remote
        Network.nw_quic_get_initial_max_stream_data_unidirectional
        Network.nw_quic_set_initial_max_stream_data_unidirectional
        Network.nw_protocol_metadata_is_quic
        self.assertResultIsRetained(Network.nw_quic_copy_sec_protocol_metadata)
        Network.nw_quic_get_stream_application_error
        Network.nw_quic_set_stream_application_error
        Network.nw_quic_get_local_max_streams_bidirectional
        Network.nw_quic_set_local_max_streams_bidirectional
        Network.nw_quic_get_local_max_streams_unidirectional
        Network.nw_quic_set_local_max_streams_unidirectional
        Network.nw_quic_get_remote_max_streams_bidirectional
        Network.nw_quic_get_application_error
        Network.nw_quic_get_stream_id
        self.assertResultIsNullTerminated(Network.nw_quic_get_application_error_reason)
        self.assertArgIsNullTerminated(Network.nw_quic_set_application_error, 2)
        Network.nw_quic_get_keepalive_interval
        Network.nw_quic_set_keepalive_interval
        Network.nw_quic_get_remote_idle_timeout
