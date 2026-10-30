from PyObjCTools.TestSupport import TestCase

import SpriteKit


class TestSKPhysicsJoint(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(SpriteKit.SKPhysicsJointPin.setShouldEnableLimits_, 0)
        self.assertResultIsBOOL(SpriteKit.SKPhysicsJointPin.shouldEnableLimits)

        self.assertArgIsBOOL(SpriteKit.SKPhysicsJointSliding.setShouldEnableLimits_, 0)
        self.assertResultIsBOOL(SpriteKit.SKPhysicsJointSliding.shouldEnableLimits)
