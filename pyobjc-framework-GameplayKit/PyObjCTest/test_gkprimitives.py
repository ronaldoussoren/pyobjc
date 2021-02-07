from PyObjCTools.TestSupport import TestCase

import GameplayKit


class TestGKPrimitives(TestCase):
    def testStructs(self):
        # SIMD:
        # v = GameKit.GKBox()
        # self.assertIsInstance(v.boxMin, ...)
        # self.assertIsInstance(v.boxMax, ...)

        # v = GameKit.GKQuad()
        # self.assertIsInstance(v.quadMin, ...)
        # self.assertIsInstance(v.quadMax, ...)

        # v = GameKit.GKTriangle()
        # self.assertIsInstance(v.points, ...)
        pass

    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKAgent3D.rightHanded)
        self.assertArgIsBOOL(GameplayKit.GKAgent3D.setRightHanded_, 0)
