from PyObjCTools.TestSupport import TestCase

import Network


class TestTCPOptions(TestCase):
    def test_functions(self):
        self.assertResultIsRetained(Network.nw_protocol_copy_tcp_definition)

        self.assertResultIsRetained(Network.nw_tcp_create_options)

        Network.nw_tcp_options_set_no_delay
        Network.nw_tcp_options_set_no_push
        Network.nw_tcp_options_set_no_options
        Network.nw_tcp_options_set_enable_keepalive
        Network.nw_tcp_options_set_keepalive_count
        Network.nw_tcp_options_set_keepalive_idle_time
        Network.nw_tcp_options_set_keepalive_interval
        Network.nw_tcp_options_set_maximum_segment_size
        Network.nw_tcp_options_set_connection_timeout
        Network.nw_tcp_options_set_persist_timeout
        Network.nw_tcp_options_set_retransmit_connection_drop_time
        Network.nw_tcp_options_set_retransmit_fin_drop
        Network.nw_tcp_options_set_disable_ack_stretching
        Network.nw_tcp_options_set_enable_fast_open
        Network.nw_tcp_options_set_disable_ecn
        Network.nw_protocol_metadata_is_tcp
        Network.nw_tcp_get_available_receive_buffer
        Network.nw_tcp_get_available_send_buffer
