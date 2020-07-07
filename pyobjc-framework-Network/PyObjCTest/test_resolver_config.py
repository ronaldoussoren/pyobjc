from PyObjCTools.TestSupport import TestCase, min_os_level

import Network


class TestResolverConfig(TestCase):
    @min_os_level("10.16")
    def test_functions(self):
        self.assertResultIsRetained(Network.nw_resolver_config_create_https)
        self.assertResultIsRetained(Network.nw_resolver_config_create_tls)

        Network.nw_resolver_config_add_server_address
