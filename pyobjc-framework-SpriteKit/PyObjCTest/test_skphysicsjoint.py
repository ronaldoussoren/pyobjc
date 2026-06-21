from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKPhysicsJoint(TestCase):
    @min_os_level("10.9")
    def test_methods(self):
        self.assertArgIsBOOL(SpriteKit.SKPhysicsJointPin.setShouldEnableLimits_, 0)
        self.assertResultIsBOOL(SpriteKit.SKPhysicsJointPin.shouldEnableLimits)

        self.assertArgIsBOOL(SpriteKit.SKPhysicsJointSliding.setShouldEnableLimits_, 0)
        self.assertResultIsBOOL(SpriteKit.SKPhysicsJointSliding.shouldEnableLimits)
