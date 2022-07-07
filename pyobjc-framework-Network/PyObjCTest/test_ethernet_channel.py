from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import Network

nw_ethernet_channel_state_changed_handler_t = b"v@@"
nw_ethernet_channel_receive_handler_t = b"v@" + objc._C_USHT + b"n[6t]n[6t]"
nw_ethernet_channel_send_completion_t = b"v@"


class TestEtherChannel(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_ethernet_channel_state_invalid, 0)
        self.assertEqual(Network.nw_ethernet_channel_state_waiting, 1)
        self.assertEqual(Network.nw_ethernet_channel_state_preparing, 2)
        self.assertEqual(Network.nw_ethernet_channel_state_ready, 3)
        self.assertEqual(Network.nw_ethernet_channel_state_failed, 4)
        self.assertEqual(Network.nw_ethernet_channel_state_cancelled, 5)

    @min_os_level("10.15")
    def test_functions10_15(self):
        self.assertResultIsRetained(Network.nw_ethernet_channel_create)

        self.assertArgIsBlock(
            Network.nw_ethernet_channel_set_state_changed_handler,
            1,
            nw_ethernet_channel_state_changed_handler_t,
        )

        Network.nw_ethernet_channel_set_queue
        Network.nw_ethernet_channel_start
        Network.nw_ethernet_channel_cancel

        self.assertArgIsBlock(
            Network.nw_ethernet_channel_set_receive_handler,
            1,
            nw_ethernet_channel_receive_handler_t,
        )
        self.assertArgIsBlock(
            Network.nw_ethernet_channel_send, 4, nw_ethernet_channel_send_completion_t
        )

    @min_os_level("13.0")
    def test_functions13_0(self):
        self.assertResultIsRetained(Network.nw_ethernet_channel_create_with_parameters)

        Network.nw_ethernet_channel_get_maximum_payload_size
