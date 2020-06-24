from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKLightNode(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertArgIsBOOL(SpriteKit.SKLightNode.setEnabled_, 0)
        self.assertResultIsBOOL(SpriteKit.SKLightNode.isEnabled)
