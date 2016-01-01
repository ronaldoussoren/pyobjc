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

            obj = SpriteKit.SKFieldNode.linearGravityFieldWithVector_((1,2,3))
            self.assertIsInstance(obj, SpriteKit.SKFieldNode)
            self.assertEqual(obj.direction(), (1,2,3))

            obj = SpriteKit.SKFieldNode.velocityFieldWithVector_((1,2,3))
            self.assertIsInstance(obj, SpriteKit.SKFieldNode)
            self.assertEqual(obj.direction(), (1,2,3))

            # FIXME
            #self.assertArgIsBlock(SpriteKit.SKFieldNode.customFieldWithEvaluationBlock_, 0,
            #        objc._C_VECTOR_FLOAT3 + objc._C_VECTOR_FLOAT3 + objc._C_FLOAT_VECTOR3 + objc._C_FLT + objc._C_FLT + objc._C_DBL)

            obj.setDirection_((9,10,11))
            self.assertEqual(obj.direction(), (9,10,11))

if __name__ == "__main__":
    main()
