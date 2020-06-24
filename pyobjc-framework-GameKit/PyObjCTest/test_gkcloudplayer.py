import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestGKCloudPlayer(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsBlock(
            GameKit.GKCloudPlayer.getCurrentSignedInPlayerForContainer_completionHandler_,
            1,
            b"v@@",
        )
