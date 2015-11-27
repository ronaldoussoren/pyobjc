from PyObjCTools.TestSupport import *
import objc

import SceneKit

class TestSCNMaterialProperty (TestCase):
    def testConstants(self):
        self.assertIsInstance(SceneKit.SCNModelTransform, unicode)
        self.assertIsInstance(SceneKit.SCNViewTransform, unicode)
        self.assertIsInstance(SceneKit.SCNProjectionTransform, unicode)
        self.assertIsInstance(SceneKit.SCNNormalTransform, unicode)
        self.assertIsInstance(SceneKit.SCNModelViewTransform, unicode)
        self.assertIsInstance(SceneKit.SCNModelViewProjectionTransform, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNMaterialProperty.isHidden)
        self.assertArgIsBOOL(SceneKit.SCNMaterialProperty.setHidden_, 0)

        self.assertArgIsBOOL(SceneKit.SCNMaterialProperty.childNodeWithName_recursively_, 1)

        self.assertArgIsBlock(SceneKit.SCNMaterialProperty.childNodesPassingTest_, 0, b'Z@o^Z')

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(SceneKit.SCNMaterialProperty.castsShadow)
        self.assertArgIsBOOL(SceneKit.SCNMaterialProperty.setCastsShadow_, 0)

        self.assertArgIsBlock(SceneKit.SCNMaterialProperty.enumerateChildNodesUsingBlock_, 0, b'v@o^Z')

        self.assertResultIsBOOL(SceneKit.SCNMaterialProperty.isPaused)
        self.assertArgIsBOOL(SceneKit.SCNMaterialProperty.setPaused_, 0)

    def testProtocols(self):
        objc.protocolNamed('SCNNodeRendererDelegate')

if __name__ == "__main__":
    main()
