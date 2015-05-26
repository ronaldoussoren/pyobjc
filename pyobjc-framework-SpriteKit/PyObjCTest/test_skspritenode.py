import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKSpriteNode (TestCase):
        @min_os_level("10.10")
        def testMethods(self):
            self.assertArgIsBOOL(SpriteKit.SKSpriteNode.spriteNodeWithImageNamed_normalMapped_, 1)

if __name__ == "__main__":
    main()
