import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level


if hasattr(GameKit, "GKLeaderboardSet"):

    class TestGKLeaderboardSetHelper(GameKit.GKLeaderboardSet):
        def loadImageWithCompletionHandler_(self, h):
            pass


class TestGKLeaderboardSet(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertArgIsBlock(
            GameKit.GKLeaderboardSet.loadLeaderboardSetsWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKLeaderboardSet.loadLeaderboardsWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            TestGKLeaderboardSetHelper.loadImageWithCompletionHandler_, 0, b"v@@"
        )

    @min_os_level("10.16")
    def testMethods10_16(self):
        self.assertArgIsBlock(
            GameKit.GKLeaderboardSet.loadLeaderboardsWithHandler_, 0, b"v@@"
        )
