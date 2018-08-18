from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Network

    class TestUDPOptions (TestCase):
        def test_functions(self):
            self.assertResultIsRetained(Network.nw_protocol_copy_udp_definition)

            self.assertResultIsRetained(Network.nw_udp_create_options)

            Network.nw_udp_options_set_prefer_no_checksum

            self.assertResultIsRetained(Network.nw_udp_create_metadata)

            Network.nw_protocol_metadata_is_udp


if __name__ == "__main__":
    main()
