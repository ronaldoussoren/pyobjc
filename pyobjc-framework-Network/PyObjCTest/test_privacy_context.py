from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import Network


class TestPrivacyContext(TestCase):
    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(Network.NW_DEFAULT_PRIVACY_CONTEXT, objc.objc_object)

    @min_os_level("11.0")
    def test_functions11_0(self):
        self.assertResultIsRetained(Network.nw_privacy_context_create)
        self.assertArgIsIn(Network.nw_privacy_context_create, 0)
        self.assertArgIsNullTerminated(Network.nw_privacy_context_create, 0)

        Network.nw_privacy_context_flush_cache
        Network.nw_privacy_context_disable_logging
        Network.nw_privacy_context_require_encrypted_name_resolution
