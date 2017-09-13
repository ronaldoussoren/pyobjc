from PyObjCTools.TestSupport import *

import GameKit

GKChallengeComposeCompletionBlock = b'v@Z@'

class TestGKChallenge (TestCase):

    def testConstants(self):
        self.assertEqual(GameKit.GKChallengeStateInvalid, 0)
        self.assertEqual(GameKit.GKChallengeStatePending, 1)
        self.assertEqual(GameKit.GKChallengeStateCompleted, 2)
        self.assertEqual(GameKit.GKChallengeStateDeclined, 3)

    def testMethods(self):
        self.assertArgIsBlock(GameKit.GKChallenge.loadReceivedChallengesWithCompletionHandler, 0, b'v@@')

        self.assertArgIsBlock(GameKit.GKAchievement.selectChallengeablePlayerIDs_withCompletionHandler_, 1, b'v@@')

    @min_os_level('10.10')
    def testMethods(self):
        self.assertArgIsBlock(GameKit.GKScore.challengeComposeControllerWithMessage_players_completionHandler_, 2, GKChallengeComposeCompletionBlock)
        self.assertArgIsBlock(GameKit.GKScore.reportScores_withEligibleChallenges_withCompletionHandler_, 2, b'v@')
        self.assertArgIsBlock(GameKit.GKAchievement.challengeComposeControllerWithMessage_players_completionHandler_, 2, GKChallengeComposeCompletionBlock)
        self.assertArgIsBlock(GameKit.GKAchievement.selectChallengeablePlayers_withCompletionHandler_, 1, b'v@@')
        self.assertArgIsBlock(GameKit.GKAchievement.reportAchievements_withEligibleChallenges_withCompletionHandler_, 2, b'v@')



if __name__ == "__main__":
    main()
