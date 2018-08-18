from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import Network

    class TestContentContext (TestCase):
        def test_functions(self):
            self.assertResultIsRetained(Network.nw_content_context_create)
            self.assertArgIsIn(Network.nw_content_context_create, 0)
            self.assertArgIsNullTerminated(Network.nw_content_context_create, 0)

            self.assertResultIsNullTerminated(Network.nw_content_context_get_identifier)

            Network.nw_content_context_get_is_final
            Network.nw_content_context_set_is_final
            Network.nw_content_context_get_expiration_milliseconds
            Network.nw_content_context_set_expiration_milliseconds
            Network.nw_content_context_get_relative_priority
            Network.nw_content_context_set_relative_priority
            Network.nw_content_context_set_antecedent

            self.assertResultIsRetained(Network.nw_content_context_copy_antecedent)

            Network.nw_content_context_set_metadata_for_protocol

            self.assertResultIsRetained(Network.nw_content_context_copy_protocol_metadata)

            self.assertArgIsBlock(Network.nw_content_context_foreach_protocol_metadata, 1, b'v@@')

if __name__ == "__main__":
    main()

