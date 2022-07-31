from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
from objc.simd import vector_float3

import SpriteKit


class TestSK3Node(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertIsInstance(SpriteKit.SK3DNode, objc.objc_class)

        self.assertResultIsBOOL(SpriteKit.SK3DNode.isPlaying)
        self.assertArgIsBOOL(SpriteKit.SK3DNode.setPlaying_, 0)

        self.assertResultIsBOOL(SpriteKit.SK3DNode.loops)
        self.assertArgIsBOOL(SpriteKit.SK3DNode.setLoops_, 0)

        self.assertResultIsBOOL(SpriteKit.SK3DNode.autoenablesDefaultLighting)
        self.assertArgIsBOOL(SpriteKit.SK3DNode.setAutoenablesDefaultLighting_, 0)

        self.assertResultHasType(
            SpriteKit.SK3DNode.projectPoint_, vector_float3.__typestr__
        )
        self.assertArgHasType(
            SpriteKit.SK3DNode.projectPoint_, 0, vector_float3.__typestr__
        )

        self.assertResultHasType(
            SpriteKit.SK3DNode.unprojectPoint_, vector_float3.__typestr__
        )
        self.assertArgHasType(
            SpriteKit.SK3DNode.unprojectPoint_, 0, vector_float3.__typestr__
        )

        node = SpriteKit.SK3DNode.alloc().initWithViewportSize_((100, 200))
        v = node.projectPoint_((10, 20, 30))
        self.assertIsInstance(v, vector_float3)

        v = node.unprojectPoint_((10, 20, 30))
        self.assertIsInstance(v, vector_float3)
