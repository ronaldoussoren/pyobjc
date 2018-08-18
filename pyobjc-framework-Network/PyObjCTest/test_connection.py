from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Network

    class TestConnection (TestCase):
        def test_constants(self):
            self.assertEqual(Network.nw_connection_state_invalid, 0)
            self.assertEqual(Network.nw_connection_state_waiting, 1)
            self.assertEqual(Network.nw_connection_state_preparing, 2)
            self.assertEqual(Network.nw_connection_state_ready, 3)
            self.assertEqual(Network.nw_connection_state_failed, 4)
            self.assertEqual(Network.nw_connection_state_cancelled, 5)

            self.assertIsInstance(Network.NW_CONNECTION_SEND_IDEMPOTENT_CONTENT, objc.objc_object)
            self.assertIsInstance(Network.NW_CONNECTION_DEFAULT_MESSAGE_CONTEXT, objc.objc_object)
            self.assertIsInstance(Network.NW_CONNECTION_FINAL_MESSAGE_CONTEXT, objc.objc_object)
            self.assertIsInstance(Network.NW_CONNECTION_DEFAULT_STREAM_CONTEXT, objc.objc_object)

        def test_functions(self):
            self.assertResultHasType(Network.nw_connection_create, objc._C_ID)
            self.assertResultIsRetained(Network.nw_connection_create)
            self.assertArgHasType(Network.nw_connection_create, 0, objc._C_ID)
            self.assertArgHasType(Network.nw_connection_create, 1, objc._C_ID)

            self.assertResultHasType(Network.nw_connection_copy_endpoint, objc._C_ID)
            self.assertResultIsRetained(Network.nw_connection_copy_endpoint)
            self.assertArgHasType(Network.nw_connection_copy_endpoint, 0, objc._C_ID)

            self.assertResultHasType(Network.nw_connection_copy_parameters, objc._C_ID)
            self.assertResultIsRetained(Network.nw_connection_copy_parameters)
            self.assertArgHasType(Network.nw_connection_copy_parameters, 0, objc._C_ID)

            self.assertArgHasType(Network.nw_connection_set_state_changed_handler, 0, objc._C_ID)
            self.assertArgIsBlock(Network.nw_connection_set_state_changed_handler, 1, b'vi@')

            self.assertArgHasType(Network.nw_connection_set_viability_changed_handler, 0, objc._C_ID)
            self.assertArgIsBlock(Network.nw_connection_set_viability_changed_handler, 1, b'vB')

            self.assertArgHasType(Network.nw_connection_set_better_path_available_handler, 0, objc._C_ID)
            self.assertArgIsBlock(Network.nw_connection_set_better_path_available_handler, 1, b'vB')

            self.assertArgHasType(Network.nw_connection_set_path_changed_handler, 0, objc._C_ID)
            self.assertArgIsBlock(Network.nw_connection_set_path_changed_handler, 1, b'v@')

            self.assertArgHasType(Network.nw_connection_set_queue, 0, objc._C_ID)
            self.assertArgHasType(Network.nw_connection_set_queue, 1, objc._C_ID)

            self.assertArgHasType(Network.nw_connection_start, 0, objc._C_ID)

            self.assertArgHasType(Network.nw_connection_restart, 0, objc._C_ID)

            self.assertArgHasType(Network.nw_connection_cancel, 0, objc._C_ID)

            self.assertArgHasType(Network.nw_connection_force_cancel, 0, objc._C_ID)

            self.assertArgHasType(Network.nw_connection_cancel_current_endpoint, 0, objc._C_ID)

            self.assertArgHasType(Network.nw_connection_receive, 0, objc._C_ID)
            self.assertArgIsBlock(Network.nw_connection_receive, 3, b'v@@B@')

            self.assertArgHasType(Network.nw_connection_receive_message, 0, objc._C_ID)
            self.assertArgIsBlock(Network.nw_connection_receive_message, 1, b'v@@B@')


            self.assertArgIsBlock(Network.nw_connection_send, 4, b'v@')
            self.assertArgIsBlock(Network.nw_connection_batch, 1, b'v')

            # XXX: "the caller must call free", therefore need manual wrapper
            Network.nw_connection_copy_description

            self.assertResultIsRetained(Network.nw_connection_copy_current_path)
            self.assertResultIsRetained(Network.nw_connection_copy_protocol_metadata)

            Network.nw_connection_get_maximum_datagram_size





if __name__ == "__main__":
    main()
