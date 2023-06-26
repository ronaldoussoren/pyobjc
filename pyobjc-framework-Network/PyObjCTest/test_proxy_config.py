from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import Network


class TestProxyConfig(TestCase):
    @min_os_level("14.0")
    def test_functions(self):
        self.assertResultHasType(Network.nw_relay_hop_create, objc._C_ID)
        self.assertResultIsRetained(Network.nw_relay_hop_create)

        self.assertArgHasType(
            Network.nw_relay_hop_add_additional_http_header_field, 1, "n^t"
        )
        self.assertArgIsNullDelimited(
            Network.nw_relay_hop_add_additional_http_header_field, 1
        )
        self.assertArgHasType(
            Network.nw_relay_hop_add_additional_http_header_field, 2, "n^t"
        )
        self.assertArgIsNullDelimited(
            Network.nw_relay_hop_add_additional_http_header_field, 2
        )

        self.assertResultHasType(Network.nw_proxy_config_create_relay, objc._C_ID)
        self.assertResultIsRetained(Network.nw_proxy_config_create_relay)

        self.assertResultHasType(
            Network.nw_proxy_config_create_oblivious_http, objc._C_ID
        )
        self.assertResultIsRetained(Network.nw_proxy_config_create_oblivious_http)
        self.assertArgHasType(Network.nw_proxy_config_create_oblivious_http, 1, "n^t")
        self.assertArgIsNullDelimited(Network.nw_proxy_config_create_oblivious_http, 1)
        self.assertArgHasType(Network.nw_proxy_config_create_oblivious_http, 2, "n^v")
        self.assertArgSizeInArg(Network.nw_proxy_config_create_oblivious_http, 2, 3)

        self.assertResultHasType(
            Network.nw_proxy_config_create_http_connect, objc._C_ID
        )
        self.assertResultIsRetained(Network.nw_proxy_config_create_http_connect)

        self.assertResultHasType(Network.nw_proxy_config_create_socksv5, objc._C_ID)
        self.assertResultIsRetained(Network.nw_proxy_config_create_socksv5)

        self.assertArgHasType(
            Network.nw_proxy_config_set_username_and_password, 1, "n^t"
        )
        self.assertArgIsNullDelimited(
            Network.nw_proxy_config_set_username_and_password, 1
        )
        self.assertArgHasType(
            Network.nw_proxy_config_set_username_and_password, 2, "n^t"
        )
        self.assertArgIsNullDelimited(
            Network.nw_proxy_config_set_username_and_password, 2
        )

        Network.nw_proxy_config_set_failover_allowed
        Network.nw_proxy_config_get_failover_allowed
