import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level

GKChallengeComposeCompletionBlock = b"v@Z@"


class TestGKChallenge(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameKit.GKChallengeState)

    def testConstants(self):
        self.assertEqual(GameKit.GKChallengeStateInvalid, 0)
        self.assertEqual(GameKit.GKChallengeStatePending, 1)
        self.assertEqual(GameKit.GKChallengeStateCompleted, 2)
        self.assertEqual(GameKit.GKChallengeStateDeclined, 3)

    def testMethods(self):
        self.assertArgIsBlock(
            GameKit.GKChallenge.loadReceivedChallengesWithCompletionHandler_, 0, b"v@@"
        )

        self.assertArgIsBlock(
            GameKit.GKAchievement.selectChallengeablePlayerIDs_withCompletionHandler_,
            1,
            b"v@@",
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            GameKit.GKScore.challengeComposeControllerWithMessage_players_completionHandler_,
            2,
            GKChallengeComposeCompletionBlock,
        )
        self.assertArgIsBlock(
            GameKit.GKScore.reportScores_withEligibleChallenges_withCompletionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKAchievement.challengeComposeControllerWithMessage_players_completionHandler_,
            2,
            GKChallengeComposeCompletionBlock,
        )
        self.assertArgIsBlock(
            GameKit.GKAchievement.selectChallengeablePlayers_withCompletionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKAchievement.reportAchievements_withEligibleChallenges_withCompletionHandler_,
            2,
            b"v@",
        )

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertArgIsBlock(
            GameKit.GKScore.reportLeaderboardScores_withEligibleChallenges_withCompletionHandler_,
            2,
            b"v@",
        )
