from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter

GKChallengeComposeCompletionBlock = b"@Z@"


class TestGKChallenge(TestCase):
    def test_enums(self):
        self.assertIsEnumType(GameCenter.GKChallengeState)
        self.assertEqual(GameCenter.GKChallengeStateInvalid, 0)
        self.assertEqual(GameCenter.GKChallengeStatePending, 1)
        self.assertEqual(GameCenter.GKChallengeStateCompleted, 2)
        self.assertEqual(GameCenter.GKChallengeStateDeclined, 3)

    def test_methods(self):
        self.assertArgIsBlock(
            GameCenter.GKChallenge.loadReceivedChallengesWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameCenter.GKAchievement.selectChallengeablePlayerIDs_withCompletionHandler_,
            1,
            b"v@@",
        )

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertArgIsBlock(
            GameCenter.GKScore.challengeComposeControllerWithMessage_players_completionHandler_,
            2,
            GKChallengeComposeCompletionBlock,
        )
        self.assertArgIsBlock(
            GameCenter.GKScore.reportScores_withEligibleChallenges_withCompletionHandler_,
            2,
            b"v@",
        )

        self.assertArgIsBlock(
            GameCenter.GKAchievement.challengeComposeControllerWithMessage_players_completionHandler_,
            2,
            GKChallengeComposeCompletionBlock,
        )
        self.assertArgIsBlock(
            GameCenter.GKAchievement.selectChallengeablePlayers_withCompletionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameCenter.GKAchievement.reportAchievements_withEligibleChallenges_withCompletionHandler_,
            2,
            b"v@",
        )
