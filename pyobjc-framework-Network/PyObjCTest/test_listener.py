from PyObjCTools.TestSupport import TestCase, min_os_level

import Network

nw_listener_state_changed_handler_t = b"vi@"
nw_listener_new_connection_handler_t = b"v@"
nw_listener_advertised_endpoint_changed_handler_t = b"v@B"


class TestListener(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_listener_state_invalid, 0)
        self.assertEqual(Network.nw_listener_state_waiting, 1)
        self.assertEqual(Network.nw_listener_state_ready, 2)
        self.assertEqual(Network.nw_listener_state_failed, 3)
        self.assertEqual(Network.nw_listener_state_cancelled, 4)

        self.assertEqual(Network.NW_LISTENER_INFINITE_CONNECTION_LIMIT, 0xFFFFFFFF)

    def test_functions(self):
        self.assertResultIsRetained(Network.nw_listener_create_with_port)

        self.assertResultIsRetained(Network.nw_listener_create)

        self.assertResultIsRetained(Network.nw_listener_create_with_connection)

        Network.nw_listener_set_queue

        self.assertArgIsBlock(
            Network.nw_listener_set_state_changed_handler,
            1,
            nw_listener_state_changed_handler_t,
        )

        self.assertArgIsBlock(
            Network.nw_listener_set_new_connection_handler,
            1,
            nw_listener_new_connection_handler_t,
        )

        Network.nw_listener_set_advertise_descriptor

        self.assertArgIsBlock(
            Network.nw_listener_set_advertised_endpoint_changed_handler,
            1,
            nw_listener_advertised_endpoint_changed_handler_t,
        )

        Network.nw_listener_get_port
        Network.nw_listener_start
        Network.nw_listener_cancel

    @min_os_level("10.15")
    def test_functions10_15(self):
        Network.nw_listener_get_new_connection_limit
        Network.nw_listener_set_new_connection_limit
