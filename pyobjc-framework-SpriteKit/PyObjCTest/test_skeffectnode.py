import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKEffectNode (TestCase):
        @min_os_level("10.9")
        def testMethods(self):
            self.assertArgIsBOOL(SpriteKit.SKEffectNode.setShouldCenterFilter_, 0)
            self.assertResultIsBOOL(SpriteKit.SKEffectNode.shouldCenterFilter)
            self.assertArgIsBOOL(SpriteKit.SKEffectNode.setShouldEnableEffects_, 0)
            self.assertResultIsBOOL(SpriteKit.SKEffectNode.shouldEnableEffects)
            self.assertArgIsBOOL(SpriteKit.SKEffectNode.setShouldRasterize_, 0)
            self.assertResultIsBOOL(SpriteKit.SKEffectNode.shouldRasterize)

if __name__ == "__main__":
    main()
