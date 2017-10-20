from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKGoal (TestCase):
        def testMethods(self):
            self.assertArgIsBOOL(GameplayKit.GKGoal.goalToFollowPath_maxPredictionTime_forward_, 2)


if __name__ == "__main__":
    main()
