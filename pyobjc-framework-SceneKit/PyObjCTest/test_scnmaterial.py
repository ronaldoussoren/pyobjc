from PyObjCTools.TestSupport import TestCase, min_os_level

import SceneKit


class TestSCNMaterial(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(SceneKit.SCNLightingModel, str)

    def test_enum_types(self):
        self.assertIsEnumType(SceneKit.SCNBlendMode)
        self.assertIsEnumType(SceneKit.SCNCullMode)
        self.assertIsEnumType(SceneKit.SCNFillMode)
        self.assertIsEnumType(SceneKit.SCNTransparencyMode)

    def testConstants(self):
        self.assertIsInstance(SceneKit.SCNLightingModelPhong, str)
        self.assertIsInstance(SceneKit.SCNLightingModelBlinn, str)
        self.assertIsInstance(SceneKit.SCNLightingModelLambert, str)
        self.assertIsInstance(SceneKit.SCNLightingModelConstant, str)

        self.assertEqual(SceneKit.SCNFillModeFill, 0)
        self.assertEqual(SceneKit.SCNFillModeLines, 1)

        self.assertEqual(SceneKit.SCNCullBack, 0)
        self.assertEqual(SceneKit.SCNCullFront, 1)

        self.assertEqual(SceneKit.SCNTransparencyModeAOne, 0)
        self.assertEqual(SceneKit.SCNTransparencyModeRGBZero, 1)
        self.assertEqual(SceneKit.SCNTransparencyModeSingleLayer, 2)
        self.assertEqual(SceneKit.SCNTransparencyModeDualLayer, 3)
        self.assertEqual(
            SceneKit.SCNTransparencyModeDefault, SceneKit.SCNTransparencyModeAOne
        )

        self.assertEqual(SceneKit.SCNBlendModeAlpha, 0)
        self.assertEqual(SceneKit.SCNBlendModeAdd, 1)
        self.assertEqual(SceneKit.SCNBlendModeSubtract, 2)
        self.assertEqual(SceneKit.SCNBlendModeMultiply, 3)
        self.assertEqual(SceneKit.SCNBlendModeScreen, 4)
        self.assertEqual(SceneKit.SCNBlendModeReplace, 5)
        self.assertEqual(SceneKit.SCNBlendModeMax, 6)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(SceneKit.SCNLightingModelPhysicallyBased, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(SceneKit.SCNLightingModelShadowOnly, str)

    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNMaterial.isLitPerPixel)
        self.assertArgIsBOOL(SceneKit.SCNMaterial.setLitPerPixel_, 0)

        self.assertResultIsBOOL(SceneKit.SCNMaterial.isDoubleSided)
        self.assertArgIsBOOL(SceneKit.SCNMaterial.setDoubleSided_, 0)

        self.assertResultIsBOOL(SceneKit.SCNMaterial.locksAmbientWithDiffuse)
        self.assertArgIsBOOL(SceneKit.SCNMaterial.setLocksAmbientWithDiffuse_, 0)

        self.assertResultIsBOOL(SceneKit.SCNMaterial.writesToDepthBuffer)
        self.assertArgIsBOOL(SceneKit.SCNMaterial.setWritesToDepthBuffer_, 0)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(SceneKit.SCNMaterial.readsFromDepthBuffer)
        self.assertArgIsBOOL(SceneKit.SCNMaterial.setReadsFromDepthBuffer_, 0)
