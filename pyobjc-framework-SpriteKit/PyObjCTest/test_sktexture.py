import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKTexture (TestCase):
        @min_os_level('10.9')
        def testConstants(self):
            self.assertEqual(SpriteKit.SKTextureFilteringNearest, 0)
            self.assertEqual(SpriteKit.SKTextureFilteringLinear, 1)

        @min_os_level("10.9")
        def testMethods10_9(self):
            self.assertArgIsBOOL(SpriteKit.SKTexture.setUsesMipmaps_, 0)
            self.assertResultIsBOOL(SpriteKit.SKTexture.usesMipmaps)

            self.assertArgIsBlock(SpriteKit.SKTexture.preloadTextures_withCompletionHandler_, 1, b'v')
            self.assertArgIsBlock(SpriteKit.SKTexture.preloadWithCompletionHandler_, 0, b'v')

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBOOL(SpriteKit.SKTexture.textureWithData_size_flipped_, 2)
            self.assertArgIsBOOL(SpriteKit.SKTexture.textureNoiseWithSmoothness_size_grayscale_, 2)

if __name__ == "__main__":
    main()
