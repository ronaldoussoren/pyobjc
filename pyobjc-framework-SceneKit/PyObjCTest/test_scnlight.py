from PyObjCTools.TestSupport import TestCase, min_os_level


import SceneKit


class TestSCNLight(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(SceneKit.SCNLightType, str)

    def test_enum_types(self):
        self.assertIsEnumType(SceneKit.SCNLightAreaType)
        self.assertIsEnumType(SceneKit.SCNLightProbeType)
        self.assertIsEnumType(SceneKit.SCNLightProbeUpdateType)
        self.assertIsEnumType(SceneKit.SCNShadowMode)

    @min_os_level("10.8")
    def testConstants(self):
        self.assertIsInstance(SceneKit.SCNLightTypeAmbient, str)
        self.assertIsInstance(SceneKit.SCNLightTypeOmni, str)
        self.assertIsInstance(SceneKit.SCNLightTypeDirectional, str)
        self.assertIsInstance(SceneKit.SCNLightTypeSpot, str)

        self.assertEqual(SceneKit.SCNShadowModeForward, 0)
        self.assertEqual(SceneKit.SCNShadowModeDeferred, 1)
        self.assertEqual(SceneKit.SCNShadowModeModulated, 2)

        self.assertIsInstance(SceneKit.SCNLightAttenuationStartKey, str)
        self.assertIsInstance(SceneKit.SCNLightAttenuationEndKey, str)
        self.assertIsInstance(SceneKit.SCNLightAttenuationFalloffExponentKey, str)
        self.assertIsInstance(SceneKit.SCNLightSpotInnerAngleKey, str)
        self.assertIsInstance(SceneKit.SCNLightSpotOuterAngleKey, str)
        self.assertIsInstance(SceneKit.SCNLightShadowNearClippingKey, str)
        self.assertIsInstance(SceneKit.SCNLightShadowFarClippingKey, str)

        self.assertEqual(SceneKit.SCNLightProbeTypeIrradiance, 0)
        self.assertEqual(SceneKit.SCNLightProbeTypeRadiance, 1)

        self.assertEqual(SceneKit.SCNLightProbeUpdateTypeNever, 0)
        self.assertEqual(SceneKit.SCNLightProbeUpdateTypeRealtime, 1)

        self.assertEqual(SceneKit.SCNLightAreaTypeRectangle, 1)
        self.assertEqual(SceneKit.SCNLightAreaTypePolygon, 4)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(SceneKit.SCNLightTypeIES, str)
        self.assertIsInstance(SceneKit.SCNLightTypeProbe, str)

    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNLight.castsShadow)
        self.assertArgIsBOOL(SceneKit.SCNLight.setCastsShadow_, 0)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(SceneKit.SCNLight.automaticallyAdjustsShadowProjection)
        self.assertArgIsBOOL(
            SceneKit.SCNLight.setAutomaticallyAdjustsShadowProjection_, 0
        )

        self.assertResultIsBOOL(SceneKit.SCNLight.forcesBackFaceCasters)
        self.assertArgIsBOOL(SceneKit.SCNLight.setForcesBackFaceCasters_, 0)

        self.assertResultIsBOOL(SceneKit.SCNLight.sampleDistributedShadowMaps)
        self.assertArgIsBOOL(SceneKit.SCNLight.setSampleDistributedShadowMaps_, 0)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(SceneKit.SCNLight.parallaxCorrectionEnabled)
        self.assertArgIsBOOL(SceneKit.SCNLight.setParallaxCorrectionEnabled_, 0)

        self.assertResultIsBOOL(SceneKit.SCNLight.drawsArea)
        self.assertArgIsBOOL(SceneKit.SCNLight.setDrawsArea_, 0)

        self.assertResultIsBOOL(SceneKit.SCNLight.doubleSided)
        self.assertArgIsBOOL(SceneKit.SCNLight.setDoubleSided_, 0)
