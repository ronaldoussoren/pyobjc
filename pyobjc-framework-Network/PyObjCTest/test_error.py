from PyObjCTools.TestSupport import TestCase, min_os_level

import Network


class TestError(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_error_domain_invalid, 0)
        self.assertEqual(Network.nw_error_domain_posix, 1)
        self.assertEqual(Network.nw_error_domain_dns, 2)
        self.assertEqual(Network.nw_error_domain_tls, 3)
        self.assertEqual(Network.nw_error_domain_wifi_aware, 4)

        self.assertIsInstance(Network.kNWErrorDomainPOSIX, str)
        self.assertIsInstance(Network.kNWErrorDomainDNS, str)
        self.assertIsInstance(Network.kNWErrorDomainTLS, str)

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(Network.kNWErrorDomainWiFiAware, str)

    def test_functions(self):
        Network.nw_error_get_error_domain
        Network.nw_error_get_error_code

        self.assertResultIsCFRetained(Network.nw_error_copy_cf_error)
