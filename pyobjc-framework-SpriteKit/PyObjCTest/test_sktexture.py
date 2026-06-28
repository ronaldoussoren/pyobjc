from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKTexture(TestCase):
    def test_enums(self):
        self.assertIsEnumType(SpriteKit.SKTextureFilteringMode)
        self.assertEqual(SpriteKit.SKTextureFilteringNearest, 0)
        self.assertEqual(SpriteKit.SKTextureFilteringLinear, 1)

    def test_methods(self):
        self.assertArgIsBOOL(SpriteKit.SKTexture.setUsesMipmaps_, 0)
        self.assertResultIsBOOL(SpriteKit.SKTexture.usesMipmaps)

        self.assertArgIsBlock(
            SpriteKit.SKTexture.preloadTextures_withCompletionHandler_, 1, b"v"
        )
        self.assertArgIsBlock(
            SpriteKit.SKTexture.preloadWithCompletionHandler_, 0, b"v"
        )

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertArgIsBOOL(SpriteKit.SKTexture.textureWithData_size_flipped_, 2)
        self.assertArgIsBOOL(
            SpriteKit.SKTexture.textureNoiseWithSmoothness_size_grayscale_, 2
        )
