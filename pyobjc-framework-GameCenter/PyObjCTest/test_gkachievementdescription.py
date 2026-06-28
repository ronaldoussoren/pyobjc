from PyObjCTools.TestSupport import TestCase

import GameCenter


class TestGCAchievementDescription(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            GameCenter.GKAchievementDescription.loadAchievementDescriptionsWithCompletionHandler_,
            0,
            b"v@@",
        )

        self.assertArgIsBlock(
            GameCenter.GKAchievementDescription.loadImageWithCompletionHandler_,
            0,
            b"v@@",
        )

        obj = GameCenter.GKAchievementDescription()
        self.assertResultIsBOOL(obj.isHidden)
        self.assertResultIsBOOL(obj.isReplayable)
