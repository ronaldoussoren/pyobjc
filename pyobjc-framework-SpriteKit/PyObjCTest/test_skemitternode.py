from PyObjCTools.TestSupport import TestCase

import SpriteKit


class TestSKEmitterNode(TestCase):
    def test_enums(self):
        self.assertIsEnumType(SpriteKit.SKParticleRenderOrder)
        self.assertEqual(SpriteKit.SKParticleRenderOrderOldestLast, 0)
        self.assertEqual(SpriteKit.SKParticleRenderOrderOldestFirst, 1)
        self.assertEqual(SpriteKit.SKParticleRenderOrderDontCare, 2)
