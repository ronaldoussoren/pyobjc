from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKTransition(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SpriteKit.SKTransitionDirection)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(SpriteKit.SKTransitionDirectionUp, 0)
        self.assertEqual(SpriteKit.SKTransitionDirectionDown, 1)
        self.assertEqual(SpriteKit.SKTransitionDirectionRight, 2)
        self.assertEqual(SpriteKit.SKTransitionDirectionLeft, 3)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertArgIsBOOL(SpriteKit.SKTransition.setPausesIncomingScene_, 0)
        self.assertResultIsBOOL(SpriteKit.SKTransition.pausesIncomingScene)
        self.assertArgIsBOOL(SpriteKit.SKTransition.setPausesOutgoingScene_, 0)
        self.assertResultIsBOOL(SpriteKit.SKTransition.pausesOutgoingScene)
