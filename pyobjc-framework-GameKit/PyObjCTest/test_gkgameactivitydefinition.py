from PyObjCTools.TestSupport import TestCase, min_os_level
import GameKit


class TestGKGameActivityDefinition(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(GameKit.GKGameActivityDefinition.supportsPartyCode)
        self.assertResultIsBOOL(
            GameKit.GKGameActivityDefinition.supportsUnlimitedPlayers
        )
        self.assertArgIsBlock(
            GameKit.GKGameActivityDefinition.loadAchievementDescriptionsWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKGameActivityDefinition.loadLeaderboardsWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKGameActivityDefinition.loadImageWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKGameActivityDefinition.loadGameActivityDefinitionsWithIDs_completionHandler_,
            1,
            b"v@@",
        )
