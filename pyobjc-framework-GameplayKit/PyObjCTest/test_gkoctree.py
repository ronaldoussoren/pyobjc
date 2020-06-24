from PyObjCTools.TestSupport import TestCase
import GameplayKit


class TestGKOctree(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKOctree.removeElement_)
        self.assertResultIsBOOL(GameplayKit.GKOctree.removeElement_withNode_)
