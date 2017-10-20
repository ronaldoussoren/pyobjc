from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKPrimitives (TestCase):
        def testStructs(self):
            # SIMD:
            #v = GameKit.GKBox()
            #self.assertIsInstance(v.boxMin, ...)
            #self.assertIsInstance(v.boxMax, ...)

            #v = GameKit.GKQuad()
            #self.assertIsInstance(v.quadMin, ...)
            #self.assertIsInstance(v.quadMax, ...)

            #v = GameKit.GKTriangle()
            #self.assertIsInstance(v.points, ...)
            pass


        def testMethods(self):
            self.assertResultIsBOOL(GameplayKit.GKAgent3D.rightHanded)
            self.assertArgIsBOOL(GameplayKit.GKAgent3D.setRightHanded_, 0)


if __name__ == "__main__":
    main()
