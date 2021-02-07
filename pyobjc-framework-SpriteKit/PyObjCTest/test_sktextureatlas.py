from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKTextureAtlas(TestCase):
    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBlock(
            SpriteKit.SKTextureAtlas.preloadTextureAtlases_withCompletionHandler_,
            1,
            b"v",
        )
        self.assertArgIsBlock(
            SpriteKit.SKTextureAtlas.preloadWithCompletionHandler_, 0, b"v"
        )
