from PyObjCTools.TestSupport import TestCase
import GameplayKit


class TestGKState(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(GameplayKit.GKState.isValidNextState_)
