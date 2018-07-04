from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Network

    class TestIPOptions (TestCase):
        def test_constants(self):
            self.assertEqual(Network.nw_ip_version_any, 0)
            self.assertEqual(Network.nw_ip_version_4, 4)
            self.assertEqual(Network.nw_ip_version_6, 6)

            self.assertEqual(Network.nw_ip_ecn_flag_non_ect, 0)
            self.assertEqual(Network.nw_ip_ecn_flag_ect_0, 2)
            self.assertEqual(Network.nw_ip_ecn_flag_ect_1, 1)
            self.assertEqual(Network.nw_ip_ecn_flag_ce, 3)

        def test_functions(self):
            Network.nw_ip_options_set_version
            Network.nw_ip_options_set_hop_limit
            Network.nw_ip_options_set_use_minimum_mtu
            Network.nw_ip_options_set_disable_fragmentation

            self.assertResultIsRetained(Network.nw_ip_create_metadata)

            Network.nw_protocol_metadata_is_ip
            Network.nw_ip_metadata_set_ecn_flag
            Network.nw_ip_metadata_get_ecn_flag
            Network.nw_ip_metadata_set_service_class
            Network.nw_ip_metadata_get_service_class
            Network.nw_ip_options_set_calculate_receive_time
            Network.nw_ip_metadata_get_receive_time

if __name__ == "__main__":
    main()

