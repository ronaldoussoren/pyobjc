from PyObjCTools.TestSupport import TestCase
import GameplayKit


class TestGKStateMachine(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(GameplayKit.GKStateMachine.canEnterState_)
        self.assertResultIsBOOL(GameplayKit.GKStateMachine.enterState_)
