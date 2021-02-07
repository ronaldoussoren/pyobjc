from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKNode_NSAccessibility(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(SpriteKit.SKNode.isAccessibilityElement)
        self.assertArgIsBOOL(SpriteKit.SKNode.setAccessibilityElement_, 0)

        self.assertResultIsBOOL(SpriteKit.SKNode.isAccessibilityEnabled)
        self.assertArgIsBOOL(SpriteKit.SKNode.setAccessibilityEnabled_, 0)

        self.assertArgHasType(
            SpriteKit.SKNode.accessibilityHitTest_, 0, SpriteKit.CGPoint.__typestr__
        )
