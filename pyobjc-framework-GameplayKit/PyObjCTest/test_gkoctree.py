from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKOctree (TestCase):
        def testMethods(self):
            self.assertResultIsBOOL(GameplayKit.GKOctree.removeElement_)
            self.assertResultIsBOOL(GameplayKit.GKOctree.removeElement_withNode_)


if __name__ == "__main__":
    main()
