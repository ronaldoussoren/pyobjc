from PyObjCTools.TestSupport import TestCase
import GameplayKit


class TestGKState(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKState.isValidNextState_)
