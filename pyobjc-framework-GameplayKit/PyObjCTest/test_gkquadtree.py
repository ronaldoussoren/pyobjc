from PyObjCTools.TestSupport import TestCase

import GameplayKit


class TestGKQuadtree(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKQuadtree.removeElement_)
        self.assertResultIsBOOL(GameplayKit.GKQuadtree.removeElement_withNode_)
