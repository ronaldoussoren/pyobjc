from PyObjCTools.TestSupport import TestCase, min_os_level

import Network


class TestGroupDescriptor(TestCase):
    @min_os_level("11.0")
    def test_functions11_0(self):
        self.assertResultIsRetained(Network.nw_group_descriptor_create_multicast)
        Network.nw_group_descriptor_add_endpoint

        nw_group_descriptor_enumerate_endpoints_block_t = b"B@"

        self.assertArgIsBlock(
            Network.nw_group_descriptor_enumerate_endpoints,
            1,
            nw_group_descriptor_enumerate_endpoints_block_t,
        )

        Network.nw_multicast_group_descriptor_set_specific_source
        Network.nw_multicast_group_descriptor_set_disable_unicast_traffic
        Network.nw_multicast_group_descriptor_get_disable_unicast_traffic

    @min_os_level("12.0")
    def test_functions12_0(self):
        self.assertResultIsRetained(Network.nw_group_descriptor_create_multiplex)
