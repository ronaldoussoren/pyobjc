from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKKeyframeSequence(TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(SpriteKit.SKInterpolationModeLinear, 1)
        self.assertEqual(SpriteKit.SKInterpolationModeSpline, 2)
        self.assertEqual(SpriteKit.SKInterpolationModeStep, 3)

        self.assertEqual(SpriteKit.SKRepeatModeClamp, 1)
        self.assertEqual(SpriteKit.SKRepeatModeLoop, 2)
