from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import SpriteKit


class TestSKScene(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SpriteKit.SKSceneScaleMode)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(SpriteKit.SKSceneScaleModeFill, 0)
        self.assertEqual(SpriteKit.SKSceneScaleModeAspectFill, 1)
        self.assertEqual(SpriteKit.SKSceneScaleModeAspectFit, 2)
        self.assertEqual(SpriteKit.SKSceneScaleModeResizeFill, 3)

    @min_os_level("10.10")
    def testProtocols(self):
        objc.protocolNamed("SKSceneDelegate")
