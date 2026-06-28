from PyObjCTools.TestSupport import TestCase

import SpriteKit


class TestSKKeyframeSequence(TestCase):
    def test_enums(self):
        self.assertIsEnumType(SpriteKit.SKLabelVerticalAlignmentMode)
        self.assertEqual(SpriteKit.SKLabelVerticalAlignmentModeBaseline, 0)
        self.assertEqual(SpriteKit.SKLabelVerticalAlignmentModeCenter, 1)
        self.assertEqual(SpriteKit.SKLabelVerticalAlignmentModeTop, 2)
        self.assertEqual(SpriteKit.SKLabelVerticalAlignmentModeBottom, 3)

        self.assertIsEnumType(SpriteKit.SKLabelHorizontalAlignmentMode)
        self.assertEqual(SpriteKit.SKLabelHorizontalAlignmentModeCenter, 0)
        self.assertEqual(SpriteKit.SKLabelHorizontalAlignmentModeLeft, 1)
        self.assertEqual(SpriteKit.SKLabelHorizontalAlignmentModeRight, 2)
