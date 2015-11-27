from PyObjCTools.TestSupport import *
import objc

import SceneKit

class TestSCNLight (TestCase):
    @min_os_level('10.8')
    def testConstants(self):
        self.assertIsInstance(SceneKit.SCNLightTypeAmbient, unicode)
        self.assertIsInstance(SceneKit.SCNLightTypeOmni, unicode)
        self.assertIsInstance(SceneKit.SCNLightTypeDirectional, unicode)
        self.assertIsInstance(SceneKit.SCNLightTypeSpot, unicode)

        self.assertEqual(SceneKit.SCNShadowModeForward, 0)
        self.assertEqual(SceneKit.SCNShadowModeDeferred, 1)
        self.assertEqual(SceneKit.SCNShadowModeModulated, 2)

        self.assertIsInstance(SceneKit.SCNLightAttenuationStartKey, unicode)
        self.assertIsInstance(SceneKit.SCNLightAttenuationEndKey, unicode)
        self.assertIsInstance(SceneKit.SCNLightAttenuationFalloffExponentKey, unicode)
        self.assertIsInstance(SceneKit.SCNLightSpotInnerAngleKey, unicode)
        self.assertIsInstance(SceneKit.SCNLightSpotOuterAngleKey, unicode)
        self.assertIsInstance(SceneKit.SCNLightShadowNearClippingKey, unicode)
        self.assertIsInstance(SceneKit.SCNLightShadowFarClippingKey, unicode)


    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNLight.castsShadow)
        self.assertArgIsBOOL(SceneKit.SCNLight.setCastsShadow_, 0)


if __name__ == "__main__":
    main()
