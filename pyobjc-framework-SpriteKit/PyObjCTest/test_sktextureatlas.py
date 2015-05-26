import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKTextureAtlas (TestCase):
        @min_os_level("10.9")
        def testMethods10_9(self):
            self.assertArgIsBlock(SpriteKit.SKTextureAtlas.preloadTextureAtlases_withCompletionHandler_, 1, b'v')
            self.assertArgIsBlock(SpriteKit.SKTextureAtlas.preloadWithCompletionHandler_, 0, b'v')

if __name__ == "__main__":
    main()
