from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Network

    class TestError (TestCase):
        def test_constants(self):
            self.assertEqual(Network.nw_error_domain_invalid, 0)
            self.assertEqual(Network.nw_error_domain_posix, 1)
            self.assertEqual(Network.nw_error_domain_dns, 2)
            self.assertEqual(Network.nw_error_domain_tls, 3)

            self.assertIsInstance(Network.kNWErrorDomainPOSIX, unicode)
            self.assertIsInstance(Network.kNWErrorDomainDNS, unicode)
            self.assertIsInstance(Network.kNWErrorDomainTLS, unicode)


        def test_functions(self):
            Network.nw_error_get_error_domain
            Network.nw_error_get_error_code

            self.assertResultIsCFRetained(Network.nw_error_copy_cf_error)

if __name__ == "__main__":
    main()
