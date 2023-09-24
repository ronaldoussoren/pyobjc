from PyObjCTools.TestSupport import TestCase, min_os_level

import Network

nw_path_enumerate_interfaces_block_t = b"B@"
nw_path_enumerate_gateways_block_t = b"B@"


class TestPath(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_path_status_invalid, 0)
        self.assertEqual(Network.nw_path_status_satisfied, 1)
        self.assertEqual(Network.nw_path_status_unsatisfied, 2)
        self.assertEqual(Network.nw_path_status_satisfiable, 3)

        self.assertEqual(Network.nw_path_unsatisfied_reason_not_available, 0)
        self.assertEqual(Network.nw_path_unsatisfied_reason_cellular_denied, 1)
        self.assertEqual(Network.nw_path_unsatisfied_reason_wifi_denied, 2)
        self.assertEqual(Network.nw_path_unsatisfied_reason_local_network_denied, 3)
        self.assertEqual(Network.nw_path_unsatisfied_reason_vpn_inactive, 4)

    def test_functions(self):
        Network.nw_path_get_status

        self.assertArgIsBlock(
            Network.nw_path_enumerate_interfaces,
            1,
            nw_path_enumerate_interfaces_block_t,
        )

        Network.nw_path_is_equal
        Network.nw_path_is_expensive
        Network.nw_path_has_ipv4
        Network.nw_path_has_ipv6
        Network.nw_path_has_dns
        Network.nw_path_uses_interface_type

        self.assertResultIsRetained(Network.nw_path_copy_effective_local_endpoint)

        self.assertResultIsRetained(Network.nw_path_copy_effective_remote_endpoint)

    @min_os_level("10.15")
    def test_functions10_15(self):
        Network.nw_path_is_constrained

        self.assertArgIsBlock(
            Network.nw_path_enumerate_gateways, 1, nw_path_enumerate_gateways_block_t
        )

    @min_os_level("11.0")
    def test_functions11_0(self):
        Network.nw_path_get_unsatisfied_reason
