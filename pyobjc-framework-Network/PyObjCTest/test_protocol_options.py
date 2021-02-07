from PyObjCTools.TestSupport import TestCase

import Network


class TestProtocolOptions(TestCase):
    def test_functions(self):
        Network.nw_protocol_definition_is_equal

        self.assertResultIsRetained(Network.nw_protocol_options_copy_definition)

        self.assertResultIsRetained(Network.nw_protocol_metadata_copy_definition)
