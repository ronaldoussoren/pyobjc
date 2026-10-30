from PyObjCTools.TestSupport import TestCase

import GameplayKit


class TestGKGoal(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(
            GameplayKit.GKGoal.goalToFollowPath_maxPredictionTime_forward_, 2
        )
