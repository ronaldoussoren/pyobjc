from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKPhysicsBody(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(SpriteKit.SKPhysicsBody.setDynamic_, 0)
        self.assertResultIsBOOL(SpriteKit.SKPhysicsBody.isDynamic)
        self.assertArgIsBOOL(
            SpriteKit.SKPhysicsBody.setUsesPreciseCollisionDetection_, 0
        )
        self.assertResultIsBOOL(SpriteKit.SKPhysicsBody.usesPreciseCollisionDetection)
        self.assertArgIsBOOL(SpriteKit.SKPhysicsBody.setAllowsRotation_, 0)
        self.assertResultIsBOOL(SpriteKit.SKPhysicsBody.allowsRotation)
        self.assertArgIsBOOL(SpriteKit.SKPhysicsBody.setResting_, 0)
        self.assertResultIsBOOL(SpriteKit.SKPhysicsBody.isResting)
        self.assertArgIsBOOL(SpriteKit.SKPhysicsBody.setAffectedByGravity_, 0)
        self.assertResultIsBOOL(SpriteKit.SKPhysicsBody.affectedByGravity)

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertArgIsBOOL(SpriteKit.SKPhysicsBody.setPinned_, 0)
        self.assertResultIsBOOL(SpriteKit.SKPhysicsBody.pinned)
