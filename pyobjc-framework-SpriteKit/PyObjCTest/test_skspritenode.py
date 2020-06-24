from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKSpriteNode(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertArgIsBOOL(
            SpriteKit.SKSpriteNode.spriteNodeWithImageNamed_normalMapped_, 1
        )
