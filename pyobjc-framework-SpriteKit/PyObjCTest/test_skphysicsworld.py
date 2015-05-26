import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit
    import Quartz

    class TestSKPhysicsWorld (TestCase):
        @min_os_level("10.9")
        def testMethods(self):
            self.assertArgIsBlock(SpriteKit.SKPhysicsWorld.enumerateBodiesAtPoint_usingBlock_, 1,
                    b'v@o^Z')
            self.assertArgIsBlock(SpriteKit.SKPhysicsWorld.enumerateBodiesInRect_usingBlock_, 1,
                    b'v@o^Z')
            self.assertArgIsBlock(SpriteKit.SKPhysicsWorld.enumerateBodiesAlongRayStart_end_usingBlock_, 2,
                    b'v@' + Quartz.CGPoint.__typestr__ + Quartz.CGVector.__typestr__ + b'o^Z')

            self.assertArgHasType(SpriteKit.SKPhysicsWorld.sampleFieldsAt_, 0, objc._C_VECTOR_FLOAT3)
            self.assertResultHasType(SpriteKit.SKPhysicsWorld.sampleFieldsAt_, objc._C_VECTOR_FLOAT3)

        @min_os_level('10.10')
        def testProtocols(self):
            objc.protocolNamed('SKPhysicsContactDelegate')


if __name__ == "__main__":
    main()
