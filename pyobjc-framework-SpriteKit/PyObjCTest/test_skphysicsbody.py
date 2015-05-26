import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKPhysicsBody (TestCase):
        @min_os_level("10.9")
        def testMethods(self):
            self.assertIsInstance(SpriteKit.SKPhysicsBody, objc.objc_class)

            self.assertArgIsBOOL(SpriteKit.SKPhysicsBody.setDynamic_, 0)
            self.assertResultIsBOOL(SpriteKit.SKPhysicsBody.isDynamic)
            self.assertArgIsBOOL(SpriteKit.SKPhysicsBody.setUsesPreciseCollisionDetection_, 0)
            self.assertResultIsBOOL(SpriteKit.SKPhysicsBody.usesPreciseCollisionDetection)
            self.assertArgIsBOOL(SpriteKit.SKPhysicsBody.setAllowsRotation_, 0)
            self.assertResultIsBOOL(SpriteKit.SKPhysicsBody.allowsRotation)
            self.assertArgIsBOOL(SpriteKit.SKPhysicsBody.setResting_, 0)
            self.assertResultIsBOOL(SpriteKit.SKPhysicsBody.isResting)
            self.assertArgIsBOOL(SpriteKit.SKPhysicsBody.setAffectedByGravity_, 0)
            self.assertResultIsBOOL(SpriteKit.SKPhysicsBody.affectedByGravity)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBOOL(SpriteKit.SKPhysicsBody.setPinned_, 0)
            self.assertResultIsBOOL(SpriteKit.SKPhysicsBody.pinned)

if __name__ == "__main__":
    main()
