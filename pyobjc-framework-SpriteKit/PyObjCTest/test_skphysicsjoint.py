import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKPhysicsJoint (TestCase):
        @min_os_level("10.9")
        def testMethods(self):
            self.assertArgIsBOOL(SpriteKit.SKPhysicsJointPin.setShouldEnableLimits_, 0)
            self.assertResultIsBOOL(SpriteKit.SKPhysicsJointPin.shouldEnableLimits)

            self.assertArgIsBOOL(SpriteKit.SKPhysicsJointSliding.setShouldEnableLimits_, 0)
            self.assertResultIsBOOL(SpriteKit.SKPhysicsJointSliding.shouldEnableLimits)

if __name__ == "__main__":
    main()
