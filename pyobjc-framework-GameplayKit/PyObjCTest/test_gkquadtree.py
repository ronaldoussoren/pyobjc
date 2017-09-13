from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKQuadtree (TestCase):
        def testMethods(self):
            self.assertResultIsBOOL(GameplayKit.GKQuadtree.removeElement_)
            self.assertResultIsBOOL(GameplayKit.GKQuadtree.removeElement_withNode_)


if __name__ == "__main__":
    main()
