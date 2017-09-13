from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKState (TestCase):
        def testMethods(self):
            self.assertResultIsBOOL(GameplayKit.GKState.isValidNextState_)


if __name__ == "__main__":
    main()
