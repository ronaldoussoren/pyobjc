from PyObjCTools.TestSupport import TestCase

import Network


class TestError(TestCase):
    def test_constants(self):
        self.assertEqual(Network.nw_error_domain_invalid, 0)
        self.assertEqual(Network.nw_error_domain_posix, 1)
        self.assertEqual(Network.nw_error_domain_dns, 2)
        self.assertEqual(Network.nw_error_domain_tls, 3)

        self.assertIsInstance(Network.kNWErrorDomainPOSIX, str)
        self.assertIsInstance(Network.kNWErrorDomainDNS, str)
        self.assertIsInstance(Network.kNWErrorDomainTLS, str)

    def test_functions(self):
        Network.nw_error_get_error_domain
        Network.nw_error_get_error_code

        self.assertResultIsCFRetained(Network.nw_error_copy_cf_error)
