import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSKKeyframeSequence (TestCase):
        @min_os_level('10.9')
        def testConstants(self):
            self.assertEqual(SpriteKit.SKLabelVerticalAlignmentModeBaseline, 0)
            self.assertEqual(SpriteKit.SKLabelVerticalAlignmentModeCenter, 1)
            self.assertEqual(SpriteKit.SKLabelVerticalAlignmentModeTop, 2)
            self.assertEqual(SpriteKit.SKLabelVerticalAlignmentModeBottom, 3)

            self.assertEqual(SpriteKit.SKLabelHorizontalAlignmentModeCenter, 0)
            self.assertEqual(SpriteKit.SKLabelHorizontalAlignmentModeLeft, 1)
            self.assertEqual(SpriteKit.SKLabelHorizontalAlignmentModeRight, 2)


if __name__ == "__main__":
    main()
