from PyObjCTools.TestSupport import TestCase
import GameplayKit


class TestGKStateMachine(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKStateMachine.canEnterState_)
        self.assertResultIsBOOL(GameplayKit.GKStateMachine.enterState_)
