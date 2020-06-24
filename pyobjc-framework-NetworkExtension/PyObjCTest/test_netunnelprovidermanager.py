from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNETunnelProviderManager(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertArgIsBlock(
            NetworkExtension.NETunnelProviderManager.loadAllFromPreferencesWithCompletionHandler_,
            0,
            b"v@@",
        )
