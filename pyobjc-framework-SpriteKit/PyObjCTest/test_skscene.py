from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKScene(TestCase):
    def test_enums(self):
        self.assertIsEnumType(SpriteKit.SKSceneScaleMode)
        self.assertEqual(SpriteKit.SKSceneScaleModeFill, 0)
        self.assertEqual(SpriteKit.SKSceneScaleModeAspectFill, 1)
        self.assertEqual(SpriteKit.SKSceneScaleModeAspectFit, 2)
        self.assertEqual(SpriteKit.SKSceneScaleModeResizeFill, 3)

    @min_os_level("10.10")
    def test_protocols(self):
        self.assertProtocolExists("SKSceneDelegate", SpriteKit)
