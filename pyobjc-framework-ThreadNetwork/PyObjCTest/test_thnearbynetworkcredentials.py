from PyObjCTools.TestSupport import TestCase, min_os_level

import ThreadNetwork


class TestTHNearbyNetworkCredentials(TestCase):
    @min_os_level("27.3")
    def test_methods(self):
        self.assertResultIsBOOL(
            ThreadNetwork.THNearbyNetworkCredentials.isPreferredNetworkCredentials
        )
