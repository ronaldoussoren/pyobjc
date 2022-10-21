from PyObjCTools.TestSupport import TestCase

import GameplayKit


class TestGKPrimitives(TestCase):
    def testStructs(self):
        self.assertEqual(GameplayKit.GKBox.__typestr__, b"{GKBox=<3f><3f>}")
        v = GameplayKit.GKBox()
        self.assertIs(v.boxMin, None)
        self.assertIs(v.boxMax, None)

        self.assertEqual(GameplayKit.GKQuad.__typestr__, b"{GKQuad=<2f><2f>}")
        v = GameplayKit.GKQuad()
        self.assertIs(v.quadMin, None)
        self.assertIs(v.quadMax, None)

        self.assertEqual(GameplayKit.GKTriangle.__typestr__, b"{GKTriangle=[3<3f>]}")
        v = GameplayKit.GKTriangle()
        self.assertIs(v.points, None)
