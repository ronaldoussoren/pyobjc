import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit
    class TestSKShapeNode (TestCase):
        @min_os_level("10.10")
        def testMethods(self):
            self.assertArgIsBOOL(SpriteKit.SKShapeNode.shapeNodeWithPath_centered_, 1)

            self.assertArgIsIn(SpriteKit.SKShapeNode.shapeNodeWithPoints_count_, 0)
            self.assertArgSizeInArg(SpriteKit.SKShapeNode.shapeNodeWithPoints_count_, 0, 1)
            self.assertArgIsIn(SpriteKit.SKShapeNode.shapeNodeWithSplinePoints_count_, 0)
            self.assertArgSizeInArg(SpriteKit.SKShapeNode.shapeNodeWithSplinePoints_count_, 0, 1)

            self.assertArgIsBOOL(SpriteKit.SKShapeNode.setAntialiased_, 0)
            self.assertResultIsBOOL(SpriteKit.SKShapeNode.isAntialiased)

if __name__ == "__main__":
    main()
