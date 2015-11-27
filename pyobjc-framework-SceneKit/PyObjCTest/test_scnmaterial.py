from PyObjCTools.TestSupport import *
import objc

import SceneKit

class TestSCNMaterial (TestCase):
    def testConstants(self):
        self.assertIsInstance(SceneKit.SCNLightingModelPhong, unicode)
        self.assertIsInstance(SceneKit.SCNLightingModelBlinn, unicode)
        self.assertIsInstance(SceneKit.SCNLightingModelLambert, unicode)
        self.assertIsInstance(SceneKit.SCNLightingModelConstant, unicode)

        self.assertEqual(SceneKit.SCNCullBack, 0)
        self.assertEqual(SceneKit.SCNCullFront, 1)

        self.assertEqual(SceneKit.SCNTransparencyModeAOne, 0)
        self.assertEqual(SceneKit.SCNTransparencyModeRGBZero, 1)

        self.assertEqual(SceneKit.SCNBlendModeAlpha, 0)
        self.assertEqual(SceneKit.SCNBlendModeAdd, 1)
        self.assertEqual(SceneKit.SCNBlendModeSubtract, 2)
        self.assertEqual(SceneKit.SCNBlendModeMultiply, 3)
        self.assertEqual(SceneKit.SCNBlendModeScreen, 4)
        self.assertEqual(SceneKit.SCNBlendModeReplace, 5)


    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNMaterial.isLitPerPixel)
        self.assertArgIsBOOL(SceneKit.SCNMaterial.setLitPerPixel_, 0)

        self.assertResultIsBOOL(SceneKit.SCNMaterial.isDoubleSided)
        self.assertArgIsBOOL(SceneKit.SCNMaterial.setDoubleSided_, 0)

        self.assertResultIsBOOL(SceneKit.SCNMaterial.locksAmbientWithDiffuse)
        self.assertArgIsBOOL(SceneKit.SCNMaterial.setLocksAmbientWithDiffuse_, 0)

        self.assertResultIsBOOL(SceneKit.SCNMaterial.writesToDepthBuffer)
        self.assertArgIsBOOL(SceneKit.SCNMaterial.setWritesToDepthBuffer_, 0)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertResultIsBOOL(SceneKit.SCNMaterial.readsFromDepthBuffer)
        self.assertArgIsBOOL(SceneKit.SCNMaterial.setReadsFromDepthBuffer_, 0)


if __name__ == "__main__":
    main()
