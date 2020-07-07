from PyObjCTools.TestSupport import TestCase, min_os_level

import Network


class TestConnectionGroup(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_connection_group_state_invalid, 0)
        self.assertEqual(Network.nw_connection_group_state_waiting, 1)
        self.assertEqual(Network.nw_connection_group_state_ready, 2)
        self.assertEqual(Network.nw_connection_group_state_failed, 3)
        self.assertEqual(Network.nw_connection_group_state_cancelled, 4)

    @min_os_level("10.16")
    def test_functions10_16(self):
        self.assertResultIsRetained(Network.nw_connection_group_create)
        self.assertResultIsRetained(Network.nw_connection_group_copy_descriptor)
        self.assertResultIsRetained(Network.nw_connection_group_copy_parameters)

        Network.nw_connection_group_set_queue

        nw_connection_group_state_changed_handler_t = b"vi@"

        self.assertArgIsBlock(
            Network.nw_connection_group_set_state_changed_handler,
            1,
            nw_connection_group_state_changed_handler_t,
        )

        nw_connection_group_receive_handler_t = b"v@@B"

        self.assertArgIsBlock(
            Network.nw_connection_group_set_receive_handler,
            3,
            nw_connection_group_receive_handler_t,
        )

        Network.nw_connection_group_start
        Network.nw_connection_group_cancel

        self.assertResultIsRetained(
            Network.nw_connection_group_copy_remote_endpoint_for_message
        )
        self.assertResultIsRetained(
            Network.nw_connection_group_copy_local_endpoint_for_message
        )
        self.assertResultIsRetained(
            Network.nw_connection_group_copy_local_endpoint_for_message
        )

        Network.nw_connection_group_reply

        self.assertResultIsRetained(
            Network.nw_connection_group_extract_connection_for_message
        )

        nw_connection_group_send_completion_t = b"v@"

        self.assertArgIsBlock(
            Network.nw_connection_group_send_message,
            4,
            nw_connection_group_send_completion_t,
        )
