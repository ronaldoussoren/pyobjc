import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKView (TestCase):
        @min_os_level("10.9")
        def testMethods10_9(self):
            self.assertArgIsBOOL(SpriteKit.SKView.setPaused_, 0)
            self.assertResultIsBOOL(SpriteKit.SKView.isPaused)
            self.assertArgIsBOOL(SpriteKit.SKView.setShowsFPS_, 0)
            self.assertResultIsBOOL(SpriteKit.SKView.showsFPS)
            self.assertArgIsBOOL(SpriteKit.SKView.setShowsDrawCount_, 0)
            self.assertResultIsBOOL(SpriteKit.SKView.showsDrawCount)
            self.assertArgIsBOOL(SpriteKit.SKView.setShowsNodeCount_, 0)
            self.assertResultIsBOOL(SpriteKit.SKView.showsNodeCount)
            self.assertArgIsBOOL(SpriteKit.SKView.setShowsQuadCount_, 0)
            self.assertResultIsBOOL(SpriteKit.SKView.showsQuadCount)
            self.assertArgIsBOOL(SpriteKit.SKView.setShowsPhysics_, 0)
            self.assertResultIsBOOL(SpriteKit.SKView.showsPhysics)
            self.assertArgIsBOOL(SpriteKit.SKView.setShowsFields_, 0)
            self.assertResultIsBOOL(SpriteKit.SKView.showsFields)
            self.assertArgIsBOOL(SpriteKit.SKView.setAsynchronous_, 0)
            self.assertResultIsBOOL(SpriteKit.SKView.isAsynchronous)
            self.assertArgIsBOOL(SpriteKit.SKView.setIgnoresSiblingOrder_, 0)
            self.assertResultIsBOOL(SpriteKit.SKView.ignoresSiblingOrder)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBOOL(SpriteKit.SKView.setAllowsTransparency_, 0)
            self.assertResultIsBOOL(SpriteKit.SKView.allowsTransparency)
            self.assertArgIsBOOL(SpriteKit.SKView.setShouldCullNonVisibleNodes_, 0)
            self.assertResultIsBOOL(SpriteKit.SKView.shouldCullNonVisibleNodes)

if __name__ == "__main__":
    main()
