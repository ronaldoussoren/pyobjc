from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Network

    class TestInterface (TestCase):
        def test_constants(self):
            self.assertEqual(Network.nw_endpoint_type_invalid, 0)
            self.assertEqual(Network.nw_endpoint_type_address, 1)
            self.assertEqual(Network.nw_endpoint_type_host, 2)
            self.assertEqual(Network.nw_endpoint_type_bonjour_service, 3)

        def test_functions(self):
            Network.nw_endpoint_get_type

            self.assertResultIsRetained(Network.nw_endpoint_create_host)
            self.assertArgIsIn(Network.nw_endpoint_create_host, 0)
            self.assertArgIsNullTerminated(Network.nw_endpoint_create_host, 0)
            self.assertArgIsIn(Network.nw_endpoint_create_host, 1)
            self.assertArgIsNullTerminated(Network.nw_endpoint_create_host, 1)

            self.assertResultIsNullTerminated(Network.nw_endpoint_get_hostname)

            self.assertResultIsNullTerminated(Network.nw_endpoint_copy_port_string)

            Network.nw_endpoint_get_port

            self.assertResultIsRetained(Network.nw_endpoint_create_address)
            self.assertArgIsIn(Network.nw_endpoint_create_address, 0)

            self.assertResultIsNullTerminated(Network.nw_endpoint_copy_address_string)

            Network.nw_endpoint_get_address # XXX Explicit test needed

            self.assertResultIsRetained(Network.nw_endpoint_create_bonjour_service)
            self.assertArgIsIn(Network.nw_endpoint_create_bonjour_service, 0)
            self.assertArgIsNullTerminated(Network.nw_endpoint_create_bonjour_service, 0)
            self.assertArgIsIn(Network.nw_endpoint_create_bonjour_service, 1)
            self.assertArgIsNullTerminated(Network.nw_endpoint_create_bonjour_service, 1)
            self.assertArgIsIn(Network.nw_endpoint_create_bonjour_service, 2)
            self.assertArgIsNullTerminated(Network.nw_endpoint_create_bonjour_service, 2)

            self.assertResultIsNullTerminated(Network.nw_endpoint_get_bonjour_service_name)
            self.assertResultIsNullTerminated(Network.nw_endpoint_get_bonjour_service_type)
            self.assertResultIsNullTerminated(Network.nw_endpoint_get_bonjour_service_domain)

if __name__ == "__main__":
    main()
