from PyObjCTools.TestSupport import TestCase

import SpriteKit


class TestSKEffectNode(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(SpriteKit.SKEffectNode.setShouldCenterFilter_, 0)
        self.assertResultIsBOOL(SpriteKit.SKEffectNode.shouldCenterFilter)
        self.assertArgIsBOOL(SpriteKit.SKEffectNode.setShouldEnableEffects_, 0)
        self.assertResultIsBOOL(SpriteKit.SKEffectNode.shouldEnableEffects)
        self.assertArgIsBOOL(SpriteKit.SKEffectNode.setShouldRasterize_, 0)
        self.assertResultIsBOOL(SpriteKit.SKEffectNode.shouldRasterize)
