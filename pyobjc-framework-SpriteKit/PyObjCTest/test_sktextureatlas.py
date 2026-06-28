from PyObjCTools.TestSupport import TestCase

import SpriteKit


class TestSKTextureAtlas(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            SpriteKit.SKTextureAtlas.preloadTextureAtlases_withCompletionHandler_,
            1,
            b"v",
        )
        self.assertArgIsBlock(
            SpriteKit.SKTextureAtlas.preloadWithCompletionHandler_, 0, b"v"
        )
