import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit
    class TestSKNode_NSAccessibility (TestCase):
        @min_os_level("10.12")
        def testMethods(self):
            self.assertResultIsBOOL(SpriteKit.SKNode.isAccessibilityElement)
            self.assertArgIsBOOL(SpriteKit.SKNode.setAccessibilityElement_, 0)

            self.assertResultIsBOOL(SpriteKit.SKNode.isAccessibilityEnabled)
            self.assertArgIsBOOL(SpriteKit.SKNode.setAccessibilityEnabled_, 0)

            self.assertArgHasType(SpriteKit.SKNode.accessibilityHitTest_, 0, SpriteKit.CGPoint.__typestr__)

if __name__ == "__main__":
    main()
