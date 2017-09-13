from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKStateMachine (TestCase):
        def testMethods(self):
            self.assertResultIsBOOL(GameplayKit.GKStateMachine.canEnterState_)
            self.assertResultIsBOOL(GameplayKit.GKStateMachine.enterState_)


if __name__ == "__main__":
    main()
