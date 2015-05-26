import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKFieldNode (TestCase):

        @min_os_level("10.10")
        def testMethods(self):
            self.assertArgIsBOOL(SpriteKit.SKFieldNode.setEnabled_, 0)
            self.assertResultIsBOOL(SpriteKit.SKFieldNode.isEnabled)
            self.assertArgIsBOOL(SpriteKit.SKFieldNode.setExclusive_, 0)
            self.assertResultIsBOOL(SpriteKit.SKFieldNode.isExclusive)

            self.assertArgHasType(SpriteKit.SKFieldNode.linearGravityFieldWithVector_, 0, objc._C_VECTOR_FLOAT3)
            self.assertArgHasType(SpriteKit.SKFieldNode.velocityFieldWithVector_, 0, objc._C_VECTOR_FLOAT3)

            self.assertArgIsBlock(SpriteKit.SKFieldNode.customFieldWithEvaluationBlock_, 0,
                    objc._C_VECTOR_FLOAT3 + objc._C_VECTOR_FLOAT3 + objc._C_FLOAT_VECTOR3 + objc._C_FLT + objc._C_FLT + objc._C_DBL)


            self.assertArgHasType(SpriteKit.SKFieldNode.setDirection_, 0, objc._C_VECTOR_FLOAT3)
            self.assertResultHasType(SpriteKit.SKFieldNode.direction, objc._C_VECTOR_FLOAT3)

if __name__ == "__main__":
    main()
