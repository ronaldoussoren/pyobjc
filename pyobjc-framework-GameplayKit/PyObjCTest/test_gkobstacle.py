from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import GameplayKit

    class TestGKObstacle (TestCase):
        def testMethods(self):
            # SIMD:
            #self.assertArgIsIn(GameplayKit.GKPolygonObstacle.obstacleWithPoints_count_, 0)
            #self.assertArgSizeInArg(GameplayKit.GKPolygonObstacle.obstacleWithPoints_count_, 0, 1)

            #self.assertArgIsIn(GameplayKit.GKPolygonObstacle.initWithPoints_count_, 0)
            #self.assertArgSizeInArg(GameplayKit.GKPolygonObstacle.initWithPoints_count_, 0, 1)

            pass


if __name__ == "__main__":
    main()
