import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSK3Node (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(SpriteKit.SK3DNode, objc.objc_class)

            self.assertResultHasType(SpriteKit.SK3DNode.projectPoint_, objc._C_VECTOR_FLOAT3)
            self.assertArgHasType(SpriteKit.SK3DNode.projectPoint_, 0, objc._C_VECTOR_FLOAT3)

            self.assertResultHasType(SpriteKit.SK3DNode.unprojectPoint_, objc._C_VECTOR_FLOAT3)
            self.assertArgHasType(SpriteKit.SK3DNode.unprojectPoint_, 0, objc._C_VECTOR_FLOAT3)

            self.assertResultIsBOOL(SpriteKit.SK3DNode.isPlaying)
            self.assertArgIsBOOL(SpriteKit.SK3DNode.setPlaying_)

            self.assertResultIsBOOL(SpriteKit.SK3DNode.loops)
            self.assertArgIsBOOL(SpriteKit.SK3DNode.setLoops_)

            self.assertResultIsBOOL(SpriteKit.SK3DNode.autoenablesDefaultLighting)
            self.assertArgIsBOOL(SpriteKit.SK3DNode.setAutoenablesDefaultLighting_)

if __name__ == "__main__":
    main()
