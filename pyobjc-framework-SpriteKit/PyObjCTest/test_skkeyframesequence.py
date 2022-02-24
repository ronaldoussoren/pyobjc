from PyObjCTools.TestSupport import TestCase

import SpriteKit


class TestSKKeyframeSequence(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SpriteKit.SKInterpolationMode)
        self.assertIsEnumType(SpriteKit.SKRepeatMode)

    def testConstants(self):
        self.assertEqual(SpriteKit.SKInterpolationModeLinear, 1)
        self.assertEqual(SpriteKit.SKInterpolationModeSpline, 2)
        self.assertEqual(SpriteKit.SKInterpolationModeStep, 3)

        self.assertEqual(SpriteKit.SKRepeatModeClamp, 1)
        self.assertEqual(SpriteKit.SKRepeatModeLoop, 2)
