from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKTileDefinition(TestCase):
    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(SpriteKit.SKTileDefinitionRotation0, 0)
        self.assertEqual(SpriteKit.SKTileDefinitionRotation90, 1)
        self.assertEqual(SpriteKit.SKTileDefinitionRotation180, 2)
        self.assertEqual(SpriteKit.SKTileDefinitionRotation270, 3)

    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(SpriteKit.SKTileDefinition.flipVertically)
        self.assertArgIsBOOL(SpriteKit.SKTileDefinition.setFlipVertically_, 0)

        self.assertResultIsBOOL(SpriteKit.SKTileDefinition.flipHorizontally)
        self.assertArgIsBOOL(SpriteKit.SKTileDefinition.setFlipHorizontally_, 0)
