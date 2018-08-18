from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Network

    nw_path_enumerate_interfaces_block_t = b'B@'

    class TestPath (TestCase):
        def test_constants(self):
            self.assertEqual(Network.nw_path_status_invalid, 0)
            self.assertEqual(Network.nw_path_status_satisfied, 1)
            self.assertEqual(Network.nw_path_status_unsatisfied, 2)
            self.assertEqual(Network.nw_path_status_satisfiable, 3)

        def test_functions(self):
            Network.nw_path_get_status

            self.assertArgIsBlock(Network.nw_path_enumerate_interfaces, 1, nw_path_enumerate_interfaces_block_t)

            Network.nw_path_is_equal
            Network.nw_path_is_expensive
            Network.nw_path_has_ipv4
            Network.nw_path_has_ipv6
            Network.nw_path_has_dns
            Network.nw_path_uses_interface_type

            self.assertResultIsRetained(Network.nw_path_copy_effective_local_endpoint)

            self.assertResultIsRetained(Network.nw_path_copy_effective_remote_endpoint)


if __name__ == "__main__":
    main()
