from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKAction(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SpriteKit.SKUniformType)

    @min_os_level("10.10")
    def testConstants(self):
        self.assertEqual(SpriteKit.SKUniformTypeNone, 0)
        self.assertEqual(SpriteKit.SKUniformTypeFloat, 1)
        self.assertEqual(SpriteKit.SKUniformTypeFloatVector2, 2)
        self.assertEqual(SpriteKit.SKUniformTypeFloatVector3, 3)
        self.assertEqual(SpriteKit.SKUniformTypeFloatVector4, 4)
        self.assertEqual(SpriteKit.SKUniformTypeFloatMatrix2, 5)
        self.assertEqual(SpriteKit.SKUniformTypeFloatMatrix3, 6)
        self.assertEqual(SpriteKit.SKUniformTypeFloatMatrix4, 7)
        self.assertEqual(SpriteKit.SKUniformTypeTexture, 8)
