from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKRenderer(TestCase):
    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(SpriteKit.SKRenderer.ignoresSiblingOrder)
        self.assertArgIsBOOL(SpriteKit.SKRenderer.setIgnoresSiblingOrder_, 0)

        self.assertResultIsBOOL(SpriteKit.SKRenderer.shouldCullNonVisibleNodes)
        self.assertArgIsBOOL(SpriteKit.SKRenderer.setShouldCullNonVisibleNodes_, 0)

        self.assertResultIsBOOL(SpriteKit.SKRenderer.showsDrawCount)
        self.assertArgIsBOOL(SpriteKit.SKRenderer.setShowsDrawCount_, 0)

        self.assertResultIsBOOL(SpriteKit.SKRenderer.showsNodeCount)
        self.assertArgIsBOOL(SpriteKit.SKRenderer.setShowsNodeCount_, 0)

        self.assertResultIsBOOL(SpriteKit.SKRenderer.showsQuadCount)
        self.assertArgIsBOOL(SpriteKit.SKRenderer.setShowsQuadCount_, 0)

        self.assertResultIsBOOL(SpriteKit.SKRenderer.showsPhysics)
        self.assertArgIsBOOL(SpriteKit.SKRenderer.setShowsPhysics_, 0)

        self.assertResultIsBOOL(SpriteKit.SKRenderer.showsFields)
        self.assertArgIsBOOL(SpriteKit.SKRenderer.setShowsFields_, 0)
