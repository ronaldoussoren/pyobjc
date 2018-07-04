from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Network

    nw_parameters_configure_protocol_block_t = b'v@'
    nw_parameters_iterate_interfaces_block_t = b'B@'
    nw_parameters_iterate_interface_types_block_t = b'Bi'
    nw_protocol_stack_iterate_protocols_block_t = b'v@'

    class TestParameters (TestCase):
        def test_constants(self):
            self.assertIsInstance(Network.NW_PARAMETERS_DEFAULT_CONFIGURATION, objc.objc_object)
            self.assertIsInstance(Network.NW_PARAMETERS_DISABLE_PROTOCOL, objc.objc_object)

            self.assertEqual(Network.nw_service_class_best_effort, 0)
            self.assertEqual(Network.nw_service_class_background, 1)
            self.assertEqual(Network.nw_service_class_interactive_video, 2)
            self.assertEqual(Network.nw_service_class_interactive_voice, 3)
            self.assertEqual(Network.nw_service_class_responsive_data, 4)
            self.assertEqual(Network.nw_service_class_signaling, 5)

            self.assertEqual(Network.nw_multipath_service_disabled, 0)
            self.assertEqual(Network.nw_multipath_service_handover, 1)
            self.assertEqual(Network.nw_multipath_service_interactive, 2)
            self.assertEqual(Network.nw_multipath_service_aggregate, 3)

            self.assertEqual(Network.nw_parameters_expired_dns_behavior_default, 0)
            self.assertEqual(Network.nw_parameters_expired_dns_behavior_allow, 1)
            self.assertEqual(Network.nw_parameters_expired_dns_behavior_prohibit, 2)

        def test_functions(self):
            self.assertResultIsRetained(Network.nw_parameters_create_secure_tcp)
            self.assertArgIsBlock(Network.nw_parameters_create_secure_tcp, 1, nw_parameters_configure_protocol_block_t)

            self.assertResultIsRetained(Network.nw_parameters_create_secure_udp)
            self.assertArgIsBlock(Network.nw_parameters_create_secure_udp, 1, nw_parameters_configure_protocol_block_t)

            self.assertResultIsRetained(Network.nw_parameters_create)
            self.assertResultIsRetained(Network.nw_parameters_copy)

            Network.nw_parameters_require_interface
            self.assertResultIsRetained(Network.nw_parameters_copy_required_interface)

            Network.nw_parameters_prohibit_interface
            Network.nw_parameters_clear_prohibited_interfaces

            self.assertArgIsBlock(Network.nw_parameters_iterate_prohibited_interfaces, 1, nw_parameters_iterate_interfaces_block_t)

            Network.nw_parameters_set_required_interface_type
            Network.nw_parameters_get_required_interface_type
            Network.nw_parameters_prohibit_interface_type

            Network.nw_parameters_clear_prohibited_interface_types

            self.assertArgIsBlock(Network.nw_parameters_iterate_prohibited_interface_types, 1, nw_parameters_iterate_interface_types_block_t)

            Network.nw_parameters_set_prohibit_expensive
            Network.nw_parameters_get_prohibit_expensive
            Network.nw_parameters_set_reuse_local_address
            Network.nw_parameters_get_reuse_local_address
            Network.nw_parameters_set_local_endpoint

            self.assertResultIsRetained(Network.nw_parameters_copy_local_endpoint)

            Network.nw_parameters_set_fast_open_enabled
            Network.nw_parameters_get_fast_open_enabled
            Network.nw_parameters_set_service_class
            Network.nw_parameters_get_service_class
            Network.nw_parameters_set_multipath_service
            Network.nw_parameters_get_multipath_service

            self.assertResultIsRetained(Network.nw_parameters_copy_default_protocol_stack)

            Network.nw_protocol_stack_prepend_application_protocol
            Network.nw_protocol_stack_clear_application_protocols

            self.assertArgIsBlock(Network.nw_protocol_stack_iterate_application_protocols, 1, nw_protocol_stack_iterate_protocols_block_t)

            self.assertResultIsRetained(Network.nw_protocol_stack_copy_transport_protocol)

            Network.nw_protocol_stack_set_transport_protocol

            self.assertResultIsRetained(Network.nw_protocol_stack_copy_internet_protocol)

            Network.nw_parameters_set_local_only
            Network.nw_parameters_get_local_only
            Network.nw_parameters_set_prefer_no_proxy
            Network.nw_parameters_get_prefer_no_proxy
            Network.nw_parameters_set_expired_dns_behavior
            Network.nw_parameters_get_expired_dns_behavior
            Network.nw_parameters_set_include_peer_to_peer
            Network.nw_parameters_get_include_peer_to_peer

if __name__ == "__main__":
    main()
