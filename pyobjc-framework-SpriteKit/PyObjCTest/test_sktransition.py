from PyObjCTools.TestSupport import TestCase

import SpriteKit


class TestSKTransition(TestCase):
    def test_enums(self):
        self.assertIsEnumType(SpriteKit.SKTransitionDirection)
        self.assertEqual(SpriteKit.SKTransitionDirectionUp, 0)
        self.assertEqual(SpriteKit.SKTransitionDirectionDown, 1)
        self.assertEqual(SpriteKit.SKTransitionDirectionRight, 2)
        self.assertEqual(SpriteKit.SKTransitionDirectionLeft, 3)

    def test_methods(self):
        self.assertArgIsBOOL(SpriteKit.SKTransition.setPausesIncomingScene_, 0)
        self.assertResultIsBOOL(SpriteKit.SKTransition.pausesIncomingScene)
        self.assertArgIsBOOL(SpriteKit.SKTransition.setPausesOutgoingScene_, 0)
        self.assertResultIsBOOL(SpriteKit.SKTransition.pausesOutgoingScene)
