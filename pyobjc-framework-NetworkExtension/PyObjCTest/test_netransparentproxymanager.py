from PyObjCTools.TestSupport import TestCase, min_os_level

import NetworkExtension


class TestNETransparentProxyManager(TestCase):
    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            NetworkExtension.NETransparentProxyManager.loadAllFromPreferencesWithCompletionHandler_,
            0,
            b"v@@",
        )
