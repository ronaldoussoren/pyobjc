import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSK3Node (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(SpriteKit.SK3DNode, objc.objc_class)

            self.assertResultIsBOOL(SpriteKit.SK3DNode.isPlaying)
            self.assertArgIsBOOL(SpriteKit.SK3DNode.setPlaying_, 0)

            self.assertResultIsBOOL(SpriteKit.SK3DNode.loops)
            self.assertArgIsBOOL(SpriteKit.SK3DNode.setLoops_, 0)

            self.assertResultIsBOOL(SpriteKit.SK3DNode.autoenablesDefaultLighting)
            self.assertArgIsBOOL(SpriteKit.SK3DNode.setAutoenablesDefaultLighting_, 0)

            node = SpriteKit.SK3DNode.alloc().initWithViewportSize_((100, 200))
            v = node.projectPoint_((10,20,30))
            self.assertIsInstance(v, tuple)
            self.assertEqual(len(v), 3)
            self.assertTrue(all(isinstance(i, float) for i in v))

            v = node.unprojectPoint_((10,20,30))
            self.assertIsInstance(v, tuple)
            self.assertEqual(len(v), 3)
            self.assertTrue(all(isinstance(i, float) for i in v))


if __name__ == "__main__":
    main()
