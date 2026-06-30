from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKTileDefinition(TestCase):
    def test_enums(self):
        self.assertIsEnumType(SpriteKit.SKTileDefinitionRotation)
        self.assertEqual(SpriteKit.SKTileDefinitionRotation0, 0)
        self.assertEqual(SpriteKit.SKTileDefinitionRotation90, 1)
        self.assertEqual(SpriteKit.SKTileDefinitionRotation180, 2)
        self.assertEqual(SpriteKit.SKTileDefinitionRotation270, 3)

    @min_os_level("10.12")
    def test_methods(self):
        self.assertResultIsBOOL(SpriteKit.SKTileDefinition.flipVertically)
        self.assertArgIsBOOL(SpriteKit.SKTileDefinition.setFlipVertically_, 0)

        self.assertResultIsBOOL(SpriteKit.SKTileDefinition.flipHorizontally)
        self.assertArgIsBOOL(SpriteKit.SKTileDefinition.setFlipHorizontally_, 0)
